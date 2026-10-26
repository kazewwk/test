#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from course_pipeline.common import load, write_json, utcnow
from course_pipeline.drive import Drive
from course_pipeline.inventory import summary

p = argparse.ArgumentParser()
p.add_argument("--inventory", type=Path, required=True)
p.add_argument("--rclone-config", required=True)
p.add_argument("--remote", default="bili_drive")
a = p.parse_args()
rows = load(a.inventory)
drive = Drive(a.rclone_config, a.remote)
by_id = {}
for folder in sorted({r["drive_parent_id"] for r in rows}):
    for meta in drive.list_folder(folder):
        by_id[meta["id"]] = meta
for row in rows:
    meta = by_id.get(row["drive_file_id"])
    if not meta:
        row["source_issue"] = "File missing from authenticated parent listing"
        continue
    row["drive_md5"] = meta.get("md5Checksum")
    row["drive_sha256"] = meta.get("sha256Checksum")
    row["drive_size_bytes"] = int(meta.get("size", 0))
    row["drive_video_metadata"] = meta.get("videoMediaMetadata", {})
    if meta.get("videoMediaMetadata", {}).get("durationMillis"):
        row["catalog_duration_seconds"] = row.get("duration_seconds")
        row["duration_seconds"] = int(meta["videoMediaMetadata"]["durationMillis"]) / 1000
        row["duration_source"] = "Google Drive videoMediaMetadata"
    row["metadata_checked_at"] = utcnow()
write_json(a.inventory, rows)
write_json(a.inventory.with_name("inventory_summary.json"), summary(rows))
print(f"Authenticated metadata for {len(by_id)} files; {len(rows)} target videos")
