#!/usr/bin/env python3
"""把卡片规范（JSONL）打包成 Anki 可导入的文件。

用法：
  python3 build_anki.py cards.jsonl [more.jsonl ...] --out 生化_第02章.apkg
                        [--media-dir 分子制卡/02_.../images] [--tsv-dir anki_tsv/] [--root-deck 生化]

产物：
  *.apkg   含笔记类型（带样式）、牌组、图片。双击或 Anki → File → Import 即可；再次导入同名 id 的卡会更新而非重复。
  --tsv-dir 时另输出每种笔记类型一个 .txt（带 #separator/#html/#deck column/#tags column 头部），
           供不想用 .apkg 的人用“文本文件导入”；图片需要自己复制到 collection.media。

依赖：pip install genanki
"""

from __future__ import annotations

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cardspec import Card, load_cards, md_to_html  # noqa: E402

try:
    import genanki
except ImportError:  # pragma: no cover
    raise SystemExit("缺少 genanki：pip install genanki")

CSS = """
.card { font-family: -apple-system, "PingFang SC", "Microsoft YaHei", "Noto Sans CJK SC", sans-serif;
        font-size: 20px; line-height: 1.5; text-align: left; color: #1a1a1a; background: #fff; padding: 12px 18px; }
.night_mode .card { color: #e8e8e8; background: #2b2b2b; }
.q { font-size: 22px; font-weight: 600; }
.a { margin-top: 6px; }
.extra { margin-top: 14px; padding-top: 8px; border-top: 1px dashed #bbb; font-size: 15px; color: #666; }
.night_mode .extra { color: #aaa; border-color: #555; }
.tag { display: inline-block; font-size: 13px; color: #888; margin-top: 10px; }
img { max-width: 100%; max-height: 60vh; display: block; margin: 8px auto; }
table { border-collapse: collapse; margin: 8px 0; font-size: 17px; }
th, td { border: 1px solid #999; padding: 4px 10px; vertical-align: top; }
th { background: #f0f0f0; }
.night_mode th { background: #3a3a3a; }
ol, ul { margin: 4px 0 4px 1.2em; padding: 0; }
li { margin: 2px 0; }
code { font-family: Menlo, Consolas, monospace; font-size: 17px; background: #f3f3f3; padding: 0 4px; border-radius: 3px; }
.night_mode code { background: #444; }
.cloze { font-weight: bold; color: #1b6ac9; }
hr#answer { margin: 10px 0; }
"""

FRONT_QA = '<div class="q">{{#Image}}<img src="{{text:Image}}">{{/Image}}{{Front}}</div>'
BACK_QA = ('{{FrontSide}}<hr id="answer"><div class="a">{{#BackImage}}<img src="{{text:BackImage}}">{{/BackImage}}{{Back}}</div>'
           '{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}<div class="tag">{{Tags}}</div>')


def stable_id(name: str) -> int:
    """由名字算出稳定的 model/deck id（genanki 要求 32 位内的随机整数，且每次构建相同）。"""
    return int(hashlib.sha1(name.encode("utf-8")).hexdigest()[:8], 16) | 1


