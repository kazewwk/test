#!/usr/bin/env python3
"""生成 `生化制卡/`：以朱圣庚《生物化学》上下册为主干，把 Lehninger
Principles of Biochemistry（英文）的各小节插入对应的中文章节。

- 每个中文章节一个子文件夹，内含合并后的 Markdown 和该章引用的全部图片。
- 英文小节插在对应中文一级小节（“一、二、三……”）的末尾。
- 英文各章的章首导言插在中文章首，关键术语、习题和习题简答放在中文章末。
- 英文前置内容、术语表和索引不对应具体章节，放在附录文件夹。

用法：python3 scripts/build_biochem_cards.py
"""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOKS = ROOT / "书籍"
EN_BOOK = BOOKS / "02_生物化学原理"
ZH_BOOKS = [BOOKS / "10_生物化学_上册_朱圣庚_徐长法", BOOKS / "11_生物化学_下册_朱圣庚_徐长法"]
OUT = ROOT / "生化制卡"

EN_SOURCE = "Lehninger Principles of Biochemistry（书籍/02_生物化学原理）"

# 英文各章在 merged/full.md 中的起始行（1 起）。原书 chapters/ 的分章与真实章号错位，
# 所以按全文重新切分。篇首页（Part I/II/III）并入其后第一章。
EN_CHAPTER_START = {
    1: 1946, 2: 3084, 3: 4216, 4: 5252, 5: 6277, 6: 7197, 7: 8802, 8: 9641,
    9: 10483, 10: 11299, 11: 11918, 12: 12831, 13: 14078, 14: 15720, 15: 17047,
    16: 17503, 17: 18275, 18: 18908, 19: 19601, 20: 20641, 21: 21741, 22: 22779,
    23: 23832, 24: 24761, 25: 25475, 26: 26405, 27: 27359, 28: 28397,
}
EN_SOLUTIONS_START = 29360
EN_GLOSSARY_START = 31509
EN_INDEX_START = 33926

EN_CHAPTER_TITLE = {
    1: "The Foundations of Biochemistry", 2: "Water, the Solvent of Life",
    3: "Amino Acids, Peptides, and Proteins", 4: "The Three-Dimensional Structure of Proteins",
    5: "Protein Function", 6: "Enzymes", 7: "Carbohydrates and Glycobiology",
    8: "Nucleotides and Nucleic Acids", 9: "DNA-Based Information Technologies",
    10: "Lipids", 11: "Biological Membranes and Transport", 12: "Biochemical Signaling",
    13: "Introduction to Metabolism",
    14: "Glycolysis, Gluconeogenesis, and the Pentose Phosphate Pathway",
    15: "The Metabolism of Glycogen in Animals", 16: "The Citric Acid Cycle",
    17: "Fatty Acid Catabolism", 18: "Amino Acid Oxidation and the Production of Urea",
    19: "Oxidative Phosphorylation", 20: "Photosynthesis and Carbohydrate Synthesis in Plants",
    21: "Lipid Biosynthesis", 22: "Biosynthesis of Amino Acids, Nucleotides, and Related Molecules",
    23: "Hormonal Regulation and Integration of Mammalian Metabolism",
    24: "Genes and Chromosomes", 25: "DNA Metabolism", 26: "RNA Metabolism",
    27: "Protein Metabolism", 28: "Regulation of Gene Expression",
}

