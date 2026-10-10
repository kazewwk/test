import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
books = json.loads((root / "manifest.json").read_text(encoding="utf-8"))["books"]
for book in books:
    if len(book["files"]) == 1 and book["files"][0]["path"] == book["original_name"]:
        path = root / book["original_name"]
        with path.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        assert path.stat().st_size == book["size"] and digest == book["sha256"], "PDF 校验失败"
        print("校验通过：", path)
        continue
    destination = root / "restored-pdfs" / book["original_name"]
    if destination.exists():
        with destination.open("rb") as stream:
            digest = hashlib.file_digest(stream, "sha256").hexdigest()
        assert destination.stat().st_size == book["size"] and digest == book["sha256"], "已有文件校验失败，请先移动该文件"
        print("已还原并校验通过：", destination)
        continue
    destination.parent.mkdir(exist_ok=True)
    temp = destination.with_suffix(destination.suffix + ".tmp")
    total_hash = hashlib.sha256()
    try:
        with temp.open("wb") as output:
            for part in book["files"]:
                path = root / part["path"]
                assert path.stat().st_size == part["size"], "分片大小不符：" + str(path)
                part_hash = hashlib.sha256()
                with path.open("rb") as source:
                    while data := source.read(1024 * 1024):
                        output.write(data)
                        part_hash.update(data)
                        total_hash.update(data)
                assert part_hash.hexdigest() == part["sha256"], "分片校验失败：" + str(path)
        assert temp.stat().st_size == book["size"] and total_hash.hexdigest() == book["sha256"], "原始 PDF 校验失败"
        temp.rename(destination)
    except BaseException:
        temp.unlink(missing_ok=True)
        raise
    print("已还原并校验通过：", destination)
