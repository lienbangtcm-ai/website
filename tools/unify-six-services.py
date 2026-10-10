from pathlib import Path
import re
root=Path('output/site-preview');routes=['pulse-diagnosis','acupuncture','acupuncture-physical-therapy','針刀','美顏針','埋線','浮針'];photos=['/assets/user-20261009/pulse-hero.webp','/assets/user-20261009/wrist.webp','/assets/user-20261009/movement.webp','/assets/service-acupotomy-real-v3.png','/assets/user-20261009/facial.webp','/assets/service-embedding-real-v3.png','/services/images/fsn.webp']
for base in [root,root/'dist']:
 for route,photo in zip(routes,photos):
  f=base/route/'index.html'
  if not f.exists():continue
  t=f.read_text(encoding='utf-8')
  if 'service-unified-20261009.css' in t:continue
  m=re.search(r'<(section|header)\b[^>]*class="(?:pd-hero|lbnr-hero|lb-hero)"[^>]*>.*?</\1>',t,re.S)
  if not m:raise Exception(route)
  old=m[0];h=re.search(r'<h1\b.*?</h1>',old,re.S)[0];paras=re.findall(r'<p\b[^>]*>.*?</p>',old,re.S);links=re.findall(r'<a\b[^>]*>.*?</a>',old,re.S)
  if len(paras)==1:
   first=re.search(r'<section\b[^>]*class="lb-section[^\"]*"[^>]*>.*?<p\b[^>]*>(.*?)</p>',t,re.S)
   if first:paras.append('<p>'+first[1]+'</p>')
  content=paras[0]+h+''.join(paras[1:]);buttons=''.join(links) or '<a href="https://lin.ee/UWWKmse">LINE 預約諮詢</a>'
  hero=f'<section class="su-hero" style="--su-photo:url(\'{photo}\')"><div class="su-hero-inner"><div class="su-hero-copy">{content}<div class="su-actions">{buttons}</div></div></div></section>'
  t=t[:m.start()]+hero+t[m.end():]
  # Preserve the existing explanatory illustration outside the hero.
  if route=='針刀':
   img=re.search(r'<img\b[^>]*>',old)
   if img:t=t.replace('<h2>針刀是什麼？</h2>','<h2>針刀是什麼？</h2><figure class="su-explanation">'+img[0]+'</figure>',1)
  if route=='pulse-diagnosis':
   t=t.replace('<section class="pd-benefits"','<section id="service-features" class="pd-benefits"').replace('<section class="rd-approach"','<section id="service-approach" class="rd-approach"').replace('<section class="pd-audience"','<section id="service-audience" class="pd-audience"')
   t=t.replace(hero,hero+'<nav class="su-nav" aria-label="本頁內容"><a href="#service-features">療程特色</a><a href="#service-approach">治療理念</a><a href="#service-audience">適合族群</a></nav>')
  t=t.replace('🏥 讓專業團隊成為您的健康後盾','讓專業團隊成為您的健康後盾')
  t=t.replace('</body>','<link rel="stylesheet" href="/assets/service-unified-20261009.css">\n</body>');t=t.replace('home-system"','home-system service-unified"')
  f.write_text(t,encoding='utf-8')
