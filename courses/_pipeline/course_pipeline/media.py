from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path
import cv2
import numpy as np
from .common import run, write_json, digest


def probe(video):
    p = json.loads(run(["ffprobe", "-v", "error", "-show_format", "-show_streams", "-of", "json", video]))
    videos = [x for x in p["streams"] if x["codec_type"] == "video"]
    audios = [x for x in p["streams"] if x["codec_type"] == "audio"]
    if not videos or not audios:
        raise ValueError("Source must contain both video and audio")
    return {"duration_seconds": float(p["format"]["duration"]), "video": videos[0],
            "audio": audios[0], "all_streams": p["streams"], "format": p["format"]}


def extract_audio(video, dest, log):
    run(["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-y", "-i", video,
         "-map", "0:a:0", "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", dest], log=log)


def verify_decode(video, log):
    run(["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-xerror", "-i", video,
         "-map", "0:v:0", "-map", "0:a:0", "-f", "null", "-"], log=log)


def audio_windows(duration, core_seconds=30.0, overlap_seconds=2.0):
    if duration <= 0 or core_seconds <= 0 or overlap_seconds < 0:
        raise ValueError("Invalid audio window configuration")
    windows = []
    start = 0.0
    while start < duration - 1e-6:
        end = min(duration, start + core_seconds)
        windows.append({"id": len(windows), "start": max(0.0, start - overlap_seconds),
                        "end": min(duration, end + overlap_seconds), "core_start": start, "core_end": end})
        start = end
    return windows


def silence_intervals(audio, duration):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostdin", "-i", str(audio), "-af",
                        "silencedetect=noise=-35dB:d=0.5", "-f", "null", "-"],
                       capture_output=True, text=True, check=True, timeout=3600)
    intervals = []
    start = None
    for line in p.stderr.splitlines():
        m = re.search(r"silence_start: ([0-9.]+)", line)
        if m:
            start = float(m[1])
        m = re.search(r"silence_end: ([0-9.]+)", line)
        if m:
            intervals.append([max(0, start or 0), min(duration, float(m[1]))])
            start = None
    if start is not None:
        intervals.append([start, duration])
    return intervals


def difference(a, b):
    diff = cv2.absdiff(a, b)
    mask = diff > 18
    # Local tiles detect small additions to handwriting or slide text.
    tiles = [float(x.mean()) for row in np.array_split(mask, 12, axis=0)
             for x in np.array_split(row, 16, axis=1)]
    return float(mask.mean()), max(tiles), float(diff.mean())


def choose_events(samples, fps, *, global_threshold=0.003, tile_threshold=0.02,
                  settle_seconds=0.28, motion_interval=1.0, maximum_hold=60.0,
                  timestamps=None, ignore_regions=()):
    """Consume every decoded low-resolution frame. Intervals are safeguards only.

    Detect accumulated changes relative to the last saved state and settle after
    animation. During continuous motion capture additional states every second.
    """
    events = []
    reference = previous = last_image = None
    last_time = 0.0
    stable_since = 0.0
    pending = False
    last_n = 0
    for n, gray in enumerate(samples):
        t = timestamps[n] if timestamps is not None else n / fps
        last_n = n
        gray = gray.copy()
        for x1, y1, x2, y2 in ignore_regions:
            h, w = gray.shape
            gray[round(y1*h):round(y2*h), round(x1*w):round(x2*w)] = 0
        if reference is None:
            reference = previous = gray.copy()
            last_image = gray.copy()
            events.append({"frame_number": n, "time": t, "reason": "first", "global_change": 1.0})
            continue
        global_change, local_change, _ = difference(reference, gray)
        step_change, step_local, _ = difference(previous, gray)
        changed = global_change >= global_threshold or local_change >= tile_threshold
        if step_change > 0.0007 or step_local > 0.01:
            stable_since = t
        pending = pending or changed
        settled = pending and t - stable_since >= settle_seconds
        motion_due = changed and t - last_time >= motion_interval
        heartbeat = t - last_time >= maximum_hold
        if (settled or motion_due or heartbeat) and t - last_time >= 0.16:
            events.append({"frame_number": n, "time": t,
                           "reason": "settled_change" if settled else "motion_change" if motion_due else "audit_hold",
                           "global_change": global_change, "local_change": local_change})
            reference = gray.copy()
            last_image = gray.copy()
            last_time = t
            pending = not settled and not heartbeat
        previous = gray
    end_time = timestamps[last_n] if timestamps is not None and previous is not None else last_n / fps
    if previous is not None and end_time - last_time > 0.1:
        events.append({"frame_number": last_n, "time": end_time, "reason": "last"})
    return events


