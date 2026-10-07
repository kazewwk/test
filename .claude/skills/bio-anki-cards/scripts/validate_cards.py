#!/usr/bin/env python3
"""校验卡片规范（JSONL），在生成 .apkg 之前把写坏的卡挡下来。

用法：
  python3 validate_cards.py cards.jsonl [more.jsonl ...] [--media-dir DIR] [--max-cloze 0.05]
                            [--target N] [--strict]

检查项（E = 错误，W = 警告）：
  E  字段缺失 / type 非法 / id 重复 / front 为空 / 非 cloze 卡 back 为空 / image 卡缺图或图不存在
  E  cloze 卡没有 {{cN::}} 标记；非 cloze 卡出现 {{c1::}}
  E  cloze 卡占比超过 --max-cloze（默认 5%）——这个技能的使用者不喜欢填空卡
  W  是非题（“……吗？”“是否……”“能否……”）：答对不等于会，改成要求说出内容的问句
  W  问题面过长（>120 字）或答案面过长（>350 字）：一张卡只装一个事实，长了就拆
  W  答案面是“列举 N 个”且 N>7 又没有分组：超过工作记忆容量，拆成子卡或分组卡
  W  同一牌组内问题面近似重复
  W  没有章节标签 / 没有 extra 来源
  W  --target 给定时，总数偏离目标 ±25% 以上

退出码：有 E 为 1，否则 0（--strict 时 W 也算失败）。
"""

from __future__ import annotations

import argparse
import collections
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cardspec import TYPES, Card, load_cards, strip_html  # noqa: E402

YESNO = re.compile(r"(吗[？?]?\s*$|是否|是不是|能否|能不能|会不会|有没有|对不对|可不可以)")
CLOZE = re.compile(r"\{\{c\d+::")
ENUM = re.compile(r"(列举|举出|有哪几|有哪些|包括哪|分为哪|哪几种|几类|几步|几个)")


def norm(s: str) -> str:
    s = strip_html(s).lower()
    return re.sub(r"[\s，。、；：？！,.;:?!()（）\[\]【】\"'“”‘’]+", "", s)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("files", nargs="+", type=Path)
    ap.add_argument("--media-dir", type=Path, default=None, help="图片所在目录（image 卡会检查文件存在）")
    ap.add_argument("--max-cloze", type=float, default=0.05)
    ap.add_argument("--target", type=int, default=None, help="本批卡的目标张数（来自制卡建议）")
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    cards = load_cards(args.files)
    errors: list[str] = []
    warns: list[str] = []
    where = lambda c: f"{Path(c.source).name}:{c.line} [{c.id or '?'}]"

    seen_ids: dict[str, Card] = {}
    fronts: dict[tuple[str, str], Card] = {}
    by_type = collections.Counter()
    by_deck = collections.Counter()
    for c in cards:
        by_type[c.type] += 1
        by_deck[c.deck] += 1
        if not c.id:
            errors.append(f"{where(c)} 缺 id")
        elif c.id in seen_ids:
            errors.append(f"{where(c)} id 重复（首次出现在第 {seen_ids[c.id].line} 行）")
        else:
            seen_ids[c.id] = c
        if c.type not in TYPES:
            errors.append(f"{where(c)} type 必须是 {TYPES} 之一，现在是 {c.type!r}")
            continue
        if not c.deck:
            errors.append(f"{where(c)} 缺 deck")
        if not c.front.strip():
            errors.append(f"{where(c)} front 为空")
            continue
        if c.type == "cloze":
            if not CLOZE.search(c.front):
                errors.append(f"{where(c)} cloze 卡的 front 里没有 {{{{c1::…}}}}")
        else:
            if CLOZE.search(c.front) or CLOZE.search(c.back):
                errors.append(f"{where(c)} 非 cloze 卡不能含 {{{{cN::}}}}，改 type 或改写成问句")
            if not c.back.strip():
                errors.append(f"{where(c)} back 为空")
        if c.type == "image":
            if not c.image:
                errors.append(f"{where(c)} image 卡缺 image 字段")
            elif args.media_dir and not (args.media_dir / c.image).is_file():
                errors.append(f"{where(c)} 图片不存在：{args.media_dir / c.image}")
        elif c.image and args.media_dir and not (args.media_dir / c.image).is_file():
            errors.append(f"{where(c)} 图片不存在：{args.media_dir / c.image}")
        if c.back_image and args.media_dir and not (args.media_dir / c.back_image).is_file():
            errors.append(f"{where(c)} 图片不存在：{args.media_dir / c.back_image}")

        f_plain, b_plain = strip_html(c.front), strip_html(c.back)
        if c.type != "cloze" and YESNO.search(f_plain.strip()):
            warns.append(f"{where(c)} 是非题：{f_plain[:40]!r}，改成“……是什么/为什么/如何区分”")
        if len(f_plain) > 120:
            warns.append(f"{where(c)} 问题面 {len(f_plain)} 字，过长")
        if len(b_plain) > 350:
            warns.append(f"{where(c)} 答案面 {len(b_plain)} 字，过长，考虑拆分")
        if ENUM.search(f_plain):
            items = len(re.findall(r"^\s*(?:\d+[.)]|[-*•])\s", c.back, flags=re.M))
            if items > 7:
                warns.append(f"{where(c)} 列举 {items} 项，超过 7 项请分组或拆卡")
        key = (c.deck, norm(c.front))
        if key in fronts:
            warns.append(f"{where(c)} 问题面与第 {fronts[key].line} 行近似重复")
        else:
            fronts[key] = c
        if not any(re.search(r"第\d+章|ch\d+|chapter", t, re.I) for t in c.tags):
            warns.append(f"{where(c)} 没有章节标签（如 第2章）")
        if not c.extra.strip():
            warns.append(f"{where(c)} 没有 extra（来源/助记）")

    n = len(cards)
    n_cloze = by_type.get("cloze", 0)
    if n and n_cloze / n > args.max_cloze:
        errors.append(f"cloze 卡 {n_cloze}/{n} = {n_cloze / n:.1%}，超过上限 {args.max_cloze:.0%}；把填空改写成问句、步骤卡或图卡")
    if args.target and n and abs(n - args.target) / args.target > 0.25:
        warns.append(f"总数 {n} 偏离目标 {args.target} 超过 25%")

    print(f"卡片 {n} 张；类型：" + "，".join(f"{k} {v}" for k, v in sorted(by_type.items())))
    print("牌组：" + "；".join(f"{k} {v}" for k, v in sorted(by_deck.items())))
    for e in errors:
        print("E", e)
    for w in warns:
        print("W", w)
    print(f"错误 {len(errors)}，警告 {len(warns)}")
    return 1 if errors or (args.strict and warns) else 0


if __name__ == "__main__":
    sys.exit(main())
