#!/usr/bin/env python3
"""从不可变的原始TXT和逐章审读记录生成四列Anki TXT、媒体及覆盖报告。"""
from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import html
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote
import zipfile

BASELINE = 'fce68232f65f9ac6ae21bf526792c9e034eedb3e'
SOURCE = 'd443ed18fd7b95569ebcbfc3b0d54666a6607687'
FILES = {'B': 'SHU_2027_Biochemistry_2514_Basic.txt', 'M': 'SHU_Molecular_Anki.txt'}
HEADER = '#separator:Tab\n#html:true\n#notetype:Basic\n#tags column:3\n#deck column:4\n#columns:Front\tBack\tTags\tDeck\n'


def read_jsonl(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_jsonl(path, values):
    path.write_text(''.join(json.dumps(v, ensure_ascii=False, separators=(',', ':')) + '\n' for v in values))


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def link(path, line=None):
    suffix = f'#L{line}' if line else ''
    return f'https://github.com/kazewwk/test/blob/{SOURCE}/{quote(path, safe="/")}{suffix}'


def original_cards(repo):
    cards = []
    for subject, filename in FILES.items():
        raw = subprocess.check_output(['git', 'show', f'{BASELINE}:anki/{filename}'], cwd=repo).decode()
        rows = csv.reader(io.StringIO('\n'.join(line for line in raw.splitlines() if not line.startswith('#'))), delimiter='\t')
        counts = collections.Counter()
        for row in rows:
            assert len(row) == 4, (filename, '必须为四列', len(row))
            front, back, tags, deck = row
            chapter = re.search(r'(?:章节|章)::(\d+)', tags).group(1)
            counts[chapter] += 1
            card_id = re.search(r'卡ID::(\S+)', tags).group(1) if subject == 'M' else f'B{chapter}-{counts[chapter]:03d}'
            cards.append(dict(id=card_id, chapter=subject+chapter, front=front, back=back, tags=tags, deck=deck, file=filename))
    return cards


def replace_section(back, label, value):
    replacement = f'<b>{label}</b><br>{value}'
    pattern = rf'<b>{re.escape(label)}</b><br>.*?(?=<br><br><b>|$)'
    if re.search(pattern, back):
        return re.sub(pattern, lambda _: replacement, back, count=1)
    pos = back.find('<br><br><b>')
    assert pos >= 0, ('缺少可插入位置', label)
    return back[:pos] + '<br><br>' + replacement + back[pos:]


def fold_optional_sections(back):
    pattern = r'<br><br><b>(解释／边界|补充解释|来源)</b><br>(.*?)(?=<br><br><b>|$)'
    return re.sub(pattern, lambda m: '<br><br><details><summary>' + m[1] +
                  '</summary><br>' + m[2] + '</details>', back, flags=re.S)


def export(repo, source_root):
    audit = repo / 'anki' / 'audit'
    images = {x['id']: x for x in read_jsonl(audit / 'image-index.jsonl')}
    external_path = audit / 'external-images.json'
    external = {x['id']: x for x in json.loads(external_path.read_text())} if external_path.exists() else {}
    assert not (images.keys() & external.keys()), '教材与网络图片编号冲突'
    for record in external.values():
        assert record.get('visually_reviewed') and record.get('academic_review'), ('网络原图尚未复查', record['id'])
    source_image_ids = set(images)
    images.update(external)
    chapters = {x['id']: x for x in json.loads((audit / 'chapters.json').read_text())}
    baseline = original_cards(repo)
    cards = {c['id']: c.copy() for c in baseline}
    updates = collections.defaultdict(list)
    new_cards = []
    front_images = {}
    image_review = {}
    chapter_review = {}
    practice = []
    exercise_audit = []
    for path in sorted((audit / 'edits').glob('*.json')):
        edit = json.loads(path.read_text())
        key = edit['chapter']
        assert key not in chapter_review, ('章节审读记录重复', key)
        chapter_review[key] = edit['review']
        chapter_images = {i for i in source_image_ids if images[i]['chapter'] == key}
        recorded_images = {x['id'] for x in edit['images']}
        assert recorded_images == chapter_images, ('逐图记录缺失或多余', key)
        for item in edit['images']:
            assert item['id'] not in image_review, ('图片记录重复', item['id'])
            assert item['reason'], ('图片缺少处理原因', item['id'])
            image_review[item['id']] = item
        for update in edit.get('updates', []):
            assert update['id'] in cards, ('原卡不存在', update['id'])
            updates[update['id']].append(update)
        for item in edit.get('new_cards', []):
            assert item['id'] not in cards, ('卡片审读编号重复', item['id'])
            assert isinstance(item['criteria'], list) and all(isinstance(t, str) and t.strip() for t in item['criteria']), ('新卡评分点必须为列表', item['id'])
            target_chapter = item.get('target_chapter', key)
            assert target_chapter in chapters and not chapters[target_chapter].get('auxiliary'), ('新卡缺少有效章节', item['id'])
            template = next(c for c in baseline if c['chapter'] == target_chapter)
            tags = [t for t in template['tags'].split() if not t.startswith(('卡ID::', '深度::', '能力::', '卡型::'))]
            tags += [f'卡ID::{item["id"]}', f'深度::{item["depth"]}', f'能力::{item["ability"]}', '优化::图片核对_20261009']
            criteria = '<br>'.join(f'{n}. {html.escape(t)}' for n, t in enumerate(item['criteria'], 1))
            back = f'<b>核心答案</b><br>{html.escape(item["core"])}<br><br><b>通过标准</b><br>{criteria}'
            if item.get('extra'):
                back += '<br><br><b>补充解释</b><br>' + html.escape(item['extra'])
            back += '<br><br><b>来源</b><br>' + html.escape(item['source'])
            back += f'<br><a href="{link(chapters[key]["path"])}">查看章节来源</a>'
            cards[item['id']] = dict(id=item['id'], chapter=target_chapter, front=item['front'], back=back, tags=' '.join(tags), deck=template['deck'], file=template['file'])
            updates[item['id']].append({k: item[k] for k in ('image_ids', 'image_refs') if k in item})
            if item.get('front_image_ids'):
                front_images[item['id']] = list(dict.fromkeys(item['front_image_ids']))
            new_cards.append(item['id'])
        for item in edit.get('practice', []):
            practice.append({'chapter': key, **item})
        for item in edit.get('exercise_audit', []):
            exercise_audit.append({'chapter': key, **item})

    # Copy only figures selected for daily review. The ledger still accounts for every source image.
    media = repo / 'anki' / 'media'
    media.mkdir(exist_ok=True)
    media_used = {}

    def render_image(image_id, caption=True):
        assert image_id in images, ('图片审读编号不存在', image_id)
        record = images[image_id]
        src = (repo if record.get('external_original') else source_root) / record['path']
        assert src.is_file(), ('源图片不存在', str(src))
        assert sha(src) == record['sha256'], ('源图片校验和不符', str(src))
        filename = f'bioanki_{record["sha256"][:20]}{src.suffix.lower()}'
        dst = media / filename
        if not dst.exists():
            shutil.copyfile(src, dst)
        assert sha(dst) == record['sha256'], ('媒体校验和不符', filename)
        media_used[filename] = record['sha256']
        label = record.get('source') or (record['refs'][0]['source'] if record.get('refs') else '教材原图')
        return (f'<span>{html.escape(label)} · 原图</span><br>' if caption else '') + \
            f'<img src="{filename}" style="max-width:100%;height:auto;">'

    for card_id, image_ids in front_images.items():
        cards[card_id]['front'] += '<br><br>' + '<br><br>'.join(render_image(i, False) for i in image_ids)

    for card_id, entries in updates.items():
        card = cards[card_id]
        notes, selected, refs = [], [], []
        replacements = {}
        for item in entries:
            for field, label in [('replace_core', '核心答案'), ('replace_criteria', '通过标准')]:
                if field in item:
                    if field == 'replace_criteria':
                        assert isinstance(item[field], list) and all(isinstance(t, str) and t.strip() for t in item[field]), ('评分点必须为列表', card_id)
                    assert field not in replacements or replacements[field] == item[field], ('原卡修订冲突，请先核对合并', card_id, field)
                    replacements[field] = item[field]
                    value = html.escape(item[field]) if field == 'replace_core' else '<br>'.join(f'{n}. {html.escape(t)}' for n, t in enumerate(item[field], 1))
                    card['back'] = replace_section(card['back'], label, value)
            notes += [item[k] for k in ('append_explanation', 'image_analysis') if item.get(k)]
            selected += item.get('image_ids', [])
            refs += item.get('image_refs', [])
        selected = list(dict.fromkeys(selected))
        refs = list(dict.fromkeys(selected + front_images.get(card_id, []) + refs))
        blocks = []
        for image_id in selected:
            blocks.append(render_image(image_id))
        if notes:
            corrected_figure = any(image_review.get(i, {}).get('disposition') == 'corrected'
                                   for i in selected + front_images.get(card_id, []))
            details = '<details open>' if corrected_figure else '<details>'
            blocks.append(details + '<summary>读图要点与勘误</summary><br>' +
                          '<br><br>'.join(html.escape(t) for t in dict.fromkeys(notes)) + '</details>')
        if refs:
            source_links = []
            for image_id in refs:
                assert image_id in images, ('图片出处审读编号不存在', image_id)
                record = images[image_id]
                lines = record.get('refs', [])
                if record.get('external_original'):
                    url, label = record['url'], record['source']
                    source_links.append(f'<a href="{record["license_url"]}">{html.escape(record["creator"])} · {html.escape(record["license"])} · 原图未改动</a>')
                elif lines:
                    r = lines[0]
                    chapter = chapters[record['chapter']]
                    url = link(r.get('document', chapter['path']), r['line'])
                    label = f'{image_id} · {r["source"]} L{r["line"]}'
                else:
                    url, label = link(record['path']), f'{image_id} · 图片文件'
                source_links.append(f'<a href="{url}">{html.escape(label)}</a>')
                if record.get('recovered_from_missing_reference'):
                    source_links.append(f'<a href="{link(record["path"])}">{html.escape(image_id)} · 补回的教材原图</a>')
            blocks.append('<details><summary>图片来源</summary>' + '<br>'.join(source_links) + '</details>')
        if blocks:
            addition = '<br><br><b>图示核对</b><br>' + '<br><br>'.join(blocks)
            pos = card['back'].find('<br><br><b>来源</b>')
            card['back'] = card['back'][:pos] + addition + card['back'][pos:] if pos >= 0 else card['back'] + addition
        if '优化::图片核对_20261009' not in card['tags'].split():
            card['tags'] += ' 优化::图片核对_20261009'

    for filename in media.iterdir():
        if filename.name.startswith('bioanki_') and filename.name not in media_used:
            filename.unlink()

    ordered = [cards[c['id']] for c in baseline] + [cards[i] for i in new_cards]
    for c in ordered:
        c['back'] = c['back'].replace('/blob/ccr-f99fd7ec-4tkepr/', f'/blob/{SOURCE}/')
        c['back'] = fold_optional_sections(c['back'])
    for subject, filename in FILES.items():
        target = repo / 'anki' / filename
        with target.open('w', newline='') as handle:
            handle.write(HEADER)
            writer = csv.writer(handle, delimiter='\t', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
            for c in ordered:
                if c['chapter'].startswith(subject):
                    writer.writerow([c['front'], c['back'], c['tags'], c['deck']])

    # Meaningful invariants: matching fronts and decks, import layout, media, and evidence coverage.
    for c in baseline:
        assert cards[c['id']]['front'] == c['front'], ('原卡正面变化，可能损失匹配', c['id'])
        assert cards[c['id']]['deck'] == c['deck'], ('原牌组变化', c['id'])
    for subject, filename in FILES.items():
        rows = list(csv.reader(io.StringIO('\n'.join(line for line in (repo/'anki'/filename).read_text().splitlines() if not line.startswith('#'))), delimiter='\t'))
        expected = [c for c in ordered if c['chapter'].startswith(subject)]
        assert len(rows) == len(expected)
        assert all(len(r) == 4 and all('\n' not in f and '\t' not in f for f in r) for r in rows)
        assert len({r[0] for r in rows}) == len(rows), ('同一导入文件正面重复', filename)
        for row, card in zip(rows, expected):
            assert row == [card['front'], card['back'], card['tags'], card['deck']]
            assert '{{c' not in card['front'] + card['back'], ('此导出为Basic，不能混入Cloze', card['id'])
            for name in re.findall(r'<img\s+[^>]*src="([^"]+)"', card['front'] + card['back']):
                assert name in media_used and (media/name).is_file(), ('媒体缺失', name)
    for record in image_review.values():
        for card_id in record['cards']:
            assert card_id in cards, ('图片覆盖的卡不存在', record['id'], card_id)

    ledger = []
    for image_id, record in images.items():
        if image_id not in source_image_ids:
            continue
        entry = {'id': image_id, 'chapter': record['chapter'], 'path': record['path'], 'sha256': record['sha256']}
        entry.update(image_review.get(image_id, {'disposition': 'pending', 'cards': [], 'reason': '尚未完成逐图视觉审读'}))
        ledger.append(entry)
    write_jsonl(audit/'image-review.jsonl', ledger)
    # Inventory status follows the human review ledger, rather than keeping the initial pending marker.
    inventory = []
    for image_id, record in images.items():
        if image_id in source_image_ids:
            inventory.append({**record, 'review_status': 'reviewed' if image_id in image_review else 'pending'})
    write_jsonl(audit/'image-index.jsonl', inventory)
    write_jsonl(audit/'media-manifest.jsonl', [{'file': n, 'sha256': s} for n, s in sorted(media_used.items())])
    counts = collections.Counter(c['chapter'] for c in ordered)
    learning_chapters = [key for key, info in chapters.items() if not info.get('auxiliary')]
    auxiliary = [key for key, info in chapters.items() if info.get('auxiliary')]
    status = {'baseline_commit': BASELINE, 'source_commit': SOURCE, 'original_cards': len(baseline), 'new_cards': len(new_cards), 'updated_existing_cards': len(set(updates)-set(new_cards)), 'total_cards': len(ordered), 'reviewed_chapters': sum(key in chapter_review for key in learning_chapters), 'total_chapters': len(learning_chapters), 'reviewed_auxiliary_folders': sum(key in chapter_review for key in auxiliary), 'total_auxiliary_folders': len(auxiliary), 'reviewed_images': len(image_review), 'total_images': len(source_image_ids), 'external_original_images': len(external), 'generated_images': 0, 'media_files': len(media_used), 'cards_with_images': sum('<img ' in c['front'] + c['back'] for c in ordered), 'cards_with_question_images': len(front_images), 'basic_cards': len(ordered), 'cloze_cards': 0, 'chapter_cards': dict(sorted(counts.items())), 'chapter_review': chapter_review}
    (audit/'status.json').write_text(json.dumps(status, ensure_ascii=False, indent=2)+'\n')
    with zipfile.ZipFile(repo/'anki'/'biology_anki_media.zip', 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for filename in sorted(media_used):
            info = zipfile.ZipInfo(filename, date_time=(2026,10,9,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, (media/filename).read_bytes())
    practice_text = '# 整题训练（独立于每日卡片）\n\n'
    for item in practice:
        assert item.get('front') and item.get('answer'), ('练习缺少题干或答案', item['chapter'])
        practice_text += f'## {item["chapter"]} {item["front"]}\n\n{item["answer"]}\n\n'
        if item.get('source'):
            practice_text += '来源：' + item['source'] + '\n\n'
        for image_id in item.get('image_ids', []):
            assert image_id in images, ('练习图片不存在', image_id)
            record = images[image_id]
            url = record['url'] if record.get('external_original') else link(record['path']) + '?raw=1'
            practice_text += f'![{image_id} 教材原图]({url})\n\n'
    (audit/'practice.md').write_text(practice_text.rstrip()+'\n')
    exercise_text = '# 习题审读与处置记录\n\n这些条目记录原教材习题的审读、条件与入卡处置；完整题干见链接中的原资料。\n\n'
    for item in exercise_audit:
        doc = item.get('document', chapters[item['chapter']]['path'])
        exercise_text += f'## {item["chapter"]} {item["source"]}\n\n{item["decision"]}。{item["note"]}\n\n'
        exercise_text += '关联卡：' + '、'.join(item.get('cards', [])) + '\n\n'
        exercise_text += f'[原教材章节]({link(doc, item.get("line"))})\n\n'
    (audit/'exercise-audit.md').write_text(exercise_text.rstrip()+'\n')
    errata = []
    limitations = []
    for path in sorted((audit/'edits').glob('*.json')):
        edit = json.loads(path.read_text())
        key = edit['chapter']
        for item in edit.get('source_errata', []):
            doc = item.get('document', chapters[key]['path'])
            errata.append({'chapter': key, **item, 'document': doc, 'url': link(doc, item['line'])})
        for item in edit.get('uncertain', []):
            item = item if isinstance(item, dict) else {'issue': item}
            doc = item.get('document') or (item.get('source') if str(item.get('source', '')).endswith('.md') else chapters[key]['path'])
            limitations.append({'chapter': key, **item, 'document': doc, 'url': link(doc, item.get('line'))})
    write_jsonl(audit/'source-errata.jsonl', errata)
    write_jsonl(audit/'source-limitations.jsonl', limitations)
    print(json.dumps({k: v for k, v in status.items() if k not in ('chapter_cards', 'chapter_review')}, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root', type=Path, required=True, help='包含生化制卡、分子制卡的源工作树；源提交见SOURCE常量')
    args = parser.parse_args()
    export(Path(__file__).resolve().parents[1], args.source_root.resolve())
