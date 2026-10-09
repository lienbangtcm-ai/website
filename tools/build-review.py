from pathlib import Path
from PIL import Image
root=Path(__file__).resolve().parents[1]
qa=root/'output/visual-qa'
out=root/'output/site-preview/review'
out.mkdir(exist_ok=True)
names={'home':'首頁','services':'治療服務','symptoms':'常見症狀','team':'醫師團隊','about-lienbang':'關於連邦','acupuncture':'針灸','pulse-diagnosis':'中醫內科／脈診','acupuncture-physical-therapy':'中醫 × 物理治療'}
parts=['<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>視覺驗收</title><style>body{margin:24px;background:#fffdf9;color:#493023;font:16px/1.7 sans-serif}section{border-top:1px solid #dccab9;padding:24px 0}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}img{width:100%;height:auto}a{color:#795033}@media(max-width:700px){.pair{grid-template-columns:1fr}}</style><h1>本機視覺驗收紀錄</h1><p>八頁於 1440、768、390px 檢查，保留三輪修正紀錄。參考圖等比縮放，沒有拉伸高度。除首頁外沒有獨立手機參考圖，手機與平板對照不代表像素吻合率。</p><p>未完全一致：醫師原照白色背景、症狀照片待補、關於頁照片及影片待補、整合治療六項流程保留原醫療內容。功能通過不代表 100% 還原。</p>']
for route,label in names.items():
 url='/' if route=='home' else '/'+route+'/'
 parts.append(f'<section><h2>{label}</h2><a href="{url}">操作此頁</a>')
 for width in [1440,768,390]:
  parts.append(f'<details><summary>{width}px 修改前／修改後</summary><div class="pair">')
  for phase in ['baseline','final']:
   image=Image.open(qa/phase/f'{route}-{width}.png').convert('RGB');image.thumbnail((1000,20000))
   name=f'{route}-{width}-{phase}.webp';image.save(out/name,quality=82,method=0)
   caption='修改前' if phase=='baseline' else '修改後'
   parts.append(f'<figure><figcaption>{caption}</figcaption><a href="{name}"><img loading="lazy" src="{name}"></a></figure>')
  parts.append('</div></details>')
 for kind,label in [('compare','參考圖／最新實作'),('overlay','疊圖'),('diff','差異圖')]:
  image=Image.open(qa/'final'/f'{route}-1440-{kind}.jpg');image.thumbnail((1400,14000))
  name=f'{route}-{kind}.webp';image.save(out/name,quality=80)
  parts.append(f'<a href="{name}">{label}</a>　')
 parts.append('</section>')
parts.append('</html>');(out/'index.html').write_text(''.join(parts),encoding='utf-8')
