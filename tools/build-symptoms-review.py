from pathlib import Path
from PIL import Image
import json,html
base=Path('output/visual-qa/home-system');out=Path('output/site-preview/review/symptoms-refresh');out.mkdir(parents=True,exist_ok=True)
manifest=json.loads(Path('output/site-preview/assets/symptoms-20261010/manifest.json').read_text(encoding='utf-8'))
rows=[('symptoms','常見症狀總覽')]+[('symptoms/'+r['slug'],r['title']) for r in manifest]
parts=[]
for route,title in rows:
 chunks=[]
 for w in (1440,390):
  cells=[]
  for phase,label in [('symptoms-before','修改前'),('symptoms-approved','修改後')]:
   source=base/phase/(route.replace('/','--')+f'-{w}.png')
   dest=out/(route.replace('/','--')+f'-{w}-{phase}.webp')
   im=Image.open(source);im.thumbnail((900,30000));im.save(dest,quality=76,method=3)
   cells.append(f'<div><h3>{label}</h3><a href="{dest.name}"><img src="{dest.name}" loading="lazy" alt="{title}{label}"></a></div>')
  chunks.append(f'<h3>{w}px</h3><div class="compare">'+''.join(cells)+'</div>')
 parts.append(f'<section id="{route.replace("/","-")}"><h2>{title}</h2><a href="/{route}/">開啟頁面</a>'+''.join(chunks)+'</section>')
text='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>症狀頁修改前後對照</title><style>body{margin:0;background:#fffdf9;color:#281c15;font:17px/1.8 Microsoft JhengHei,sans-serif}main{max-width:1400px;margin:auto;padding:32px}h1,h2{font-family:PMingLiU,serif}.compare{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}img{width:100%;height:auto;border:1px solid #e6ddd3}section{margin:60px 0;padding-top:24px;border-top:1px solid #e6ddd3}a{color:#89603f}@media(max-width:600px){main{padding:16px}.compare{gap:10px}}</style><main><h1>症狀頁修改前後對照</h1><p>16 張使用者提供的症狀情境照片，沿用既定品牌與醫療文章格式。桌機 1440px、手機 390px；平板 768px 功能及溢出檢查另存測試紀錄。</p><p>三輪檢查：第一輪補齊照片與主視覺；第二輪修正舊欄寬衝突；第三輪改善手機總覽主視覺。原有評估與照護圖解保留，並非實際患者或診所紀錄照片。</p>'''+''.join(parts)+'</main></html>'
(out/'index.html').write_text(text,encoding='utf-8')
print('Built 17-page comparison report')
