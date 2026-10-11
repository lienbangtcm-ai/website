from pathlib import Path
import re,json,urllib.parse
root=Path('output/site-preview')
fsn='/assets/symptoms-20261010/frozen-shoulder-1600.webp'
catalog=[('/pulse-diagnosis/','中醫內科／脈診','辨證處方・體質調理','/assets/service-internal-real-v3.png'),('/acupuncture/','針灸','不留針・快速放鬆','/assets/user-20261009/wrist.webp'),('/acupuncture-physical-therapy/','中醫 × 物理治療','整合評估・動作控制','/assets/user-20261009/movement.webp'),('/浮針/','浮針','患肌評估・活動調整',fsn),('/針刀/','針刀','精準處理・組織疼痛','/assets/service-acupotomy-real-v3.png'),('/美顏針/','美顏針','自然調理・由內而外','/assets/user-20261009/facial.webp')]
byhref={r[0]:r for r in catalog}
changed=[]
for p in root.rglob('*.html'):
 if any(x in p.relative_to(root).parts for x in ['review','assets']):continue
 s=p.read_text(encoding='utf-8');old=s
 def anchor(m):
  chunk=m[0];href=re.search(r'href="([^"]+)"',chunk)
  if not href:return chunk
  url=urllib.parse.unquote(href[1]);
  if url in ['/埋線/','/embedding/']:
   chunk=chunk.replace(href[1],urllib.parse.quote('/浮針/'),1).replace('穴位埋線','浮針').replace('埋線','浮針').replace('長期調理・體態改善','患肌評估・活動調整').replace('使用可吸收線材，操作前需個別評估並說明後續照護。','依患肌、活動限制與個別狀況評估浮針治療。')
   chunk=re.sub(r'(<img\b[^>]*src=")[^"]+',r'\g<1>'+fsn,chunk)
   chunk=re.sub(r'(<img\b[^>]*alt=")[^"]*',r'\g<1>肩部不適情境示意',chunk)
  if url=='/針刀/':chunk=chunk.replace('針刀／浮針','針刀').replace('肩背部針刀與浮針治療情境','肩背部針具操作情境示意')
  return chunk
 s=re.sub(r'<a\b[^>]*>.*?</a>',anchor,s,flags=re.S)
 # Stable shared six-item order in menus, homepage and service overview.
 for cls in ['global-treatment-card','home-service-card','to-service-card']:
  matches=list(re.finditer(r'<a\b[^>]*class="'+cls+r'"[^>]*>.*?</a>',s,re.S))
  if len(matches)==6:
   mapped={urllib.parse.unquote(re.search(r'href="([^"]+)"',m[0])[1]):m[0] for m in matches}
   if set(mapped)==set(byhref):s=s[:matches[0].start()]+''.join(mapped[r[0]] for r in catalog)+s[matches[-1].end():]
 def schema(m):
  try:data=json.loads(m[2])
  except:return m[0]
  if isinstance(data,dict) and data.get('@type')=='ItemList' and data.get('numberOfItems')==6:
   data['itemListElement']=[{'@type':'ListItem','position':i+1,'name':r[1],'url':'https://lienbangtcm.tw'+urllib.parse.quote(r[0])} for i,r in enumerate(catalog)]
   return m[1]+json.dumps(data,ensure_ascii=False,separators=(',',':'))+m[3]
  return m[0]
 s=re.sub(r'(<script[^>]*type="application/ld\+json"[^>]*>)(.*?)(</script>)',schema,s,flags=re.S)
 if p.parent.name=='浮針':
  s=s.replace("--su-photo:url('/services/images/fsn.webp')","--su-photo:url('"+fsn+"')")
 if p.parent.name=='埋線':
  # Keep historical address accessible, but do not present retired treatment for booking.
  archive=Path('output/archive/retired-embedding')/('dist-index.html' if 'dist' in p.parts else 'index.html');archive.parent.mkdir(parents=True,exist_ok=True);archive.write_text(old,encoding='utf-8')
  header=re.search(r'<header class="global-header">.*?</header>',s,re.S)[0]
  footer=re.search(r'<footer id="site-footer".*?</footer>',s,re.S)[0]
  s='<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>療程資訊更新｜連邦中醫診所</title><link rel="stylesheet" href="/assets/global-shell.css"><link rel="stylesheet" href="/assets/shell-unified-20261009.css"><link rel="stylesheet" href="/assets/home-design-system-20261009.css"></head><body class="shell-unified home-system">'+header+'<main style="width:92%;max-width:1040px;margin:70px auto;min-height:320px"><h1>療程資訊更新</h1><p>穴位埋線目前未提供。請查看連邦目前的六項治療服務，再由醫師依個別狀況評估適合的安排。</p><p><a href="/services/">查看目前治療服務</a></p></main>'+footer+'<script src="/assets/global-shell.js?v=2" defer></script></body></html>'
 if s!=old:p.write_text(s,encoding='utf-8');changed.append(str(p))
Path('output/visual-qa/six-services-audit/catalog-20261011.json').write_text(json.dumps({'services':[{'href':r[0],'title':r[1],'description':r[2],'image':r[3]} for r in catalog],'changedFiles':changed,'retired':'/埋線/','imageNote':'浮針使用肩部不適情境圖，並非浮針操作示範；需要診所提供操作照片。'},ensure_ascii=False,indent=2),encoding='utf-8')
print(f'Updated {len(changed)} HTML files; retired embedding archived locally')