# 英文小节 -> (中文章号, 中文一级小节序号)。插入位置为该中文小节末尾。
SECTION_MAP = {
    "1.1": (1, "七"), "1.2": (1, "三"), "1.3": (1, "一"), "1.4": (1, "二"), "1.5": (1, "八"),
    "2.1": (1, "五"), "2.2": (1, "六"), "2.3": (1, "六"),
    "3.1": (2, "三"), "3.2": (2, "八"), "3.3": (5, "三"), "3.4": (2, "十二"),
    "4.1": (3, "一"), "4.2": (3, "三"), "4.3": (3, "六"), "4.4": (3, "九"), "4.5": (3, "二"),
    "5.1": (4, "四"), "5.2": (4, "五"), "5.3": (4, "六"),
    "6.1": (6, "二"), "6.2": (8, "三"), "6.3": (7, "三"), "6.4": (8, "四"), "6.5": (8, "六"),
    "7.1": (9, "四"), "7.2": (9, "五"), "7.3": (9, "六"), "7.4": (9, "七"), "7.5": (9, "八"),
    "8.1": (11, "三"), "8.2": (11, "五"), "8.3": (12, "六"), "8.4": (13, "三"),
    "9.1": (35, "二"), "9.2": (36, "二"), "9.3": (36, "一"),
    "10.1": (10, "一"), "10.2": (10, "二"), "10.3": (10, "三"), "10.4": (10, "六"),
    "11.1": (10, "五"), "11.2": (10, "五"), "11.3": (10, "五"),
    "12.1": (14, "五"), "12.2": (14, "六"), "12.3": (14, "六"), "12.4": (14, "七"),
    "12.5": (14, "七"), "12.6": (14, "九"), "12.7": (14, "十一"), "12.8": (14, "十一"),
    "12.9": (14, "十一"),
    "13.1": (16, "一"), "13.2": (15, "二"), "13.3": (16, "三"), "13.4": (19, "一"),
    "13.5": (28, "二"),
    "14.1": (17, "五"), "14.2": (17, "九"), "14.3": (17, "七"), "14.4": (21, "一"),
    "14.5": (17, "八"), "14.6": (20, "二"),
    "15.1": (22, "一"), "15.2": (22, "三"), "15.3": (22, "四"),
    "16.1": (18, "一"), "16.2": (18, "二"), "16.3": (18, "五"), "16.4": (18, "四"),
    "17.1": (24, "一"), "17.2": (24, "三"), "17.3": (24, "四"),
    "18.1": (25, "二"), "18.2": (25, "三"), "18.3": (25, "四"),
    "19.1": (19, "二"), "19.2": (19, "三"), "19.3": (19, "三"), "19.4": (19, "三"),
    "19.5": (19, "三"),
    "20.1": (23, "二"), "20.2": (23, "三"), "20.3": (23, "四"), "20.4": (23, "五"),
    "20.5": (23, "六"), "20.6": (23, "六"),
    "21.1": (24, "六"), "21.2": (24, "六"), "21.3": (24, "六"), "21.4": (24, "六"),
    "22.1": (26, "二"), "22.2": (26, "四"), "22.3": (26, "五"), "22.4": (27, "二"),
    "23.1": (14, "一"), "23.2": (28, "四"), "23.3": (28, "四"), "23.4": (28, "五"),
    "23.5": (28, "五"),
    "24.1": (29, "二"), "24.2": (29, "三"), "24.3": (29, "三"),
    "25.1": (30, "一"), "25.2": (30, "二"), "25.3": (31, "三"),
    "26.1": (32, "一"), "26.2": (32, "二"), "26.3": (32, "三"), "26.4": (6, "七"),
    "27.1": (33, "一"), "27.2": (33, "三"), "27.3": (33, "五"),
    "28.1": (34, "一"), "28.2": (34, "二"), "28.3": (34, "三"),
}

# 英文各章的章首导言、关键术语/习题/习题简答放到哪个中文章。
CHAPTER_HOME = {
    1: 1, 2: 1, 3: 2, 4: 3, 5: 4, 6: 6, 7: 9, 8: 11, 9: 35, 10: 10, 11: 10, 12: 14,
    13: 15, 14: 17, 15: 22, 16: 18, 17: 24, 18: 25, 19: 19, 20: 23, 21: 24, 22: 26,
    23: 28, 24: 29, 25: 30, 26: 32, 27: 33, 28: 34,
}

NUMERALS = ["一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
            "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十"]

IMAGE_RE = re.compile(r"\]\((?:\.\./merged/)?images/([^)\s]+)\)")
ZH_L1_RE = re.compile(r"^#{1,6}\s*([一二三四五六七八九十]+)、")
ZH_END_RE = re.compile(r"^#{1,6}\s*(提要|习题)\s*$")
EN_KEYTERMS_RE = re.compile(r"^#{1,6}\s*KEY TERMS\s*$")


def read_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def demote_headings(lines: list[str], level: int) -> list[str]:
    """英文段落里的标题统一降到 `level` 级，并加 [EN] 标记，避免与中文标题混淆。"""
    out = []
    in_math = False
    for line in lines:
        if line.strip() == "$$":
            in_math = not in_math
        m = None if in_math else re.match(r"^#{1,6}\s+(.*)$", line)
        out.append(f"{'#' * level} [EN] {m.group(1)}" if m else line)
    return out


