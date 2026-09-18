from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote
root=Path(__file__).resolve().parents[1]/'output/site-preview'
class Parser(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.images=[];self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.add(a['id'])
  if tag=='h1':self.h1+=1
  if tag=='a':self.links.append(a.get('href',''))
  if tag=='img':self.images.append(a.get('src',''))
pages={}
for f in root.rglob('*.html'):
 p=Parser();p.feed(f.read_text(encoding='utf-8'));pages[f.resolve()]=p
errors=[]
for f,p in pages.items():
 if p.h1!=1:errors.append(f'{f.relative_to(root)}: H1={p.h1}')
 for u in p.links+p.images:
  v=urlparse(u)
  if v.scheme or v.netloc:continue
  path=unquote(v.path)
  target=((root/path.lstrip('/')) if path.startswith('/') else (f.parent/path)) if path else f
  if target.is_dir():target=target/'index.html'
  target=target.resolve()
  if not target.exists():errors.append(f'{f.relative_to(root)}: missing {u}')
  elif v.fragment and target in pages and v.fragment not in pages[target].ids:errors.append(f'{f.relative_to(root)}: anchor {u}')
print('\n'.join(errors) if errors else f'PASS: {len(pages)} pages, H1 counts, local links, anchors and local image paths')
raise SystemExit(bool(errors))
