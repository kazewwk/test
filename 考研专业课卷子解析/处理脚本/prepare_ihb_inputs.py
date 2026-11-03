#!/usr/bin/env python3
"""Prepare only 15 IHB subject PDFs, without OCR/reflow or cropbox masking.
Writes only inputs/IHB_*.pdf and ihb_crops.json beside this script. Existing
outputs are verified, never overwritten. All original sources stay untouched.
"""
from __future__ import annotations
import hashlib
import json
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
KIND = "doc_compilation_subject_extract_pdf"
RENDER_CHECKS = {("IHB_2010_cell", 0), ("IHB_2005_bio", 3), ("IHB_2005_cell", 3)}


def normalized(text):
    # Whitespace only; no punctuation, formula or OCR substitutions.
    return re.sub(r"\s+", "", text)


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def poppler_text(path):
    return subprocess.run(["pdftotext", "-layout", str(path), "-"],
                          check=True, capture_output=True).stdout.decode("utf-8")


def text_lines(page):
    return [{"text": "".join(s["text"] for s in line["spans"]),
             "bbox": list(line["bbox"])}
            for block in page.get_text("dict")["blocks"] if block["type"] == 0
            for line in block["lines"]
            if normalized("".join(s["text"] for s in line["spans"]))]


def anchor_line(page, anchor):
    hits = [line for line in text_lines(page)
            if normalized(line["text"]) == normalized(anchor)]
    if len(hits) != 1:
        raise ValueError(f"Expected one anchor {anchor!r}; found {len(hits)}")
    return hits[0]


def chars_in_region(page, top, bottom):
    chars = []
    for block in page.get_text("rawdict")["blocks"]:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                for char in span["chars"]:
                    if not normalized(char["c"]):
                        continue
                    box = char["bbox"]
                    if box[1] >= top - 0.01 and box[3] <= bottom + 0.01:
                        chars.append((char["c"], tuple(round(x, 2) for x in box)))
                    elif box[3] > top and box[1] < bottom:
                        raise ValueError(f"Crop boundary intersects retained character: {char}")
    return chars


def boundary_plan(paper, source):
    b = paper["subject_boundary"]
    first = anchor_line(source[0], b["canonical_start_lines"][0])
    last = anchor_line(source[-1], b["canonical_end_lines"][-1])
    plans = []
    if b["has_preceding_subject_text"]:
        neighbors = [line for line in text_lines(source[0])
                     if line["bbox"][3] < first["bbox"][1]]
        if not neighbors:
            raise ValueError("Inventory says preceding neighbor but none was found")
        previous = max(neighbors, key=lambda x: x["bbox"][3])
        cut = (previous["bbox"][3] + first["bbox"][1]) / 2
        plans.append({"page_1based": 1, "side": "above_subject_start",
                      "rect": [0, 0, source[0].rect.width, cut],
                      "retained_anchor": first, "neighbor_anchor": previous,
                      "reason": "Remove preceding subject before canonical heading"})
    if b["has_following_subject_text"]:
        neighbors = [line for line in text_lines(source[-1])
                     if line["bbox"][1] > last["bbox"][3]]
        if not neighbors:
            raise ValueError("Inventory says following neighbor but none was found")
        following = min(neighbors, key=lambda x: x["bbox"][1])
        cut = (last["bbox"][3] + following["bbox"][1]) / 2
        plans.append({"page_1based": len(source), "side": "below_subject_end",
                      "rect": [0, cut, source[-1].rect.width, source[-1].rect.height],
                      "retained_anchor": last, "neighbor_anchor": following,
                      "reason": "Remove next subject after complete canonical final question"})
    return plans


