# 重建与校验

`mapping.py` 保存人工主题对照；`build.py` 依中文章、节生成整合材料；`validate.py` 独立核对正文、图表、图片和链接。

下载仓库两个来源 Release 的完整解析 ZIP，解压后使用 Python 3.10+ 运行：

```bash
python build.py --chinese '/path/中文解析/细胞生物学_第5版' --english '/path/英文解析/Molecular Biology of the Cell' --output '/path/新输出目录'
python validate.py '/path/新输出目录' '/path/中文解析/细胞生物学_第5版'
```

输出目录必须是新目录，避免覆盖已有材料。主题块记录原始标题序号、字符偏移与 SHA256，方便调整对应关系和检查内容是否改变。

中文来源：[12-cell-biology-5e.zip](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/12-cell-biology-5e.zip)

英文来源：[Molecular-Biology-of-the-Cell-7e-MinerU-Hybrid.zip](https://github.com/kazewwk/test/releases/download/molecular-biology-of-the-cell-7e-2026-10-09/Molecular-Biology-of-the-Cell-7e-MinerU-Hybrid.zip)

<!-- BEGIN NEW_SOURCES -->
## 在原有双教材基础上追加两本已解析书

先使用原 `build.py` 生成双教材基础目录，再运行：

```bash
python supplement.py --output ../ --wang-jinfa /path/to/细胞生物学（王金发） --laboratory /path/to/细胞生物学实验教程_第2版
python validate_supplements.py --output ../ --baseline /path/to/原双教材目录
```

`supplement_mapping.json` 固定每块原文的字符区间、SHA-256、唯一主归属和其他适用节。`supplement.py` 仅替换自有补充标记内的内容，支持重复运行；原中文/英文正文不改写。校验器检查原正文保留、新块一致性、71个实验完整覆盖、配图、公式、整合视图、链接、原始来源哈希和100MB单文件限制。
<!-- END NEW_SOURCES -->
