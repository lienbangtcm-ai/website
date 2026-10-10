from pathlib import Path
import json,html
from PIL import Image
q=Path('output/visual-qa/home-system');dest=Path('output/site-preview/review/home-system');dest.mkdir(parents=True,exist_ok=True)
data=json.loads((q/'final/report.json').read_text(encoding='utf-8'));pages=[p for p in data['pages'] if p['width']==1440];sections=[]
for p in pages:
 route=p['route'];key=route.replace('/','--');images=[]
 for w in [1440,390]:
  pair=[]
  for phase in ['before','final']:
   name=f'{key}-{w}-{phase}.webp';Image.open(q/phase/f'{key}-{w}.png').save(dest/name,'WEBP',quality=75);pair.append(f'<figure><figcaption>{"修改前" if phase=="before" else "修改後"} · {w}px</figcaption><a href="{name}" target="_blank"><img loading="lazy" src="{name}" alt="{html.escape(route)} {phase} {w}"></a></figure>')
  images.append('<div class="pair">'+''.join(pair)+'</div>')
 sections.append(f'<section><h2>{html.escape(p["title"])} <small>/{route if route!="home" else ""}/</small></h2><p>1440 / 768 / 390px：溢出、圖片、標題、FAQ、手機選單及執行錯誤驗證通過。</p>'+''.join(images)+'</section>')
page='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>連邦全站首頁設計統一對照</title><style>body{margin:0;background:#fffdf9;color:#281c15;font:17px/1.8 Microsoft JhengHei,sans-serif}main{max-width:1320px;margin:auto;padding:40px 24px}h1{font-size:36px}h2{font-size:25px}small{font-size:15px;color:#887b70}section{padding:32px 0;border-top:1px solid #e6ddd3}.pair{display:grid;grid-template-columns:1fr 1fr;gap:24px;margin-bottom:30px}figure{margin:0;background:#fffdfa}img{width:100%;display:block}figcaption{padding:12px;font-weight:bold}a{color:#825332}@media(max-width:600px){.pair{gap:10px}main{padding:20px 12px}}</style><main><h1>以首頁為基準的全站視覺統一</h1><p>共 31 頁，桌機與手機 62 張修改前、62 張修改後完整截圖。點選圖片可開啟完整尺寸。</p><p>首頁依後續指示同步六項服務圖片、雙語標題、對齊與移除圓圈箭頭；醫療內容、SEO、Schema、追蹤腳本與既有目的連結保留。設計採首頁暖米白 #fffdf9、深木色 #281c15、19px 桌機內文、1320px 最大內容寬度。</p><p>已統一全域字體、Hero、卡片、CTA 與響應式尺寸；保留各頁的文章、醫師與服務結構。醫師個人頁改回原始人像。六個服務頁已統一主視覺、章節導覽、流程卡片與預約區；各頁長度依原始內容保留差異。</p><p>待提供：真實症狀照片、部分實際治療攝影及品牌影片。既有情境素材保留，不能視為實際診所攝影。衛教與交通導覽仍沿用既有連結目的地。</p>'''+''.join(sections)+'</main></html>'
(dest/'index.html').write_text(page,encoding='utf-8');print('31 page comparison report generated')

