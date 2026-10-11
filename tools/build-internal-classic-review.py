from pathlib import Path
from PIL import Image
import json,html
base=Path('output/visual-qa/home-system');out=Path('output/site-preview/review/internal-classic');out.mkdir(parents=True,exist_ok=True)
manifest=json.loads(Path('output/site-preview/assets/symptoms-20261010/manifest.json').read_text(encoding='utf-8'))
rows=[('symptoms/'+r['slug'],r['title']) for r in manifest if r['slug'] in ['gerd','cough','insomnia','allergic-rhinitis','diarrhea','constipation','menstrual-pain','fatigue']]
parts=[]
for route,title in rows:
 chunks=[]
 for w in (1440,390):
  cells=[]
  for phase,label in [('internal-reader-final','修改前'),('internal-classic-restored','修改後')]:
   source=base/phase/(route.replace('/','--')+f'-{w}.png')
   dest=out/(route.replace('/','--')+f'-{w}-{phase}.webp')
   im=Image.open(source);im.thumbnail((900,30000));im.save(dest,quality=76,method=3)
   cells.append(f'<div><h3>{label}</h3><a href="{dest.name}"><img src="{dest.name}" loading="lazy" alt="{title}{label}"></a></div>')
  chunks.append(f'<h3>{w}px</h3><div class="compare">'+''.join(cells)+'</div>')
 parts.append(f'<section id="{route.replace("/","-")}"><h2>{title}</h2><a href="/{route}/">開啟頁面</a>'+''.join(chunks)+'</section>')
text='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>內科頁恢復中醫版型對照</title><style>body{margin:0;background:#fffdf9;color:#281c15;font:17px/1.8 Microsoft JhengHei,sans-serif}main{max-width:1400px;margin:auto;padding:32px}h1,h2{font-family:PMingLiU,serif}.compare{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}img{width:100%;height:auto;border:1px solid #e6ddd3}section{margin:60px 0;padding-top:24px;border-top:1px solid #e6ddd3}a{color:#89603f}@media(max-width:600px){main{padding:16px}.compare{gap:10px}}</style><main><h1>內科頁恢復中醫版型對照</h1><p>恢復八個內科頁原有中醫文章結構，辨證、脈診與治療直接呈現，保留新症狀照片。桌機 1440px、手機 390px；平板 768px 功能及溢出檢查另存測試紀錄。</p><p>原有醫療段落、SEO與追蹤腳本保留；移除重複主圖，详细辨證恢復直接呈現。既有療效描述尚未做醫師核定，本次未新增療效保證。</p>'''+''.join(parts)+'</main></html>'
(out/'index.html').write_text(text,encoding='utf-8')
print('Built 8-page comparison report')