def validate_output(paper, source, target, plans, canonical):
    output_text = poppler_text(target)
    if normalized(output_text) != normalized(canonical):
        raise ValueError(f"{paper['id']}: output pdftotext differs from complete canonical TXT")
    b = paper["subject_boundary"]
    checks = {}
    for key in ["canonical_start_lines", "canonical_end_lines"]:
        # Start anchors can legitimately continue onto page 2 (2010/2012).
        found = [normalized(anchor) in normalized(output_text) for anchor in b[key]]
        if not all(found):
            raise ValueError(f"{paper['id']}: missing {key}")
        checks[key] = {"all_present": True, "count": len(found), "anchors": b[key]}
    render_checks = []
    with fitz.open(target) as output:
        if len(output) != len(source):
            raise ValueError("Page count changed")
        retained_count = 0
        for i, (before, after) in enumerate(zip(source, output)):
            if before.rect != after.rect or before.cropbox != after.cropbox or before.mediabox != after.mediabox:
                raise ValueError("Page geometry changed")
            top, bottom = 0.0, before.rect.height
            for plan in plans:
                if plan["page_1based"] == i + 1:
                    if plan["side"] == "above_subject_start":
                        top = plan["rect"][3]
                    else:
                        bottom = plan["rect"][1]
                    removed = after.get_text(clip=fitz.Rect(plan["rect"]))
                    if normalized(removed):
                        raise ValueError("Neighbor text remains extractable in redacted region")
            expected_chars = chars_in_region(before, top, bottom)
            actual_chars = chars_in_region(after, 0, after.rect.height)
            if expected_chars != actual_chars:
                raise ValueError(f"{paper['id']} page {i+1}: retained text/coordinates changed")
            retained_count += len(expected_chars)
            if (paper["id"], i) in RENDER_CHECKS:
                clip = fitz.Rect(0, top + (1 if top else 0), before.rect.width,
                                 bottom - (1 if bottom < before.rect.height else 0))
                a = before.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), clip=clip, alpha=False)
                z = after.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), clip=clip, alpha=False)
                if (a.width, a.height, a.samples) != (z.width, z.height, z.samples):
                    raise ValueError(f"{paper['id']} page {i+1}: retained rendering changed")
                render_checks.append({"page_1based": i+1, "scale": 1.5,
                                      "retained_clip": list(clip), "pixels_identical": True,
                                      "pixel_sha256": hashlib.sha256(a.samples).hexdigest()})
        checks.update({"normalized_poppler_fulltext_equals_canonical": True,
                       "retained_character_text_and_coordinates_unchanged": True,
                       "retained_nonwhitespace_characters": retained_count,
                       "redacted_regions_have_no_extractable_text": True,
                       "page_count_and_mediabox_cropbox_unchanged": True,
                       "render_spot_checks": render_checks})
    return checks