MODEL_QA = genanki.Model(
    stable_id("bio-anki-cards::qa::v1"), "Bio 问答",
    fields=[{"name": "Front"}, {"name": "Back"}, {"name": "Extra"}, {"name": "Image"}, {"name": "BackImage"}],
    templates=[{"name": "问答", "qfmt": FRONT_QA, "afmt": BACK_QA}],
    css=CSS,
)
MODEL_TERM = genanki.Model(
    stable_id("bio-anki-cards::term::v1"), "Bio 术语（可反向）",
    fields=[{"name": "Term"}, {"name": "Definition"}, {"name": "Extra"}, {"name": "Reverse"}],
    templates=[
        {"name": "术语→定义", "qfmt": '<div class="q">{{Term}}</div><div class="tag">说出定义 / 要点</div>',
         "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Definition}}</div>{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}<div class="tag">{{Tags}}</div>'},
        {"name": "定义→术语", "qfmt": '{{#Reverse}}<div class="q">{{Definition}}</div><div class="tag">这是什么？</div>{{/Reverse}}',
         "afmt": '{{FrontSide}}<hr id="answer"><div class="a">{{Term}}</div>{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}<div class="tag">{{Tags}}</div>'},
    ],
    css=CSS,
)
MODEL_CLOZE = genanki.Model(
    stable_id("bio-anki-cards::cloze::v1"), "Bio 填空",
    fields=[{"name": "Text"}, {"name": "Extra"}],
    templates=[{"name": "填空", "qfmt": '<div class="a">{{cloze:Text}}</div>',
                "afmt": '<div class="a">{{cloze:Text}}</div>{{#Extra}}<div class="extra">{{Extra}}</div>{{/Extra}}<div class="tag">{{Tags}}</div>'}],
    css=CSS, model_type=genanki.Model.CLOZE,
)


class Note(genanki.Note):
    @property
    def guid(self):  # 用卡片 id 生成稳定 guid：重复导入同一 id 时 Anki 更新原笔记而不是新建
        return genanki.guid_for("bio-anki-cards", self._card_id)


def make_note(c: Card) -> Note:
    extra = md_to_html(c.extra)
    if c.type == "cloze":
        n = Note(model=MODEL_CLOZE, fields=[md_to_html(c.front, keep_cloze=True), extra], tags=c.tags)
    elif c.type == "term":
        n = Note(model=MODEL_TERM, fields=[md_to_html(c.front), md_to_html(c.back), extra, "y" if c.reverse else ""], tags=c.tags)
    else:  # qa / image 共用问答模型
        n = Note(model=MODEL_QA, fields=[md_to_html(c.front), md_to_html(c.back), extra, c.image or "", c.back_image or ""], tags=c.tags)
    n._card_id = c.id
    return n


def write_tsv(cards: list[Card], out_dir: Path) -> None:
    """每种笔记类型一个文件，带 Anki 文本导入头部。字段内的制表符/换行会被替换，HTML 保留。"""
    out_dir.mkdir(parents=True, exist_ok=True)
    groups = {"qa": [], "term": [], "cloze": []}
    for c in cards:
        groups["qa" if c.type in ("qa", "image") else c.type].append(c)
    spec = {
        "qa": ("Bio 问答", lambda c: [md_to_html(c.front), md_to_html(c.back), md_to_html(c.extra),
                                       f'<img src="{c.image}">' if c.image else "", f'<img src="{c.back_image}">' if c.back_image else ""]),
        "term": ("Bio 术语（可反向）", lambda c: [md_to_html(c.front), md_to_html(c.back), md_to_html(c.extra), "y" if c.reverse else ""]),
        "cloze": ("Bio 填空", lambda c: [md_to_html(c.front, keep_cloze=True), md_to_html(c.extra)]),
    }
    clean = lambda s: s.replace("\t", " ").replace("\r", "").replace("\n", "<br>")
    for kind, items in groups.items():
        if not items:
            continue
        notetype, fn = spec[kind]
        n_fields = len(fn(items[0]))
        lines = ["#separator:tab", "#html:true", f"#notetype:{notetype}", f"#deck column:{n_fields + 2}",
                 f"#tags column:{n_fields + 3}", "#guid column:1"]
        for c in items:
            guid = genanki.guid_for("bio-anki-cards", c.id)
            lines.append("\t".join([guid] + [clean(f) for f in fn(c)] + [c.deck, " ".join(c.tags)]))
        (out_dir / f"{kind}.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--out", type=Path, required=True, help="输出 .apkg 路径")
    ap.add_argument("--media-dir", type=Path, action="append", default=[], help="图片目录，可多次指定")
    ap.add_argument("--tsv-dir", type=Path, default=None, help="同时输出文本导入文件到此目录")
    args = ap.parse_args()

    cards = load_cards(args.files)
    if not cards:
        raise SystemExit("没有卡片")
    decks: dict[str, genanki.Deck] = {}
    media: dict[str, Path] = {}
    for c in cards:
        deck = decks.setdefault(c.deck, genanki.Deck(stable_id("bio-anki-cards::deck::" + c.deck), c.deck))
        deck.add_note(make_note(c))
        for img in (c.image, c.back_image):
            if img and img not in media:
                src = next((d / img for d in args.media_dir if (d / img).is_file()), None)
                if src is None:
                    raise SystemExit(f"[{c.id}] 找不到图片 {img}（--media-dir {args.media_dir}）")
                media[img] = src
    pkg = genanki.Package(list(decks.values()))
    # genanki 以文件名作为媒体名，图片名必须唯一且不带路径
    pkg.media_files = [str(p) for p in media.values()]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    pkg.write_to_file(str(args.out))
    if args.tsv_dir:
        write_tsv(cards, args.tsv_dir)
    n_cards = sum(2 if (c.type == "term" and c.reverse) else (len(set(__import__("re").findall(r"\{\{c(\d+)::", c.front))) if c.type == "cloze" else 1) for c in cards)
    print(f"写出 {args.out}：{len(cards)} 条笔记 / 约 {n_cards} 张卡，{len(decks)} 个牌组，{len(media)} 张图片" + (f"；TSV → {args.tsv_dir}" if args.tsv_dir else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
