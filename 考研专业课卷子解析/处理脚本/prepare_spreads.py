#!/usr/bin/env python3
"""Losslessly flatten only five visually reviewed two-up scans for MinerU.
No OCR, raster re-encoding, source edits, blank-page deletion or deduplication.
"""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import pymupdf as fitz

ROOT = Path(__file__).resolve().parent
# Display-coordinate gutters individually reviewed on all eight rendered spreads.
# Never assume 50%: several right-hand pages start before the physical midpoint.
CUTS = {
    "SUDA-2011-857-CELL": [550],
    "SUDA-2010-845-CELL": [632],
    "SOUTH_SYSU_2012_1055957": [512, 512],
    "SOUTH_SYSU_2011_1035710": [536, 536],
    "SOUTH_SYSU_2011_1035711": [532, 512],
}
BLANK_RIGHT = {("SOUTH_SYSU_2012_1055957", 2), ("SOUTH_SYSU_2011_1035710", 2)}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def image_streams(doc, page):
    # Both original compressed bytes and decoded samples, resolution and bpc.
    return sorted({(im[2], im[3], im[4], im[5],
                    hashlib.sha256(doc.xref_stream_raw(im[0])).hexdigest(),
                    hashlib.sha256(doc.xref_stream(im[0])).hexdigest())
                   for im in page.get_images(full=True)})


def gutter_check(page, cut):
    pix = page.get_pixmap(colorspace=fitz.csGRAY, alpha=False)
    samples, width, height = pix.samples, pix.width, pix.height
    rows = [y for y in range(height)
            if any(samples[y * width + x] < 180 for x in range(cut-2, cut+3))]
    ratio = len(rows) / height
    # Thin crossing page-border strokes/noise are allowed; a text column is not.
    if ratio > .035:
        raise ValueError(f"Reviewed gutter unexpectedly has ink: {ratio:.3%}")
    return {"display_cut_x_pt": cut, "render_scale": 1,
            "checked_band_x_pt": [cut-2, cut+2], "dark_threshold": 180,
            "ink_rows": rows, "ink_row_fraction": ratio,
            "visually_confirmed_two_page_scan_and_gutter_clear_of_question_text": True}


def main():
    outdir = ROOT / "parsing_inputs"
    outdir.mkdir(exist_ok=True)
    results = []
    for paper_id, cuts in CUTS.items():
        source_path = ROOT / "inputs" / f"{paper_id}.pdf"
        target = outdir / f"{paper_id}.pdf"
        before_hash = sha256(source_path)
        existed = target.exists()
        mapping, gutters = [], []
        with fitz.open(source_path) as source:
            if len(source) != len(cuts):
                raise ValueError(f"{paper_id}: unexpected source page count")
            # Remove only /Rotate metadata by moving its equivalent transform into
            # page contents, in memory. The displayed scan stays exactly identical.
            original_rotations = [page.rotation for page in source]
            for page in source:
                before = page.get_pixmap(alpha=False)
                page.remove_rotation()
                after = page.get_pixmap(alpha=False)
                if (before.width, before.height, before.samples) != (after.width, after.height, after.samples):
                    raise ValueError("Rotation normalization altered rendered scan")
            output = fitz.open() if not existed else None
            for i, page in enumerate(source):
                cut = cuts[i]
                if page.rect.width <= page.rect.height:
                    raise ValueError("Expected visually reviewed landscape spread")
                gutters.append({"source_page_1based": i+1, **gutter_check(page, cut)})
                clips = [("left", fitz.Rect(0, 0, cut, page.rect.height)),
                         ("right", fitz.Rect(cut, 0, page.rect.width, page.rect.height))]
                for side, clip in clips:
                    if output is not None:
                        destination = output.new_page(width=clip.width, height=clip.height)
                        # keep_proportion=False prevents tiny float-rounded shifts.
                        # Dest size equals clip size, so this is translation only.
                        destination.show_pdf_page(destination.rect, source, i, clip=clip,
                                                  keep_proportion=False)
                    mapping.append({"output_page": len(mapping)+1,
                                    "output_page_1based": len(mapping)+1,
                                    "source_page": i+1, "source_page_1based": i+1,
                                    "side": side, "source_display_clip_pt": list(clip),
                                    "output_size_pt": [clip.width, clip.height],
                                    "source_original_rotation": original_rotations[i],
                                    "blank_half_preserved": side == "right" and (paper_id, i+1) in BLANK_RIGHT})
            if output is not None:
                # No image recompression/deflate operation is requested.
                output.save(target, garbage=4)
                output.close()
            with fitz.open(target) as check:
                if len(check) != 2*len(source):
                    raise ValueError("Output page count incorrect")
                for entry, page in zip(mapping, check):
                    original = source[entry["source_page"]-1]
                    clip = fitz.Rect(entry["source_display_clip_pt"])
                    if page.rotation != 0:
                        raise ValueError("Output page rotation is not flat")
                    if image_streams(source, original) != image_streams(check, page):
                        raise ValueError("Original image bytes or resolution changed")
                    # Clear prior full-spread image interpolation caches.
                    fitz.TOOLS.store_shrink(100)
                    a = original.get_pixmap(clip=clip, alpha=False)
                    fitz.TOOLS.store_shrink(100)
                    b = page.get_pixmap(alpha=False)
                    if (a.width, a.height, a.samples) != (b.width, b.height, b.samples):
                        raise ValueError(f"{paper_id}: rendered half differs on output page {entry['output_page']}")
                    entry["verification"] = {"rendered_pixels_equal_to_source_clip_at_72dpi": True,
                                              "render_sha256": hashlib.sha256(a.samples).hexdigest(),
                                              "original_compressed_image_bytes_and_decoded_samples_unchanged": True,
                                              "image_resolution_unchanged": True}
            if sha256(source_path) != before_hash:
                raise ValueError("Source PDF changed")
        results.append({"id": paper_id, "source_pdf": str(source_path),
                        "source_sha256": before_hash, "source_pages": len(cuts),
                        "output_pdf": str(target), "output_sha256": sha256(target),
                        "output_pages": len(mapping), "page_mapping": mapping,
                        "gutter_checks": gutters,
                        "existing_output_verified_not_overwritten": existed,
                        "verification": {"source_unchanged": True, "all_halves_preserved_left_then_right": True,
                                         "no_resampling_or_image_reencoding": True}})
        print(f"PASS {paper_id}: {len(cuts)} spreads -> {len(mapping)} pages; image streams and rendered clips exact", flush=True)
    report = {"schema_version": 1, "created_at": datetime.now(timezone.utc).isoformat(),
              "method": "Individually reviewed blank gutter; lossless rotation normalization in memory; new PDF pages using show_pdf_page clip at original physical scale, left then right. Original image compressed streams and samples retained. Both blank right halves preserved.",
              "PyMuPDF": fitz.VersionBind,
              "summary": {"papers": len(results), "source_spreads": sum(p["source_pages"] for p in results),
                          "output_pages": sum(p["output_pages"] for p in results),
                          "blank_halves_preserved": 2,
                          "all_16_rendered_halves_exact": True,
                          "all_original_image_streams_unchanged": True}, "papers": results}
    report_path = ROOT / "split_pages.json"
    if report_path.exists():
        json.loads(report_path.read_text())
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report["summary"], ensure_ascii=False))


if __name__ == "__main__":
    main()
