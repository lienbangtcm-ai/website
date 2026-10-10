import pathlib,re,json
from PIL import Image
root=pathlib.Path('output/site-preview'); assets=root/'assets/symptoms-20261010'; assets.mkdir(exist_ok=True)
rows=[('sciatica','坐骨神經痛','08_56_50-4'),('low-back-pain','腰背痛','08_56_49-3'),('neck-shoulder-pain','肩頸痛','08_56_47-2'),('frozen-shoulder','五十肩','08_56_46-1'),('fatigue','疲倦','08_44_02-8'),('menstrual-pain','經痛','08_44_00-7'),('constipation','便秘','08_44_00-6'),('diarrhea','腹瀉','08_43_58-5'),('allergic-rhinitis','鼻過敏','08_43_58-4'),('insomnia','失眠','08_43_57-3'),('cough','咳嗽','08_43_56-2'),('gerd','胃食道逆流','08_43_55-1'),('knee-pain','膝痛','08_56_51-5'),('tennis-elbow','網球肘','08_56_53-6'),('de-quervain','媽媽手','08_56_55-7'),('plantar-heel-pain','足底痛','08_56_56-8')]
manifest=[]
for slug,title,stamp in rows:
 source=pathlib.Path('C:/Users/yutin/Downloads')/f'ChatGPT 圖像 2026年10月10日 上午{stamp}.png'
 im=Image.open(source).convert('RGB')
 for width in (1600,640):
  copy=im.copy();copy.thumbnail((width,10000));copy.save(assets/f'{slug}-{width}.webp',quality=83,method=4)
 manifest.append(dict(slug=slug,title=title,source=str(source),asset=f'/assets/symptoms-20261010/{slug}-1600.webp'))
(assets/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print('Exported 32 optimized images')
by_slug={r['slug']:r for r in manifest}
def photo(slug,eager=False):
 r=by_slug[slug];base=f'/assets/symptoms-20261010/{slug}'
 return f'<img src="{base}-1600.webp" srcset="{base}-640.webp 640w, {base}-1600.webp 1600w" sizes="(max-width: 767px) 91vw, 46vw" alt="{r["title"]}生活不適情境示意" width="1672" height="941" loading="{"eager" if eager else "lazy"}" decoding="async">'
count=0
for path in root.rglob('*.html'):
 if 'review' in path.relative_to(root).parts or 'assets' in path.relative_to(root).parts:continue
 s=path.read_text(encoding='utf-8');original=s
 def anchor(m):
  chunk=m.group(0);hit=re.search(r'href=["\']/symptoms/([^/]+)/',chunk)
  if hit and hit[1] in by_slug and '<img' in chunk:chunk=re.sub(r'<img\b[^>]*>',photo(hit[1]),chunk,count=1)
  return chunk
 s=re.sub(r'<a\b[^>]*>.*?</a>',anchor,s,flags=re.S)
 slug=path.parent.name
 if slug in by_slug and 'lb-hero-grid' in s and 'sr-hero-photo' not in s:
  def hero(m):
   chunk=m.group(0);match=re.search(r'<div class="lb-shell lb-hero-grid">(.*)</div>\s*</header>',chunk,re.S)
   if not match:return chunk
   content=match[1]
   content=re.sub(r'<figure\b.*?</figure>','',content,flags=re.S)
   return '<header class="lb-hero"><div class="lb-shell lb-hero-grid"><div class="sr-hero-copy">'+content+'</div><figure class="sr-hero-photo">'+photo(slug,True)+'</figure></div></header>'
  s=re.sub(r'<header class="lb-hero">.*?</header>',hero,s,count=1,flags=re.S)
  def symptom_figure(m):
   return re.sub(r'<picture>.*?</picture>',photo(slug),m.group(0),flags=re.S)
  s=re.sub(r'<figure\b[^>]*data-article-image="symptoms".*?</figure>',symptom_figure,s,flags=re.S)
  s=re.sub(r'(<body class=")',r'\1symptoms-refresh ',s,count=1)
 if path.parent.name=='symptoms' and 'symptoms-refresh ' not in s:s=re.sub(r'(<body class=")',r'\1symptoms-refresh ',s,count=1)
 if 'symptoms-refresh ' in s and 'symptoms-refresh-20261010.css' not in s:s=s.replace('</head>','<link rel="stylesheet" href="/assets/symptoms-refresh-20261010.css">\n</head>')
 if s!=original:path.write_text(s,encoding='utf-8');count+=1
print(f'Updated {count} HTML files')
