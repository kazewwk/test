"""卡片规范（JSONL）的读取、轻量 Markdown→HTML 转换和共享常量。

一行一张卡（UTF-8 JSON）。字段：
  id      稳定唯一标识，用来生成 Anki guid（重复导入时更新而不是新建）。建议 "<学科>-<章>-<序号>"。
  type    qa | term | image | cloze
          qa    问答卡：front 问，back 答。比较卡/步骤卡/数值卡/机制卡都用它，只是 back 的写法不同。
          term  术语卡：front 术语，back 定义；reverse=true 时再生成“定义→术语”反向卡。
          image 图卡：image 必填，front 对图发问，back 回答。
          cloze 填空卡：front 中用 {{c1::…}}；只用于序列/共有序列等必须按位置记的内容，比例受校验器限制。
  deck    牌组，子牌组用 ::，例如 "生化::02 氨基酸、肽和蛋白质"。
  front / back   允许轻量 Markdown：**粗体**、换行、| 表格 |、1. 有序列表、- 无序列表、`代码`、$公式$（转为 MathJax）。
  extra   选填。来源（章节/图号）、助记、易混提醒。只在答案面显示。
  image   选填。图片文件名（相对 --media-dir），会被复制进 .apkg。
  back_image  选填。答案面的图。
  tags    选填。字符串列表；空格会被替换为下划线。
  reverse 选填。仅 term 有效。
"""

from __future__ import annotations

import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path

TYPES = ("qa", "term", "image", "cloze")


@dataclass
class Card:
    id: str
    type: str
    deck: str
    front: str
    back: str = ""
    extra: str = ""
    image: str = ""
    back_image: str = ""
    tags: list[str] = field(default_factory=list)
    reverse: bool = False
    line: int = 0
    source: str = ""


def load_cards(paths: list[Path]) -> list[Card]:
    cards: list[Card] = []
    for path in paths:
        for n, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            raw = raw.strip()
            if not raw or raw.startswith("#"):
                continue
            try:
                obj = json.loads(raw)
            except json.JSONDecodeError as e:
                raise SystemExit(f"{path}:{n}: JSON 解析失败：{e}")
            known = {k: obj.get(k, "") for k in ("id", "type", "deck", "front", "back", "extra", "image", "back_image")}
            cards.append(Card(**known, tags=[str(t).replace(" ", "_") for t in obj.get("tags", [])],
                              reverse=bool(obj.get("reverse", False)), line=n, source=str(path)))
    return cards


# ---------------------------------------------------------------------------
# 轻量 Markdown → HTML。只处理制卡常用的几种写法，避免引入依赖。

_INLINE = [
    (re.compile(r"\*\*(.+?)\*\*"), r"<b>\1</b>"),
    (re.compile(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)"), r"<i>\1</i>"),
    (re.compile(r"`([^`]+)`"), r"<code>\1</code>"),
    (re.compile(r"\^(\w+)"), r"<sup>\1</sup>"),
    (re.compile(r"~(\w+)~"), r"<sub>\1</sub>"),
]


def _inline(text: str) -> str:
    # 公式：$...$ → \(...\)；内部不做 HTML 转义以外的处理
    parts = re.split(r"(\$[^$]+\$)", text)
    out = []
    for p in parts:
        if p.startswith("$") and p.endswith("$") and len(p) > 2:
            out.append("\\(" + html.escape(p[1:-1], quote=False) + "\\)")
            continue
        p = html.escape(p, quote=False)
        for pat, rep in _INLINE:
            p = pat.sub(rep, p)
        out.append(p)
    return "".join(out)


def md_to_html(text: str, keep_cloze: bool = False) -> str:
    """把字段里的轻量 Markdown 转成 Anki 能显示的 HTML。

    keep_cloze=True 时保留 {{c1::…}} 原样（HTML 转义会破坏它）。
    """
    if not text:
        return ""
    if keep_cloze:
        # 先把 cloze 标记换成占位符，转换完再放回
        clozes: list[str] = []

        def stash(m):
            clozes.append(m.group(0))
            return f"\x00{len(clozes) - 1}\x00"

        text = re.sub(r"\{\{c\d+::.*?\}\}", stash, text, flags=re.S)
    lines = text.replace("\r\n", "\n").split("\n")
    out: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[i + 1]):
            rows = []
            header = [c.strip() for c in line.strip().strip("|").split("|")]
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            out.append("<table><tr>" + "".join(f"<th>{_inline(h)}</th>" for h in header) + "</tr>"
                       + "".join("<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>" for r in rows) + "</table>")
            continue
        m_ol = re.match(r"^\s*(\d+)[.)]\s+(.*)$", line)
        m_ul = re.match(r"^\s*[-*•]\s+(.*)$", line)
        if m_ol or m_ul:
            tag = "ol" if m_ol else "ul"
            items = []
            while i < len(lines):
                m1 = re.match(r"^\s*(\d+)[.)]\s+(.*)$", lines[i]) if tag == "ol" else re.match(r"^\s*[-*•]\s+(.*)$", lines[i])
                if not m1:
                    break
                items.append(m1.group(2) if tag == "ol" else m1.group(1))
                i += 1
            out.append(f"<{tag}>" + "".join(f"<li>{_inline(it)}</li>" for it in items) + f"</{tag}>")
            continue
        if line.strip() == "":
            out.append("<br>")
        else:
            out.append(_inline(line) + "<br>")
        i += 1
    result = "".join(out)
    result = re.sub(r"(<br>)+$", "", result)
    result = re.sub(r"(</(?:table|ol|ul)>)<br>", r"\1", result)
    if keep_cloze:
        result = re.sub(r"\x00(\d+)\x00", lambda m: clozes[int(m.group(1))], result)
    return result


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text or "")
