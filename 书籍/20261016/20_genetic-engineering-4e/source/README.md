# 原始 PDF

保存源 PDF 的原始字节。大于 95 MB 的文件按字节拆分，分片没有改写、重采样或丢弃任何页面。

若有 `.part001` 等文件，在本目录运行 `python3 reassemble.py` 即可恢复完整 PDF 并校验 SHA-256。
