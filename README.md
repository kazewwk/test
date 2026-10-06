# MinerU 书籍解析包

这里保存从 Seafile「中转站 / 图书库」导出的 13 份原始 ZIP，合计 **5.16 GiB**。原始 ZIP 没有重新压缩或修改。

**[打开全部 ZIP 下载页](https://github.com/kazewwk/test/releases/tag/mineru-books-2026-10-07)**

ZIP 附件保存在本项目的 GitHub Releases；仓库中保存书籍目录和 SHA-256 校验文件。多数 ZIP 超过 GitHub 普通文件的 100 MiB 限制，因此没有直接提交到 Git 仓库。

| 序号 | 原始文件名 | 大小 | 下载 |
| --- | --- | ---: | --- |
| 1 | Campbell Biology - MinerU Official VLM OCR - 20260721-120337.zip | 1838.88 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/01-campbell-biology.zip) |
| 2 | principles_biochemistry_MinerU3.4.4_分章解析.zip | 373.99 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/02-principles-biochemistry.zip) |
| 3 | 基因的分子生物学_第七版_MinerU3.4.4_分章解析.zip | 382.33 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/03-molecular-biology-of-the-gene-7e.zip) |
| 4 | 新概念英语1_课堂笔记_课后练习.zip | 18.34 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/04-new-concept-english-1-notes-exercises.zip) |
| 5 | 新概念英语2_课堂笔记.zip | 20.89 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/05-new-concept-english-2-notes.zip) |
| 6 | 新概念英语第一册_MinerU_VLM_按课拆分.zip | 133.43 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/06-new-concept-english-1-lessons.zip) |
| 7 | 植物学全彩版_第三版_MinerU3.4.4_分章解析.zip | 229.62 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/07-botany-3e.zip) |
| 8 | 植物生理学_第五版_MinerU3.4.4_分章解析.zip | 441.05 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/08-plant-physiology-5e.zip) |
| 9 | 现代分子生物学_MinerU3.4.4_分章解析.zip | 254.80 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/09-modern-molecular-biology.zip) |
| 10 | 生物化学_上册_朱圣庚_徐长法_MinerU_分章解析.zip | 312.52 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/10-biochemistry-vol1-zhu-xu.zip) |
| 11 | 生物化学_下册_朱圣庚_徐长法_MinerU_分章解析.zip | 437.95 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/11-biochemistry-vol2-zhu-xu.zip) |
| 12 | 细胞生物学_第5版_MinerU_分章解析.zip | 221.95 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/12-cell-biology-5e.zip) |
| 13 | 遗传学_基因和基因组分析_第八版_MinerU3.4.4_分章解析.zip | 620.45 MiB | [ZIP](https://github.com/kazewwk/test/releases/download/mineru-books-2026-10-07/13-genetics-genes-genomes-8e.zip) |

[机器可读清单](books/manifest.json)记录原始文件名、下载文件名、精确字节数和 SHA-256。[SHA256SUMS.txt](books/SHA256SUMS.txt)用于下载后的完整性检查。

下载 ZIP 时 GitHub 使用表中链接的英文文件名，Release 附件标签和清单保留原始文件名。

在所有 ZIP 的下载目录中运行：

```sh
sha256sum -c SHA256SUMS.txt
```

`git clone` 获取目录和脚本；ZIP 内容需要从上面的 Release 链接另行下载。

解析包的导入流程会先检查原始文件，再核对 GitHub 保存的字节数和 SHA-256；13 份全部通过后才发布 Release。
