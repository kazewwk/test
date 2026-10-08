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
