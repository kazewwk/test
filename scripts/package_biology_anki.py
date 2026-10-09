#!/usr/bin/env python3
"""将经过原生Anki核验的TXT和原图打包为一次下载的导入资料。"""
import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1] / 'anki'
FILES = ['SHU_2027_Biochemistry_2514_Basic.txt', 'SHU_Molecular_Anki.txt']

def run():
    status=json.loads((ROOT/'audit/status.json').read_text())
    check=json.loads((ROOT/'audit/anki-import-check.json').read_text())
    assert status['reviewed_chapters']==47 and status['reviewed_auxiliary_folders']==4
    assert status['reviewed_images']==status['total_images']==6615
    assert check['result']=='passed' and check['imported_notes']==status['total_cards']
    instructions=f'''生化与分子 Anki 原图优化版

共 {status['total_cards']} 张 Basic 单向问答卡（原3832张加{status['new_cards']}张必要识图卡）。

1. 先备份当前 Anki 集合。将本包 collection.media 文件夹中的全部图片直接复制到你当前 Anki 用户的 collection.media 文件夹，图片不应套子文件夹，也不要改名。
   Windows: %APPDATA%\\Anki2\\用户名称\\collection.media
   macOS: ~/Library/Application Support/Anki2/用户名称/collection.media
   Linux: ~/.local/share/Anki2/用户名称/collection.media
   使用自定义配置目录时，以实际用户配置目录为准。
2. 在桌面 Anki 分别导入两份 TXT。选择 Basic/基础（单向），Tab 分隔，启用 HTML。四列必须映射为：正面、背面、标签、牌组；第4列不是普通字段。推荐使用支持文件头的 Anki 2.1.54+。
3. 已有旧卡时，选择与旧卡相同的笔记类型，重复匹配范围设为“笔记类型”，选择“更新已有笔记”。保持了原3832张题面以匹配旧笔记。更新不会自动移动已有卡片；需要整理牌组时，用“浏览→卡片→更改牌组”，不要删除重建、忘记或重置。
4. 预览含图卡并运行“工具→检查媒体”，再同步手机。

47章、4个辅助目录的6615个教材图文件逐项审读；卡片使用教材原图及1张复核过的外部原图，没有模型绘图。英文主要支持读图和勘误。整题训练、逐图处理、出处及勘误详见 GitHub 仓库 anki/audit；本包核验结果来自临时Anki集合，未操作你的实际集合。

GitHub: https://github.com/kazewwk/test/tree/codex/anki-image-optimization-20261009/anki
'''
    target=ROOT/'biology_anki_import.zip'
    def put(z,name,data):
        info=zipfile.ZipInfo(name,date_time=(2026,10,9,0,0,0))
        info.compress_type=zipfile.ZIP_DEFLATED
        z.writestr(info,data)
    manifest=[json.loads(line) for line in (ROOT/'audit/media-manifest.jsonl').read_text().splitlines()]
    with zipfile.ZipFile(target,'w') as z:
        for name in FILES:put(z,name,(ROOT/name).read_bytes())
        put(z,'导入说明.txt',instructions.encode())
        put(z,'核验结果.json',(ROOT/'audit/anki-import-check.json').read_bytes())
        put(z,'媒体校验.jsonl',(ROOT/'audit/media-manifest.jsonl').read_bytes())
        for entry in manifest:
            data=(ROOT/'media'/entry['file']).read_bytes()
            assert hashlib.sha256(data).hexdigest()==entry['sha256']
            put(z,'collection.media/'+entry['file'],data)
    # The complete bundle must contain the exact checked TXT and the flat media directory.
    with zipfile.ZipFile(target) as z:
        assert len(z.namelist())==len(manifest)+len(FILES)+3
        for name in FILES:assert z.read(name)==(ROOT/name).read_bytes()
        for entry in manifest:
            assert hashlib.sha256(z.read('collection.media/'+entry['file'])).hexdigest()==entry['sha256']
    artifacts=[]
    for name in FILES+['biology_anki_media.zip','biology_anki_import.zip']:
        p=ROOT/name
        artifacts.append({'file':name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    (ROOT/'audit/artifact-manifest.json').write_text(json.dumps(artifacts,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(artifacts,ensure_ascii=False,indent=2))

if __name__=='__main__':run()