def main():
    global fitz
    try:
        import pymupdf as fitz
    except ImportError:
        print("Requires PyMuPDF. Install after current MinerU pip operation; no files written.", file=sys.stderr)
        return 2
    if not shutil.which("pdftotext"):
        raise SystemExit("Requires pdftotext (poppler-utils)")
    papers = [p for p in json.loads((ROOT / "inventory.json").read_text())["papers"]
              if p["recommended_input"]["kind"] == KIND]
    if len(papers) != 15:
        raise ValueError(f"Expected exactly 15 IHB papers, got {len(papers)}")
    results = []
    outdir = ROOT / "inputs"
    outdir.mkdir(exist_ok=True)
    for paper in papers:
        if not re.fullmatch(r"IHB_\d{4}_(bio|cell)", paper["id"]):
            raise ValueError("Unexpected output ID")
        item = paper["recommended_input"]["files"][0]
        original = Path(item["path"])
        before_sha = sha256(original)
        if before_sha != item["sha256"]:
            raise ValueError(f"Source SHA mismatch: {original}")
        b = paper["subject_boundary"]
        canonical = Path(b["canonical_subject_text_path"]).read_text()
        source_text = poppler_text(original)
        full, canon = normalized(source_text), normalized(canonical)
        if full.count(canon) != 1:
            raise ValueError("Canonical text must occur exactly once in source PDF")
        start = full.index(canon)
        prefix, suffix = full[:start], full[start + len(canon):]
        if bool(prefix) != b["has_preceding_subject_text"] or bool(suffix) != b["has_following_subject_text"]:
            raise ValueError("Observed neighbor text disagrees with inventory")
        target = outdir / f"{paper['id']}.pdf"
        existed = target.exists()
        with fitz.open(original) as source:
            if len(source) != item["pdf_physical_pages"]:
                raise ValueError("Source page count disagrees with inventory")
            page_range = b["compiled_pdf_pages_1based_inclusive"]
            if page_range[1] - page_range[0] + 1 != len(source):
                raise ValueError("Compiled page range disagrees with source")
            plans = boundary_plan(paper, source)
            if not existed:
                if plans:
                    with fitz.open(original) as work:
                        for plan in plans:
                            page = work[plan["page_1based"] - 1]
                            rect = fitz.Rect(plan["rect"])
                            keep = fitz.Rect(0, rect.y1, page.rect.width, page.rect.height) if rect.y0 == 0 else fitz.Rect(0, 0, page.rect.width, rect.y0)
                            for drawing in page.get_drawings():
                                box = fitz.Rect(drawing["rect"])
                                if box.intersects(rect) and box.intersects(keep):
                                    raise ValueError("Drawing crosses subject boundary; manual review required")
                            page.add_redact_annot(rect, fill=(1, 1, 1), cross_out=False)
                            page.apply_redactions(images=fitz.PDF_REDACT_IMAGE_PIXELS,
                                                  graphics=fitz.PDF_REDACT_LINE_ART_REMOVE_IF_TOUCHED,
                                                  text=fitz.PDF_REDACT_TEXT_REMOVE)
                        work.save(target, garbage=4, deflate=True)
                else:
                    shutil.copyfile(original, target)
            checks = validate_output(paper, source, target, plans, canonical)
            pages = len(source)
        if sha256(original) != before_sha:
            raise ValueError("Original source changed")
        result = {"id": paper["id"], "source_pdf": str(original),
                  "source_sha256": before_sha, "compiled_pdf": b["compiled_pdf_path"],
                  "compiled_pages_1based_inclusive": page_range,
                  "canonical_subject_text_path": b["canonical_subject_text_path"],
                  "output_pdf": str(target), "output_sha256": sha256(target), "pages": pages,
                  "had_neighbor_text": bool(prefix or suffix),
                  "removed_prefix_nonwhitespace_characters": len(prefix),
                  "removed_suffix_nonwhitespace_characters": len(suffix),
                  "redactions": plans, "existing_output_verified_not_overwritten": existed,
                  "verification": checks}
        results.append(result)
        print(f"PASS {paper['id']}: {pages} pages, {len(plans)} redactions, canonical fulltext exact", flush=True)
    report = {"schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
              "root": str(ROOT), "inventory": str(ROOT / "inventory.json"),
              "tool": {"PyMuPDF": fitz.VersionBind, "pdftotext": shutil.which("pdftotext")},
              "method": "Actual white-filled PyMuPDF redactions of boundary text and graphics; no cropbox-only masking, OCR, reflow or academic correction. Four clean inputs are byte-identical copies.",
              "summary": {"papers": len(results), "pages": sum(x["pages"] for x in results),
                          "papers_with_neighbors_removed": sum(x["had_neighbor_text"] for x in results),
                          "redacted_boundary_regions": sum(len(x["redactions"]) for x in results),
                          "fulltext_exact_passed": len(results),
                          "retained_render_spot_checks_passed": sum(len(x["verification"]["render_spot_checks"]) for x in results)},
              "papers": results}
    report_path = ROOT / "ihb_crops.json"
    if report_path.exists():
        json.loads(report_path.read_text())
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report["summary"], ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
