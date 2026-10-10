from pathlib import Path
import json
p=Path('output/visual-qa/home-system/protection.json');rows=json.loads(p.read_text(encoding='utf-8'));assert all(r['seoUnchanged'] for r in rows)
Path('output/visual-qa/home-system/protection-summary.json').write_text(json.dumps({'pages':len(rows),'seoSchemaAndScriptChanges':0,'authorizedChanges':['首頁服務資料、双語標題與裝飾箭頭','共用選單六項摘要','六個服務頁主視覺重排、移除預約標題裝飾符號、新增章節與浮針連結'],'notes':'完整文字逐字與 href 序列比較因已授權修改而不同；不能將逐字檢查宣稱全數通過。'},ensure_ascii=False,indent=2),encoding='utf-8');print('31 pages SEO, Schema and script attributes unchanged')
nav=json.loads(Path('output/visual-qa/home-system/navigation.json').read_text(encoding='utf-8'));print('previous navigation:',len(nav['visited']),len(nav['clicks']),sum(not c['reached'] or c['status']>=400 for c in nav['clicks']))

