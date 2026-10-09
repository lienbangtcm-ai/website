from pathlib import Path
from PIL import Image,ImageChops
root=Path(__file__).resolve().parents[1]
qa=root/'output/visual-qa'
out=root/'output/site-preview/review/about-update'
out.mkdir(exist_ok=True)
parts=['<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>關於連邦修正對照</title><style>body{background:#fffdf9;color:#493023;margin:24px;font:16px/1.7 sans-serif}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}img{width:100%}a{color:#795033}@media(max-width:700px){.pair{grid-template-columns:1fr}}</style><h1>關於連邦：最新修正</h1><p>統一暖米白與深木色、修正理念標題斷字、故事文字裁切、時間軸及照片排列。保留原合照、文字與連結；合照背景仍與設計圖不同，品牌影片待提供。</p><a href="/about-lienbang/">操作新版頁面</a>']
for width in [1440,768,390]:
 parts.append(f'<h2>{width}px 修改前／修改後</h2><div class="pair">')
 for phase,folder in [('before','final'),('after','about-polish-3')]:
  image=Image.open(qa/folder/f'about-lienbang-{width}.png').convert('RGB');image.thumbnail((1000,12000));name=f'{width}-{phase}.webp';image.save(out/name,quality=84,method=0)
  parts.append(f'<figure><figcaption>{phase}</figcaption><a href="{name}"><img loading="lazy" src="{name}"></a></figure>')
 parts.append('</div>')
actual=Image.open(qa/'about-polish-3/about-lienbang-1440.png').convert('RGB')
ref=Image.open(Path('C:/Users/yutin/Downloads/ChatGPT 圖像 2026年10月9日 下午01_42_11-1.png')).convert('RGB');ref=ref.resize((1440,int(ref.height*1440/ref.width)))
height=max(actual.height,ref.height);a=Image.new('RGB',(1440,height),'#eee');a.paste(actual);b=Image.new('RGB',(1440,height),'#eee');b.paste(ref)
side=Image.new('RGB',(2880,height),'white');side.paste(b);side.paste(a,(1440,0))
for name,image in [('compare',side),('overlay',Image.blend(a,b,.5)),('diff',ImageChops.difference(a,b))]:
 image.thumbnail((1600,12000));image.save(out/f'{name}.webp',quality=85,method=0);parts.append(f'<a href="{name}.webp">{name}</a>　')
parts.append('<p>桌面參考等比縮放至 1440px，不以照片與文字差異計算還原百分比。手機沒有獨立參考圖。</p></html>')
(out/'index.html').write_text(''.join(parts),encoding='utf-8')
