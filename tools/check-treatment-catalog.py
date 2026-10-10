from pathlib import Path
import json
rows=json.loads(Path('output/visual-qa/six-services-audit/logic-audit.json').read_text(encoding='utf-8'));catalog={c['href']:c['img'] for c in rows[0]['cards'][:6]};bad=[]
for r in rows:
 for c in r['cards']:
  if c['href'] in catalog and c['img']!=catalog[c['href']]:bad.append(c)
assert not bad,bad
for r in rows:
 if r['route'] in ['pulse-diagnosis','acupuncture','acupuncture-physical-therapy','針刀','浮針','美顏針','埋線']:assert all(x=='LINE 預約諮詢' for x in r['cta']),(r['route'],r['cta'])
print('All audited treatment cards use canonical images; seven pages booking labels match')
