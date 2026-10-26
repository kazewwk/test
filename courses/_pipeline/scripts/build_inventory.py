#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from course_pipeline.common import load, write_json
from course_pipeline.inventory import build_inventory, summary

p = argparse.ArgumentParser()
p.add_argument("--evidence", type=Path, required=True)
p.add_argument("--output", type=Path, required=True)
p.add_argument("--include-biology", action="store_true", help="Only when explicitly in scope")
a = p.parse_args()
rows = build_inventory(load(a.evidence / "drive_connector_inventory.json"),
                       load(a.evidence / "rclone_new_concept_inventory.json"),
                       load(a.evidence / "source_metadata/transfer-manifest.json"),
                       load(a.evidence / "biology_inventory.json") if a.include_biology else [])
write_json(a.output, rows)
write_json(a.output.with_name("inventory_summary.json"), summary(rows))
print(f"Wrote {len(rows)} videos to {a.output}")
