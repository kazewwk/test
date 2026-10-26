from __future__ import annotations

import re
from pathlib import Path
from .common import load, write_json, utcnow

SERIES = {"Book1": "新概念英语第一册", "Book2_L01-48": "新概念英语第二册_L01-L48",
          "Book2_L49-96": "新概念英语第二册_L49-L96"}


def safe_name(value):
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value).strip(" .")
    return value[:90] or "untitled"


def lesson_directory(title, part):
    # A Bilibili part is not a textbook lesson; retain both identifiers.
    m = re.match(r"^(?:[Ll](?:esson)?\s*)?(\d{1,3})(?:\s*[-—～~]\s*(\d{1,3}))?(?=\D|$)", title)
    if m and not re.match(r"^\d+[-～~]\d+总结", title):
        label = f"Lesson_{int(m[1]):03d}"
        if m[2]:
            label += f"-{int(m[2]):03d}"
    else:
        label = "Intro" if re.search("开篇|准备|导学|总结|前言", title) else "Video"
    return f"{label}_P{part:03d}_{safe_name(title)}"


def build_inventory(connector_inventory, rclone_inventory, transfer_manifest, biology_inventory=None):
    remote = {x["ID"]: x for x in rclone_inventory if x.get("ID")}
    metadata = {(x["group"], x["page"]): x for x in transfer_manifest["episodes"]}
    rows = []
    for folder in connector_inventory:
        group = folder["series"]
        for f in folder["files"]:
            if not f.get("mime_type", "").startswith("video/"):
                continue
            m = re.search(r"_P(\d+)\.", f["title"])
            if not m:
                raise ValueError(f"Unmapped part: {f['title']}")
            part = int(m[1])
            meta = metadata.get((group, part))
            if not meta:
                raise ValueError(f"Missing original lesson metadata: {group}/{part}")
            r = remote.get(f["id"], {})
            rows.append(dict(drive_file_id=f["id"], drive_parent_id=folder["folder_id"],
                             series=SERIES.get(group, group), source_group=group,
                             filename=f["title"], title=meta["title"], part=part,
                             duration_seconds=meta["duration"], duration_source="original transfer manifest",
                             size_bytes=int(f["size"]), drive_md5=r.get("Hashes", {}).get("md5"),
                             video_sha256=None, source_bvid=meta["bvid"], source_cid=meta.get("cid"),
                             directory=lesson_directory(meta["title"], part), status="pending",
                             priority=0))
    for folder in biology_inventory or []:
        for f in folder.get("files", []):
            if not f.get("mime_type", "").startswith("video/"):
                continue
            m = re.match(r"(\d+)[_ .-]", f["title"])
            part = int(m[1]) if m else 0
            title = Path(f["title"]).stem
            rows.append(dict(drive_file_id=f["id"], drive_parent_id=folder["folder_id"],
                             series=folder["series"], source_group=folder["series"], filename=f["title"],
                             title=title, part=part, duration_seconds=None, duration_source="not probed",
                             size_bytes=int(f["size"]), drive_md5=None, video_sha256=None,
                             directory=f"Video_{part:03d}_{safe_name(title)}_{f['id'][-6:]}",
                             status="pending", priority=1))
    if len({x["drive_file_id"] for x in rows}) != len(rows):
        raise ValueError("Duplicate Drive IDs in source scope")
    if len({(x["series"], x["directory"]) for x in rows}) != len(rows):
        raise ValueError("Output path collision")
    return sorted(rows, key=lambda x: (x["priority"], x["series"], x["part"], x["drive_file_id"]))


def summary(rows):
    result = {}
    for r in rows:
        s = result.setdefault(r["series"], dict(videos=0, bytes=0, known_duration_seconds=0,
                                             unknown_duration_count=0, completed=0))
        s["videos"] += 1
        s["bytes"] += r["size_bytes"]
        s["known_duration_seconds"] += r.get("duration_seconds") or 0
        s["unknown_duration_count"] += r.get("duration_seconds") is None
        s["completed"] += r.get("status") in ("complete", "complete_with_review_flags", "published")
    return {"observed_at": utcnow(), "series": result, "total_videos": len(rows)}
