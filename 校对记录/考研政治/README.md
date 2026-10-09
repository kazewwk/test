# 考研政治教材：OCR原页核对

五本教材共 **1,724个PDF物理页**，均从原始PDF渲染为144dpi图像，使用独立的中文PP-OCRv4进行识别，并与MinerU Hybrid解析逐区块交叉比较。可提取的原生文字也作为辅助比对来源。

已查看 **1,159个区块的差异局部及重点版面**，按原图确认 **307项区块修订**：290项移除扫描边缘或空白页上的幻觉内容，3项替换/补全区块文字，7项明确的局部文字更正，7项将不可靠图像誊写改为原图。

**仍有1,386页带待复核候选。候选不等于OCR错误**：另一套OCR也会识错，且原生文字层、扫描倾斜、小字、公式和区块边界都会引入差异。看过局部也不代表整个区块每个字都已认证。本次没有宣称全书逐字人工校对完成，也不保证字符准确率。标点、公式、模糊手写材料及图片中的全部文字仍需对照原页核对。

| 教材 | 原页数 | 确认修订 | 查看差异局部/重点区块 | 有待复核候选的页数 | 逐页记录 |
|---|---:|---:|---:|---:|---|
| 中国近现代史纲要（2023年版） | 429 | 14 | 217 | 406 | [查看](../../%E4%B8%AD%E5%9B%BD%E8%BF%91%E7%8E%B0%E4%BB%A3%E5%8F%B2%E7%BA%B2%E8%A6%81%EF%BC%882023%E5%B9%B4%E7%89%88%EF%BC%89/ocr_review/README.md) |
| 习近平新时代中国特色社会主义思想概论 | 384 | 280 | 402 | 291 | [查看](../../%E4%B9%A0%E8%BF%91%E5%B9%B3%E6%96%B0%E6%97%B6%E4%BB%A3%E4%B8%AD%E5%9B%BD%E7%89%B9%E8%89%B2%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89%E6%80%9D%E6%83%B3%E6%A6%82%E8%AE%BA/ocr_review/README.md) |
| 思想道德与法治（2023）优化版 | 264 | 7 | 250 | 181 | [查看](../../%E6%80%9D%E6%83%B3%E9%81%93%E5%BE%B7%E4%B8%8E%E6%B3%95%E6%B2%BB%EF%BC%882023%EF%BC%89%E4%BC%98%E5%8C%96%E7%89%88/ocr_review/README.md) |
| 毛泽东思想和中国特色社会主义理论体系概论 | 284 | 2 | 130 | 232 | [查看](../../%E6%AF%9B%E6%B3%BD%E4%B8%9C%E6%80%9D%E6%83%B3%E5%92%8C%E4%B8%AD%E5%9B%BD%E7%89%B9%E8%89%B2%E7%A4%BE%E4%BC%9A%E4%B8%BB%E4%B9%89%E7%90%86%E8%AE%BA%E4%BD%93%E7%B3%BB%E6%A6%82%E8%AE%BA/ocr_review/README.md) |
| 马克思主义基本原理（2023年版，数字版） | 363 | 4 | 160 | 276 | [查看](../../%E9%A9%AC%E5%85%8B%E6%80%9D%E4%B8%BB%E4%B9%89%E5%9F%BA%E6%9C%AC%E5%8E%9F%E7%90%86%EF%BC%882023%E5%B9%B4%E7%89%88%EF%BC%8C%E6%95%B0%E5%AD%97%E7%89%88%EF%BC%89/ocr_review/README.md) |

[更新后的五本书ZIP](https://github.com/kazewwk/test/releases/tag/kaoyan-politics-books-2026-10-09) · [全部原页独立OCR运行](https://github.com/kazewwk/test/actions/runs/37904595224)

每本书的 `ocr_review/` 包含 `page_audit.json`（原页定位、识别参数、文字与差异）、`corrections.json`（修正前后、坐标、源文件校验值）、`summary.json` 和 `index.html`。下载对应整书ZIP后，打开该书 `ocr_review/index.html` 可并排查看原PDF与每个物理页的OCR，按页翻阅或筛选待复核页面。章节内的 `ocr_review.md` 也逐页链接原PDF。

原始PDF、章节 `source.pdf`、原生文字和 `raw_chunks/` 的SHA-256保持不变；修订写入章节Markdown、JSON和整书全文。无法可靠誊写的手写内容以原图保留，并明确注明。原表格、图表、二维码和其他图像继续保存。所有仓库单文件均小于100,000,000字节。

`evidence/` 保存已查看的原页局部与重点整页。比对图中的箭头仅表示两套识别结果的差别，不表示已经判定哪个正确：`native/` 中的 `#编号` 对应 `native-differences.json` 的零起始数组下标；`independent/` 的 `#编号.差异编号` 对应 `independent-differences.json` 与 `independent-review-items.json`。文件名中的 B 为本书计划中的书ID，P为PDF物理页；扫描边缘联络图直接标出页码与区块号。

`ocr-corrections.json` 保存全部307项确认修订，`visual-review-decisions.json` 保存局部查阅范围和未裁定说明。比对数据保留修订前快照；最新文字和待复核状态以各书 `ocr_review/page_audit.json` 为准。

工具：[逐页独立OCR](../../scripts/audit_politics_ocr.py) · [应用修订及打包](../../scripts/review_politics_ocr.py)。应用修订脚本只接受对应的原始解析快照，并对每个修改区块核验SHA-256；已修订的目录不可直接重复应用。原页截图和比较脚本使用工作目录 `/workspace/politics-books`，运行时需保留原PDF、解析基线及独立OCR输入。