def extract_frames(video, output, metadata, ignore_regions=()):
    output = Path(output)
    frames_dir = output / "frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    # Decode all frames at a fixed ANALYSIS size; preserve original resolution in output.
    rate = metadata["video"].get("avg_frame_rate", "0/1")
    n, d = map(float, rate.split("/"))
    fps = n / d if d else 0
    if fps <= 0:
        raise ValueError("Unknown video frame rate")
    # ffprobe supplies real timestamps for VFR sources, instead of assuming n / fps.
    pts_text = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_frames",
                    "-show_entries", "frame=best_effort_timestamp_time", "-of", "csv=p=0", video])
    pts = []
    for line in pts_text.splitlines():
        try:
            pts.append(float(line.split(",")[0]))
        except ValueError:
            continue
    cmd = ["ffmpeg", "-hide_banner", "-nostdin", "-v", "error", "-i", str(video),
           "-map", "0:v:0", "-vf", "scale=384:216,format=gray", "-vsync", "0", "-f", "rawvideo", "-"]
    errpath = output / "frame_decode.log"
    with errpath.open("wb") as err:
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=err)
        def samples():
            while True:
                data = proc.stdout.read(384 * 216)
                if not data:
                    break
                if len(data) != 384 * 216:
                    raise RuntimeError("Truncated decoded frame")
                yield np.frombuffer(data, np.uint8).reshape(216, 384)
        try:
            origin = float(metadata['format'].get('start_time', 0))
            times = [max(0.0, t - origin) for t in pts]
            events = choose_events(samples(), fps, timestamps=times, ignore_regions=ignore_regions)
        finally:
            proc.stdout.close()
            rc = proc.wait(timeout=60)
        if rc:
            raise RuntimeError(f"Frame decode failed ({rc})")
    if not pts:
        raise RuntimeError("No source video timestamps")
    video_origin = float(metadata["video"].get("start_time", 0))
    format_origin = float(metadata["format"].get("start_time", 0))
    selected = {x["frame_number"]: x for x in events}
    # A second full-resolution decode is efficient and yields the exact selected frame,
    # avoiding approximate seeking and timestamp/frame mismatch.
    cap = cv2.VideoCapture(str(video))
    frame_num = 0
    while True:
        ok, image = cap.read()
        if not ok:
            break
        if frame_num in selected:
            e = selected[frame_num]
            e["time"] = max(0.0, pts[frame_num] - format_origin)
            name = f"frame_{frame_num:08d}_{round(e['time'] * 1000):010d}.webp"
            # OpenCV uses lossless WebP when quality > 100; original decoded pixels
            # are preserved, reducing repository storage without OCR blur.
            if not cv2.imwrite(str(frames_dir / name), image, [cv2.IMWRITE_WEBP_QUALITY, 101]):
                raise RuntimeError("Cannot save key frame")
            e["path"] = "frames/" + name
            e["sha256"] = digest(frames_dir / name)
            e["width"], e["height"] = image.shape[1], image.shape[0]
        frame_num += 1
    cap.release()
    if any("path" not in e for e in events):
        raise RuntimeError("Some selected key frames were not decoded")
    # A frame represents the interval until the next observed key frame, not an
    # assertion that every pixel was unchanged throughout that interval.
    for i, e in enumerate(events):
        e["end"] = events[i + 1]["time"] if i + 1 < len(events) else metadata["duration_seconds"]
    result = {"frames": events, "decoded_frames": frame_num, "source_timestamp_count": len(pts),
              "image_encoding": "lossless WebP, full source resolution",
              "trigger_ignore_regions": ignore_regions,
              "detector_version":2,"analysis_resolution":[384,216],
              "change_thresholds":{"gray_delta":18,"global_fraction":0.003,"local_fraction":0.02,"grid":[16,12],
                                   "settle_seconds":0.28,"motion_interval_seconds":1.0,"audit_hold_seconds":60.0},
              "video_start_time": video_origin, "format_start_time": format_origin,
              "method": "all-frame global and local tile changes, settling, motion states, audit hold",
              "limitations": ["Small or low-contrast changes below thresholds may be missed",
                              "Continuous action is represented by change-triggered snapshots, not every frame"]}
    write_json(output / "frames.json", result)
    return result
