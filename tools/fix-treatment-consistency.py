from pathlib import Path
import re
root=Path('output/site-preview');routes={'pulse-diagnosis','acupuncture','acupuncture-physical-therapy','針刀','浮針','美顏針','埋線','services'}
photos={'針刀':'/assets/service-acupotomy-real-v3.png','美顏針':'/assets/user-20261009/facial.webp','埋線':'/assets/service-embedding-real-v3.png','浮針':'/services/images/fsn.webp'}
from urllib.parse import unquote
for f in root.rglob('index.html'):
 if 'review' in f.parts:continue
 t=f.read_text(encoding='utf-8')
 # Match treatment link images anywhere, including cross-recommendations.
 def card(m):
  route=unquote(m[1]).strip('/');src=photos.get(route)
  return re.sub(r'(<img\b[^>]*src=")[^"]+',lambda n:n[1]+src,m[0],count=1) if src else m[0]
 t=re.sub(r'<a\b[^>]*href="([^"]+)"[^>]*>\s*<img\b[^>]*>',card,t)
 t=t.replace('<strong>埋線</strong>','<strong>穴位埋線</strong>').replace('<h2>埋線</h2>','<h2>穴位埋線</h2>').replace('<h3>埋線</h3>','<h3>穴位埋線</h3>')
 if f.parent.name in routes:
  def booking(m):
   if 'lin.ee/UWWKmse' not in m[1] or 'rd-line-mark' in m[2]:return m[0]
   plain=re.sub('<[^>]+>','',m[2]).strip()
   if plain in ['預約內科諮詢 →','LINE 預約 →','立即預約評估 (LINE)','預約諮詢 →','LINE 預約諮詢']:return m[1]+'LINE 預約諮詢</a>'
   return m[0]
  t=re.sub(r'(<a\b[^>]*>)(.*?)</a>',booking,t,flags=re.S)
 if f.parent.name in ['針刀','浮針']:
  here=f.parent.name;other='浮針' if here=='針刀' else '針刀'
  if 'su-related-treatment' not in t:
   nav=f'<nav class="su-related-treatment" aria-label="針刀與浮針療程"><span>針刀與浮針為不同療程，請分別了解：</span><a href="/%E9%87%9D%E5%88%80/"'+(' aria-current="page"' if here=='針刀' else '')+'>針刀療程</a><a href="/%E6%B5%AE%E9%87%9D/"'+(' aria-current="page"' if here=='浮針' else '')+'>浮針療程</a></nav>'
   t=t.replace('<nav class="lb-toc"',nav+'<nav class="lb-toc"',1)
 f.write_text(t,encoding='utf-8')