def parse_english():
    lines = read_lines(EN_BOOK / "merged" / "full.md")
    starts = sorted(EN_CHAPTER_START.items())
    chapters = {}
    for i, (num, start) in enumerate(starts):
        end = starts[i + 1][1] if i + 1 < len(starts) else EN_SOLUTIONS_START
        body = lines[start - 1:end - 1]
        sec_starts = []
        m_idx = 1
        for j, line in enumerate(body):
            pat = re.compile(rf"^#{{1,6}}\s*{num}\.{m_idx}\s+\S")
            # 目录行以页码结尾，正文标题不会
            if pat.match(line) and not re.search(r"\s\d{1,4}\s*$", line):
                sec_starts.append((f"{num}.{m_idx}", j))
                m_idx += 1
        expected = sorted((k for k in SECTION_MAP if k.split(".")[0] == str(num)),
                          key=lambda k: int(k.split(".")[1]))
        found = [k for k, _ in sec_starts]
        if found != expected:
            raise SystemExit(f"英文第{num}章小节不符：找到 {found}，应为 {expected}")
        kt = next(j for j, line in enumerate(body) if j > sec_starts[-1][1] and EN_KEYTERMS_RE.match(line))
        sections = {}
        for k, (key, j) in enumerate(sec_starts):
            stop = sec_starts[k + 1][1] if k + 1 < len(sec_starts) else kt
            sections[key] = body[j:stop]
        chapters[num] = {
            "intro": body[:sec_starts[0][1]],
            "sections": sections,
            "end": body[kt:],
        }
    # 习题简答按章拆分（第4章标题在原文中不是 Markdown 标题）
    sol = lines[EN_SOLUTIONS_START - 1:EN_GLOSSARY_START - 1]
    sol_starts = []
    for j, line in enumerate(sol):
        m = re.match(r"^(?:#{1,6}\s*)?Chapter (\d+)\s*$", line)
        if m:
            sol_starts.append((int(m.group(1)), j))
    if [n for n, _ in sol_starts] != list(range(1, 29)):
        raise SystemExit(f"习题简答章号不连续：{[n for n, _ in sol_starts]}")
    for k, (num, j) in enumerate(sol_starts):
        stop = sol_starts[k + 1][1] if k + 1 < len(sol_starts) else len(sol)
        chapters[num]["solutions"] = sol[j + 1:stop]
    appendix = {
        "英文教材_前置内容": lines[:EN_CHAPTER_START[1] - 1],
        "英文教材_习题简答_说明": sol[:sol_starts[0][1]],
        "英文教材_术语表": lines[EN_GLOSSARY_START - 1:EN_INDEX_START - 1],
        "英文教材_索引": lines[EN_INDEX_START - 1:],
    }
    return chapters, appendix


def zh_chapters():
    for book in ZH_BOOKS:
        for path in sorted((book / "chapters").glob("*.md")):
            m = re.match(r"^\d{3}_第(\d+)章_(.+)\.md$", path.name)
            if m:
                yield int(m.group(1)), m.group(2), path, book


def zh_section_bounds(lines: list[str], num: int):
    """返回 {一级序号: (起始行, 结束行)}，以及中文章首导言结束行。"""
    end_marker = next((i for i, line in enumerate(lines) if ZH_END_RE.match(line)), len(lines))
    heads = []
    want = 0
    for i, line in enumerate(lines[:end_marker]):
        m = ZH_L1_RE.match(line)
        if m and want < len(NUMERALS) and m.group(1) == NUMERALS[want]:
            heads.append((m.group(1), i))
            want += 1
    if not heads:
        raise SystemExit(f"中文第{num}章没有找到一级小节")
    bounds = {}
    for k, (n, i) in enumerate(heads):
        bounds[n] = (i, heads[k + 1][1] if k + 1 < len(heads) else end_marker)
    return bounds, heads[0][1]


def en_block(key: str, en_num: int, body: list[str], zh_anchor: str) -> list[str]:
    title = re.sub(r"^#{1,6}\s*", "", body[0]).strip()
    return [
        "",
        f"<!-- EN-BEGIN {key} -->",
        "",
        f"### 【英文对应 {key}】{re.sub(rf'^{re.escape(key)}\s*', '', title)}",
        "",
        f"> 来源：{EN_SOURCE} 第{en_num}章 {EN_CHAPTER_TITLE[en_num]}，§{key}。对应本章“{zh_anchor}”。",
        "",
        *demote_headings(body[1:], 4),
        "",
        f"<!-- EN-END {key} -->",
        "",
    ]


def copy_images(text: str, sources: list[Path], dest: Path, missing: list):
    names = sorted(set(IMAGE_RE.findall(text)))
    if names:
        dest.mkdir(parents=True, exist_ok=True)
    for name in names:
        src = next((s / name for s in sources if (s / name).is_file()), None)
        if src is None:
            missing.append(f"{dest.parent.name}: {name}")
            continue
        shutil.copy2(src, dest / name)
    return len(names)


def rewrite_images(text: str) -> str:
    return IMAGE_RE.sub(lambda m: f"](images/{m.group(1)})", text)


