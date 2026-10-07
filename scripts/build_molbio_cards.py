#!/usr/bin/env python3
"""生成 `分子制卡/`：以朱玉贤《现代分子生物学》为主干，把

- Watson《基因的分子生物学》第七版中译本（书籍/03）的各章/各大节，
- Campbell Biology 第 16–21 章的各 Concept（书籍/01），
- Lehninger Principles of Biochemistry 第 9、24–28 章的各小节（书籍/02）

插入对应的中文章节。每个中文章节一个子文件夹，内含合并后的 Markdown 和该章引用的全部图片。
插入位置为对应中文二级节（N.M）的末尾；各来源的章首导言放在中文章开头，
小结/习题/Key Terms/Review 放在中文章末尾。

用法：python3 scripts/build_molbio_cards.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_biochem_cards import (  # noqa: E402
    EN_BOOK, EN_CHAPTER_TITLE, IMAGE_RE, BOOKS, copy_images, demote_headings,
    parse_english, read_lines, rewrite_images,
)

ROOT = Path(__file__).resolve().parent.parent
ZH_BOOK = BOOKS / "09_现代分子生物学"
W_BOOK = BOOKS / "03_基因的分子生物学_第七版"
C_BOOK = BOOKS / "01_Campbell_Biology"
OUT = ROOT / "分子制卡"

W_SOURCE = "Watson《基因的分子生物学》第七版中译本（书籍/03_基因的分子生物学_第七版）"
C_SOURCE = "Campbell Biology（书籍/01_Campbell_Biology）"
L_SOURCE = "Lehninger Principles of Biochemistry（书籍/02_生物化学原理）"

# ---------------------------------------------------------------------------
# Watson 中译本：每章拆成若干片段，(切分标题, 目标中文节)。None 表示章首到第一个切分标题。
# 没有列出的章整章作为一个片段。切分标题按去空格后的全文匹配，只在“小结”之前查找。
W_SPLITS = {
    7: [(None, "5.1"), ("核酸：基本方法", "5.2"), ("基因组学", "11.2"), ("蛋白质", "5.5"), ("蛋白质组学", "5.5")],
    13: [(None, "3.5"), ("真核生物的转录", "3.6")],
    15: [(None, "4.4"), ("信使 RNA", "3.4"), ("转运RNA", "4.2"), ("氨基酸连接到 tRNA 上", "4.2"),
         ("核糖体", "4.3"), ("翻译的起始", "4.4"), ("翻译延伸", "4.4"), ("翻译终止", "4.4"), ("翻译的调控", "8.5")],
    18: [(None, "7.1"), ("转录起始的调控：原核生物的实例", "7.4"), ("λ噬菌体：调控的层次", "7.6"),
         ("逆向调控：RNA 合成和稳定性控制相互影响并决定基因表达", "7.7")],
    19: [(None, "8.2"), ("组蛋白与 DNA 修饰导致的基因“沉默”", "8.3")],
    20: [(None, "7.7"), ("调节 RNA 在真核生物中广泛存在", "8.4")],
}
W_WHOLE = {1: "1.1", 2: "1.2", 3: "2.2", 4: "2.2", 5: "3.1", 6: "4.4", 8: "2.1", 9: "2.4", 10: "2.5",
           11: "2.5", 12: "2.6", 14: "3.8", 16: "4.1", 17: "3.12", 21: "10.1", 22: "8.5"}
# Watson 各章的小结/参考文献/习题（及附录 2 中该章的答案）放到哪个中文章末尾。
W_HOME = {1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 4, 7: 5, 8: 2, 9: 2, 10: 2, 11: 2, 12: 2, 13: 3, 14: 3,
          15: 4, 16: 4, 17: 3, 18: 7, 19: 8, 20: 8, 21: 10, 22: 8}

# Campbell：Concept -> 中文节；章首导言与 Chapter Review 放到 C_HOME 章。
C_MAP = {
    "16.1": "1.1", "16.2": "2.3", "16.3": "2.1",
    "17.1": "3.2", "17.2": "3.3", "17.3": "3.8", "17.4": "4.4", "17.5": "2.5",
    "18.1": "7.2", "18.2": "8.2", "18.3": "8.4", "18.4": "10.1", "18.5": "9.1",
    "19.1": "9.2", "19.2": "9.2", "19.3": "9.4",
    "20.1": "5.2", "20.2": "6.1", "20.3": "6.2", "20.4": "9.6",
    "21.1": "11.1", "21.2": "11.1", "21.3": "11.4", "21.4": "2.1", "21.5": "11.5", "21.6": "11.5",
}
C_HOME = {16: 2, 17: 3, 18: 8, 19: 9, 20: 5, 21: 11}

# Lehninger：小节 -> 中文节；章首导言与章末（Key Terms、习题、简答）放到 L_HOME 章。
L_MAP = {
    "9.1": "5.2", "9.2": "6.1", "9.3": "11.1",
    "24.1": "2.1", "24.2": "2.2", "24.3": "2.1",
    "25.1": "2.4", "25.2": "2.5", "25.3": "2.6",
    "26.1": "3.6", "26.2": "3.8", "26.3": "9.2", "26.4": "3.11",
    "27.1": "4.1", "27.2": "4.4", "27.3": "4.6",
    "28.1": "7.1", "28.2": "7.4", "28.3": "8.2",
}
L_HOME = {9: 5, 24: 2, 25: 2, 26: 3, 27: 4, 28: 7}

ZH_SEC_RE = re.compile(r"^#{1,3}\s*(\d+)\.(\d+)\s+\S")
ZH_END_RE = re.compile(r"^#{1,3}\s*(思考题|参考文献)\s*$")
W_PART_RE = re.compile(r"^##\s*第\s*\d+\s*篇")
C_CONCEPT_RE = re.compile(r"^#{1,2}\s*Concept\s+(\d+)\.(\d+)\s*:?\s*(.*)$")
C_REVIEW_RE = re.compile(r"^#{1,2}\s*(Chapter \d+ Review|Summary of Key Concepts)\s*$")


def norm(s: str) -> str:
    return re.sub(r"\s+", "", re.sub(r"^#+", "", s)).strip()


def heading_text(line: str) -> str:
    return re.sub(r"^#{1,6}\s*", "", line).strip()


# ---------------------------------------------------------------------------
def parse_watson():
    """返回 pieces[(ch, target, title, lines)]、ends{ch: lines}、appendix{name: lines}、front lines。"""
    files = {}
    for path in sorted((W_BOOK / "chapters").glob("*.md")):
        m = re.match(r"^\d{3}_第(\d+)章_(.+)\.md$", path.name)
        if m:
            files[int(m.group(1))] = (m.group(2).replace("_", "、"), path)
    if sorted(files) != list(range(1, 23)):
        raise SystemExit(f"Watson 章号不完整：{sorted(files)}")

    pieces, ends, appendix = [], {}, {}
    carry: list[str] = []  # 上一章文件末尾的“第 N 篇”篇首页，归入下一章
    answers: dict[int, list[str]] = {}
    for ch in range(1, 23):
        title, path = files[ch]
        lines = read_lines(path)
        part_idx = next((i for i, l in enumerate(lines) if W_PART_RE.match(l)), None)
        tail: list[str] = []
        if part_idx is not None:
            tail, lines = lines[part_idx:], lines[:part_idx]
        if ch == 22:
            # 第 6 篇附录：附录 1 模式生物 / 附录 2 答案 / 索引 / 版权页
            a2 = next(i for i, l in enumerate(tail) if re.match(r"^#{1,2}\s*附录\s*2", l))
            idx = next(i for i, l in enumerate(tail) if re.match(r"^#{1,2}\s*索引\s*$", l))
            blurb = next(i for i, l in enumerate(tail) if re.match(r"^#{1,2}\s*内容简介\s*$", l) and i > idx)
            appendix["Watson中译本_附录1_模式生物"] = tail[:a2]
            appendix["Watson中译本_索引"] = tail[idx:blurb]
            appendix["Watson中译本_版权页"] = tail[blurb:]
            cur = None
            for l in tail[a2:idx]:
                m = re.match(r"^##\s*第\s*(\d+)\s*章\s*$", l)
                if m:
                    cur = int(m.group(1))
                    answers[cur] = []
                elif cur is not None:
                    answers[cur].append(l)
            tail = []
        lines = carry + lines
        carry = tail

        end_idx = next((i for i, l in enumerate(lines) if re.match(r"^##\s*小结\s*$", l)), None)
        if end_idx is None:
            end_idx = next(i for i, l in enumerate(lines) if re.match(r"^##\s*参考文献\s*$", l))
        body, end = lines[:end_idx], lines[end_idx:]

        if ch in W_SPLITS:
            cuts = []
            pos = 0
            for head, target in W_SPLITS[ch]:
                if head is None:
                    cuts.append((0, target, f"{title}（章首）"))
                    continue
                j = next((i for i in range(pos, len(body)) if body[i].startswith("##") and norm(body[i]) == norm(head)), None)
                if j is None:
                    raise SystemExit(f"Watson 第{ch}章找不到切分标题“{head}”")
                cuts.append((j, target, head))
                pos = j + 1
            for k, (a, target, head) in enumerate(cuts):
                b = cuts[k + 1][0] if k + 1 < len(cuts) else len(body)
                pieces.append((ch, target, head, body[a:b]))
        else:
            pieces.append((ch, W_WHOLE[ch], title, body))
        ends[ch] = end
    for ch, ans in answers.items():
        ends[ch] = ends[ch] + ["", "### 附录 2：本章偶数习题答案", ""] + ans
    front = read_lines(W_BOOK / "chapters" / "000_front_matter.md")
    titles = {ch: files[ch][0] for ch in files}
    return pieces, ends, appendix, front, titles


def parse_campbell():
    chapters = {}
    for n in C_HOME:
        path = next((C_BOOK / "chapters").glob(f"{n:03d}_*.md"))
        lines = read_lines(path)
        title = re.sub(r"^#\s*第\d+章\s*", "", lines[0]).strip()
        starts = []
        want = 1
        for i, l in enumerate(lines):
            m = C_CONCEPT_RE.match(l)
            if m and int(m.group(1)) == n and int(m.group(2)) == want:
                starts.append((f"{n}.{want}", i, m.group(3).strip()))
                want += 1
        review = next(i for i, l in enumerate(lines) if i > starts[-1][1] and C_REVIEW_RE.match(l))
        expected = sorted((k for k in C_MAP if k.split(".")[0] == str(n)), key=lambda k: int(k.split(".")[1]))
        if [s[0] for s in starts] != expected:
            raise SystemExit(f"Campbell 第{n}章 Concept 不符：{[s[0] for s in starts]} vs {expected}")
        secs = {}
        for k, (key, i, ctitle) in enumerate(starts):
            stop = starts[k + 1][1] if k + 1 < len(starts) else review
            secs[key] = (ctitle, lines[i:stop])
        chapters[n] = {"title": title, "intro": lines[:starts[0][1]], "sections": secs, "end": lines[review:]}
    return chapters


# ---------------------------------------------------------------------------
def zh_chapters():
    for path in sorted((ZH_BOOK / "chapters").glob("*.md")):
        m = re.match(r"^\d{3}_第(\d+)章_(.+)\.md$", path.name)
        if m:
            yield int(m.group(1)), m.group(2), path


def zh_bounds(lines: list[str], ch: int):
    """{N.M: (起, 止)}，章首导言结束行，章末行（索引之前）。"""
    end_marker = next((i for i, l in enumerate(lines) if ZH_END_RE.match(l)), len(lines))
    heads = []
    want = 1
    for i, l in enumerate(lines[:end_marker]):
        m = ZH_SEC_RE.match(l)
        if m and int(m.group(1)) == ch and int(m.group(2)) == want:
            heads.append((f"{ch}.{want}", i))
            want += 1
    if not heads:
        raise SystemExit(f"中文第{ch}章没有找到二级节")
    bounds = {k: (i, heads[j + 1][1] if j + 1 < len(heads) else end_marker) for j, (k, i) in enumerate(heads)}
    return bounds, heads[0][1]


def block(tag: str, label: str, title: str, source: str, body: list[str], level: int = 4, prefix: str = "[EN]") -> list[str]:
    return ["", f"<!-- {tag}-BEGIN {label} -->", "", f"### 【{title}】", "", f"> {source}", "",
            *demote(body, level, prefix), "", f"<!-- {tag}-END {label} -->", ""]


def demote(lines: list[str], level: int, prefix: str) -> list[str]:
    out = []
    in_math = False
    for line in lines:
        if line.strip() == "$$":
            in_math = not in_math
        m = None if in_math else re.match(r"^#{1,6}\s+(.*)$", line)
        out.append(f"{'#' * level} {prefix} {m.group(1)}" if m else line)
    return out


def main():
    en_all, _ = parse_english()
    w_pieces, w_ends, w_appendix, w_front, w_titles = parse_watson()
    camp = parse_campbell()

    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    img_dirs = [ZH_BOOK / "merged" / "images", W_BOOK / "merged" / "images",
                C_BOOK / "merged" / "images", EN_BOOK / "merged" / "images"]
    missing: list[str] = []
    mapping = {"中文主干": ZH_BOOK.name, "中文对照": W_BOOK.name,
               "英文来源": [C_BOOK.name + "（第16–21章）", EN_BOOK.name + "（第9、24–28章）"], "章节": []}
    rows = []

    # 按中文章/节归集
    sec_inserts: dict[str, list[tuple[str, int, list[str]]]] = {}  # "N.M" -> [(kind, order, lines)]
    head_inserts: dict[int, list[tuple[int, list[str]]]] = {}
    tail_inserts: dict[int, list[tuple[int, list[str]]]] = {}
    placed: dict[int, list[str]] = {}

    def add_sec(target, kind, order, body, desc):
        sec_inserts.setdefault(target, []).append((kind, order, body))
        placed.setdefault(int(target.split(".")[0]), []).append(desc)

    for order, (ch, target, title, body) in enumerate(w_pieces):
        add_sec(target, "W", order, block(
            "W", f"Watson {ch} {title}", f"中文对照 Watson 第{ch}章：{title}",
            f"来源：{W_SOURCE} 第{ch}章 {w_titles[ch]}。", body, 4, "[W]"), f"Watson 第{ch}章「{title}」 → {target}")
    for ch, end in w_ends.items():
        home = W_HOME[ch]
        tail_inserts.setdefault(home, []).append((ch, block(
            "W", f"Watson {ch} 章末", f"中文对照 Watson 第{ch}章章末：小结、参考文献、习题",
            f"来源：{W_SOURCE} 第{ch}章 {w_titles[ch]} 章末，附录 2 中该章偶数习题答案附后。", end, 4, "[W]")))
    for n, c in camp.items():
        head_inserts.setdefault(C_HOME[n], []).append((200 + n, block(
            "C", f"Campbell {n} 导言", f"英文对应 Campbell 第{n}章导言：{c['title']}",
            f"来源：{C_SOURCE} 第{n}章章首（Key Concepts 与引言）。", c["intro"], 4)))
        for key, (ctitle, body) in c["sections"].items():
            add_sec(C_MAP[key], "C", 200 + int(key.split(".")[1]), block(
                "C", f"Campbell {key}", f"英文对应 Campbell Concept {key}：{ctitle}",
                f"来源：{C_SOURCE} 第{n}章 {c['title']}，Concept {key}。", body, 4), f"Campbell Concept {key} → {C_MAP[key]}")
        tail_inserts.setdefault(C_HOME[n], []).append((200 + n, block(
            "C", f"Campbell {n} Review", f"英文对应 Campbell 第{n}章章末：Chapter Review",
            f"来源：{C_SOURCE} 第{n}章 Summary of Key Concepts 与 Test Your Understanding。", c["end"], 3)))
    for key, target in L_MAP.items():
        n = int(key.split(".")[0])
        body = en_all[n]["sections"][key]
        t = re.sub(rf"^{re.escape(key)}\s*", "", heading_text(body[0]))
        add_sec(target, "L", 300 + int(key.split(".")[1]), block(
            "L", f"Lehninger {key}", f"英文对应 Lehninger §{key}：{t}",
            f"来源：{L_SOURCE} 第{n}章 {EN_CHAPTER_TITLE[n]}，§{key}。", body[1:], 4), f"Lehninger §{key} → {target}")
    for n, home in L_HOME.items():
        head_inserts.setdefault(home, []).append((300 + n, block(
            "L", f"Lehninger {n} 导言", f"英文对应 Lehninger 第{n}章导言：{EN_CHAPTER_TITLE[n]}",
            f"来源：{L_SOURCE} 第{n}章章首。", en_all[n]["intro"], 4)))
        tail_inserts.setdefault(home, []).append((300 + n, block(
            "L", f"Lehninger {n} 章末", f"英文对应 Lehninger 第{n}章章末：Key Terms、习题与简答",
            f"来源：{L_SOURCE} 第{n}章章末及书末 Abbreviated Solutions 第{n}章。",
            en_all[n]["end"] + ["", f"## Abbreviated Solutions — Chapter {n}", ""] + en_all[n]["solutions"], 3)))

    # 前置内容
    front_dir = OUT / "00_中文教材前置内容"
    front_dir.mkdir()
    for name, path_or_lines in [("现代分子生物学_前置内容", ZH_BOOK / "chapters" / "000_front_matter.md"),
                                ("Watson中译本_前置内容", w_front)]:
        text = "\n".join(path_or_lines) if isinstance(path_or_lines, list) else path_or_lines.read_text(encoding="utf-8")
        copy_images(text, img_dirs, front_dir / "images", missing)
        (front_dir / f"{name}.md").write_text(rewrite_images(text), encoding="utf-8")

    app_dir = OUT / "99_附录_无对应章节"
    app_dir.mkdir()

    seen = []
    for ch, title, path in zh_chapters():
        seen.append(ch)
        lines = read_lines(path)
        if ch == 11:  # 书末索引混在最后一章文件里
            idx = next(i for i, l in enumerate(lines) if re.match(r"^##\s*A\s*$", l) and i > 400)
            w_appendix["现代分子生物学_索引"] = lines[idx:]
            lines = lines[:idx]
        bounds, intro_end = zh_bounds(lines, ch)
        heading_of = {k: heading_text(lines[i]) for k, (i, _) in bounds.items()}
        at: dict[int, list[str]] = {}
        for key, items in sec_inserts.items():
            if int(key.split(".")[0]) != ch:
                continue
            if key not in bounds:
                raise SystemExit(f"中文第{ch}章没有 {key} 节")
            stop = bounds[key][1]
            for kind, order, body in sorted(items, key=lambda x: ({"W": 0, "C": 1, "L": 2}[x[0]], x[1])):
                at.setdefault(stop, []).extend(body)
        for order, body in sorted(head_inserts.get(ch, [])):
            at.setdefault(intro_end, []).extend(body)
        for order, body in sorted(tail_inserts.get(ch, [])):
            at.setdefault(len(lines), []).extend(body)
        for pos in sorted(at, reverse=True):
            lines[pos:pos] = at[pos]

        summary = ["", "> **本章插入内容**（中文对照与英文对应，插在所列中文节末尾；导言在章首，小结/习题/Review 在章末）", ">"]
        for d in placed.get(ch, []):
            k = d.rsplit("→ ", 1)[1]
            summary.append(f"> - {d.rsplit(' → ', 1)[0]} → {heading_of.get(k, k)}")
        heads = [f"Campbell 第{n}章" for n, h in C_HOME.items() if h == ch] + \
                [f"Lehninger 第{n}章" for n, h in L_HOME.items() if h == ch]
        tails = [f"Watson 第{n}章" for n, h in W_HOME.items() if h == ch]
        if heads:
            summary.append(f"> - 章首导言与章末：{'、'.join(heads)}")
        if tails:
            summary.append(f"> - 章末小结/习题：{'、'.join(tails)}")
        if len(summary) == 3:
            summary.append("> - 无")
        lines[1:1] = summary

        name = f"{ch:02d}_第{ch}章_{title}"
        folder = OUT / name
        folder.mkdir()
        text = "\n".join(lines)
        n_img = copy_images(text, img_dirs, folder / "images", missing)
        (folder / f"{name}.md").write_text(rewrite_images(text), encoding="utf-8")
        rows.append((ch, name, placed.get(ch, []), heads, tails, n_img))
        mapping["章节"].append({"中文章": ch, "文件夹": name, "插入": placed.get(ch, []),
                               "章首导言与章末": heads, "章末小结与习题": tails, "图片数": n_img})
    if seen != list(range(1, 12)):
        raise SystemExit(f"中文章号不完整：{seen}")

    for name, body in w_appendix.items():
        text = "\n".join(body)
        copy_images(text, img_dirs, app_dir / "images", missing)
        (app_dir / f"{name}.md").write_text(rewrite_images(text), encoding="utf-8")

    (OUT / "对应关系.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_readme(rows, missing, w_titles)
    if missing:
        print(f"缺失图片 {len(missing)} 个，见 README")
    print(f"完成：{len(rows)} 章；Watson 片段 {len(w_pieces)}，Campbell Concept {len(C_MAP)}，Lehninger 小节 {len(L_MAP)}")


def write_readme(rows, missing, w_titles):
    out = [
        "# 分子制卡", "",
        "以朱玉贤《现代分子生物学》为主干，把 Watson《基因的分子生物学》第七版中译本、Campbell Biology 第 16–21 章、"
        "Lehninger *Principles of Biochemistry* 第 9、24–28 章的对应内容插入各章，便于制作卡片。", "",
        "## 目录结构", "",
        "- 每个 `NN_第N章_…/` 对应《现代分子生物学》一章：`NN_第N章_….md` 为合并文本，`images/` 为该章引用的全部图片（四本书的都在），链接为相对路径 `images/…`。",
        "- `00_中文教材前置内容/`：《现代分子生物学》与 Watson 中译本的目录、前言。",
        "- `99_附录_无对应章节/`：Watson 附录 1（模式生物）、Watson 索引与版权页、《现代分子生物学》书末索引。",
        "- `对应关系.json`：机器可读的对应表。", "",
        "## 合并规则", "",
        "1. 《现代分子生物学》原文完整保留，顺序不变。",
        "2. 三个来源以“片段”为单位插在对应中文二级节（N.M）的**末尾**：Watson 按章或按大节拆分（第 7、13、15、18、19、20 章拆分，其余整章）；Campbell 按 Concept；Lehninger 按 §N.M 小节。",
        "3. 块标记：Watson `<!-- W-BEGIN … -->`，标题 `### 【中文对照 Watson 第N章：…】`，内部标题降为 `#### [W] …`；Campbell `<!-- C-BEGIN … -->`、Lehninger `<!-- L-BEGIN … -->`，标题 `### 【英文对应 …】`，内部标题 `#### [EN] …`。可按标记整体检索或剔除。",
        "4. 同一插入点的顺序：Watson → Campbell → Lehninger；同一来源按原书顺序。",
        "5. Campbell、Lehninger 各章的章首导言放在对应中文章开头；Campbell Review、Lehninger Key Terms/习题/简答、Watson 小结/参考文献/习题（附录 2 答案附后）放在对应中文章末尾。",
        "6. 每章开头有一段“本章插入内容”清单。", "",
        "对应关系按主题人工判定；觉得某处放得不合适，改 `scripts/build_molbio_cards.py` 里的 `W_SPLITS/W_WHOLE/C_MAP/L_MAP` 后重新运行即可。", "",
        "## 章节对应表", "",
        "| 中文章 | 插入内容 | 章首/章末 | 图片 |", "| --- | --- | --- | ---: |",
    ]
    for ch, name, placed, heads, tails, n_img in rows:
        ins = "；".join(d.rsplit(" → ", 1)[0] for d in placed) or "—"
        ht = "；".join(heads + tails) or "—"
        out.append(f"| [{name}]({name}/{name}.md) | {ins} | {ht} | {n_img} |")
    out += [
        "", "## Watson 中译本各章去向", "",
        "| Watson 章 | 去向 |", "| --- | --- |",
    ]
    for ch in range(1, 23):
        if ch in W_SPLITS:
            dest = "；".join(f"{'章首' if h is None else h}→{t}" for h, t in W_SPLITS[ch])
        else:
            dest = f"整章→{W_WHOLE[ch]}"
        out.append(f"| 第{ch}章 {w_titles[ch]} | {dest}；小结/习题→第{W_HOME[ch]}章末 |")
    out += [
        "", "## 已知问题", "",
        "- 文本来自 MinerU 自动解析，原有识别错误未改。《现代分子生物学》第 2 章正文中混有一行页眉“2.1 染色体 / 仅供个人科学教研”，按原样保留。",
        "- Watson 中译本的目录只到第 19 章，第 18–22 章的切分点按正文标题人工指定。",
        "- Lehninger §26.3（RNA 指导的 RNA/DNA 合成：逆转录酶、端粒酶、RNA 复制酶）在《现代分子生物学》中没有专门一节，放在第 9 章 9.2（HIV）末尾；§25.3（重组）放在 2.6（转座）末尾；Watson 第 3 章（化学键）放在 2.2（DNA 结构）末尾，第 6 章（蛋白质结构）放在 4.4 末尾，第 17 章（生命起源）放在 3.12 末尾，第 22 章（系统生物学）放在 8.5 末尾。",
    ]
    if missing:
        out += ["", f"- 有 {len(missing)} 个图片在源目录中不存在：", *[f"  - {m}" for m in missing]]
    out += ["", "重新生成：`python3 scripts/build_molbio_cards.py`", ""]
    (OUT / "README.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