def main():
    en, appendix = parse_english()
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    en_images = EN_BOOK / "merged" / "images"
    missing: list[str] = []
    index_rows = []
    mapping = {"中文主干": [b.name for b in ZH_BOOKS], "英文来源": EN_BOOK.name, "章节": []}

    # 按中文章归集插入内容
    inserts: dict[int, dict[str, list[str]]] = {}
    for key, (zh_num, sec) in SECTION_MAP.items():
        inserts.setdefault(zh_num, {}).setdefault(sec, []).append(key)
    homes: dict[int, list[int]] = {}
    for en_num, zh_num in CHAPTER_HOME.items():
        homes.setdefault(zh_num, []).append(en_num)

    # 中文前置内容
    front_dir = OUT / "00_中文教材前置内容"
    front_dir.mkdir()
    for book, label in zip(ZH_BOOKS, ["上册", "下册"]):
        text = (book / "chapters" / "000_front_matter.md").read_text(encoding="utf-8")
        copy_images(text, [book / "merged" / "images"], front_dir / "images", missing)
        (front_dir / f"{label}_前置内容.md").write_text(rewrite_images(text), encoding="utf-8")

    seen_zh = []
    for num, title, path, book in zh_chapters():
        seen_zh.append(num)
        lines = read_lines(path)
        bounds, intro_end = zh_section_bounds(lines, num)
        heading_of = {n: re.sub(r"^#{1,6}\s*", "", lines[i]).strip() for n, (i, _) in bounds.items()}
        # 插入点：行号 -> 待插入的行（倒序插入，避免行号偏移）
        at: dict[int, list[str]] = {}
        placed = []
        for sec, keys in inserts.get(num, {}).items():
            if sec not in bounds:
                raise SystemExit(f"中文第{num}章没有“{sec}、”小节，无法插入 {keys}")
            stop = bounds[sec][1]
            for key in sorted(keys, key=lambda k: tuple(map(int, k.split(".")))):
                en_num = int(key.split(".")[0])
                at.setdefault(stop, []).extend(en_block(key, en_num, en[en_num]["sections"][key], heading_of[sec]))
                placed.append((key, en_num, heading_of[sec]))
        for en_num in homes.get(num, []):
            intro = en[en_num]["intro"]
            at.setdefault(intro_end, []).extend([
                "", f"<!-- EN-BEGIN 第{en_num}章导言 -->", "",
                f"### 【英文对应 第{en_num}章导言】{EN_CHAPTER_TITLE[en_num]}", "",
                f"> 来源：{EN_SOURCE} 第{en_num}章章首（含章节目录与学习要点）。", "",
                *demote_headings(intro, 4), "", f"<!-- EN-END 第{en_num}章导言 -->", "",
            ])
            at.setdefault(len(lines), []).extend([
                "", f"<!-- EN-BEGIN 第{en_num}章章末 -->", "",
                f"## 【英文对应 第{en_num}章章末】{EN_CHAPTER_TITLE[en_num]}：关键术语、习题与简答", "",
                f"> 来源：{EN_SOURCE} 第{en_num}章章末，以及书末 Abbreviated Solutions to Problems 第{en_num}章。", "",
                *demote_headings(en[en_num]["end"], 3), "",
                f"### [EN] Abbreviated Solutions — Chapter {en_num}", "",
                *demote_headings(en[en_num]["solutions"], 4), "",
                f"<!-- EN-END 第{en_num}章章末 -->", "",
            ])
        for pos in sorted(at, reverse=True):
            lines[pos:pos] = at[pos]

        placed.sort(key=lambda p: tuple(map(int, p[0].split("."))))
        summary = ["", "> **本章英文对应内容**（Lehninger，插在所列中文小节末尾）", ">"]
        for en_num in homes.get(num, []):
            summary.append(f"> - 第{en_num}章 {EN_CHAPTER_TITLE[en_num]}：章首导言（本章开头）、关键术语/习题/简答（本章末尾）")
        for key, en_num, zh_head in placed:
            summary.append(f"> - §{key}（第{en_num}章）→ {zh_head}")
        if len(summary) == 3:
            summary.append("> - 无")
        lines[1:1] = summary

        name = f"{num:02d}_第{num}章_{title}"
        folder = OUT / name
        folder.mkdir()
        text = "\n".join(lines)
        n_img = copy_images(text, [book / "merged" / "images", en_images], folder / "images", missing)
        (folder / f"{name}.md").write_text(rewrite_images(text), encoding="utf-8")
        index_rows.append((num, name, placed, homes.get(num, []), n_img))
        mapping["章节"].append({
            "中文章": num, "文件夹": name,
            "英文小节": [{"小节": k, "英文章": e, "插入在中文小节末尾": h} for k, e, h in placed],
            "英文整章导言与章末": homes.get(num, []), "图片数": n_img,
        })

    if seen_zh != list(range(1, 37)):
        raise SystemExit(f"中文章号不完整：{seen_zh}")

    app_dir = OUT / "99_英文教材附录_无对应章节"
    app_dir.mkdir()
    for name, body in appendix.items():
        text = "\n".join(body)
        copy_images(text, [en_images], app_dir / "images", missing)
        (app_dir / f"{name}.md").write_text(rewrite_images(text), encoding="utf-8")

    (OUT / "对应关系.json").write_text(json.dumps(mapping, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_readme(index_rows, missing)
    if missing:
        print(f"缺失图片 {len(missing)} 个，见 README")
    print(f"完成：{len(index_rows)} 章，英文小节 {len(SECTION_MAP)} 个")


def write_readme(rows, missing):
    out = [
        "# 生化制卡",
        "",
        "以朱圣庚、徐长法《生物化学》（第4版）上、下册为主干，把 Lehninger *Principles of Biochemistry*（英文）"
        "各小节插入对应的中文章节，便于制作卡片。",
        "",
        "## 目录结构",
        "",
        "- 每个 `NN_第N章_…/` 对应中文教材一章：`NN_第N章_….md` 为合并文本，`images/` 为该章（中英文）引用的全部图片，链接为相对路径 `images/…`。",
        "- `00_中文教材前置内容/`：上、下册的目录、前言等正文前材料。",
        "- `99_英文教材附录_无对应章节/`：英文教材的前置内容、术语表（Glossary）、索引，以及习题简答的说明段。",
        "- `对应关系.json`：机器可读的英中对应表。",
        "",
        "## 合并规则",
        "",
        "1. 中文原文完整保留，顺序不变。",
        "2. 英文以小节（§N.M）为单位，插在对应中文一级小节（“一、二、三……”）的**末尾**，即该中文小节最后一段之后、下一个一级小节之前；最后一个小节则插在“提要/习题”之前。",
        "3. 英文内容用 `<!-- EN-BEGIN … -->` / `<!-- EN-END … -->` 包住，块标题为 `### 【英文对应 §N.M】…`，英文内部标题统一降为 `#### [EN] …`，便于检索或批量剔除。",
        "4. 英文每章的章首导言放在对应中文章开头（第一个一级小节之前）；关键术语、习题、数据分析题和书末习题简答放在中文章末尾。",
        "5. 每章开头有一段“本章英文对应内容”清单。",
        "",
        "对应关系是按小节主题人工判定的，插在主题最接近的中文小节末尾。英文一个小节常覆盖中文几个小节（例如 §3.1 同时讲氨基酸结构、分类和酸碱性质），"
        "这时一般插在所覆盖范围的最后一个中文小节之后。中文教材没有专门小节的英文内容（如 §20.6 淀粉、蔗糖和纤维素的生物合成）放在最相关章节的末尾。如果觉得某处放得不合适，改 `scripts/build_biochem_cards.py` 里的 `SECTION_MAP` 后重新运行即可。",
        "",
        "## 章节对应表",
        "",
        "| 中文章 | 插入的英文内容 | 图片 |",
        "| --- | --- | ---: |",
    ]
    for num, name, placed, homes, n_img in rows:
        parts = [f"第{e}章导言/章末" for e in homes]
        parts += [f"§{k}→{h.split('、')[0]}" for k, _, h in placed]
        out.append(f"| [{name}]({name}/{name}.md) | {'；'.join(parts) or '—'} | {n_img} |")
    out += [
        "",
        "## 已知问题",
        "",
        "- 文本来自 MinerU 自动解析，原有的识别错误（公式、表格、断行、个别标题层级）未做修改。",
        "- 中文第34章原文在“习题”之后夹有一段与生化无关的“四、投资风险分析”，为原解析结果中的内容，按原样保留。",
        "- 英文原书 `chapters/` 目录的分章与真实章号错位，本文件夹按英文全文中的章标题和小节编号重新切分，不受影响。",
    ]
    if missing:
        out += ["", f"- 有 {len(missing)} 个图片在源目录中不存在：", *[f"  - {m}" for m in missing]]
    out += ["", "重新生成：`python3 scripts/build_biochem_cards.py`", ""]
    (OUT / "README.md").write_text("\n".join(out), encoding="utf-8")


if __name__ == "__main__":
    main()
