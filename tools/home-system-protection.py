from pathlib import Path
import subprocess,json,re
from html.parser import HTMLParser
root=Path('output/site-preview');git=r'C:/Users/yutin/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/git/cmd/git.exe'
class Content(HTMLParser):
 def __init__(self):super().__init__();self.text=[];self.skip=0;self.seo=[];self.href=[];self.schema=[];self.inSchema=False
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ['style','script']:self.skip+=1
  if tag=='meta' or tag=='title' or (tag=='script' and ('src' in a or a.get('type')=='application/ld+json')):self.seo.append((tag,sorted(attrs)))
  if tag=='a' and 'href' in a:self.href.append(a['href'])
  if tag=='script' and a.get('type')=='application/ld+json':self.inSchema=True
 def handle_endtag(self,tag):
  if tag in ['style','script']:self.skip-=1
  if tag=='script':self.inSchema=False
 def handle_data(self,data):
  if self.inSchema:self.schema.append(data)
  if not self.skip:self.text.append(data)
def parse(s):
 p=Content();p.feed(s);return {'text':re.sub(r'\s+',' ',''.join(p.text)).strip(),'seo':p.seo,'schema':p.schema,'links':p.href}
report=[]
for p in root.rglob('index.html'):
 if 'review' in p.parts or 'dist' in p.parts:continue
 s=p.read_text(encoding='utf-8-sig')
 if 'global-shell.css' not in s:continue
 old=subprocess.check_output([git,'show','HEAD:'+p.as_posix()]).decode('utf-8-sig');a,b=parse(old),parse(s)
 report.append({'path':p.as_posix(),'contentUnchanged':a['text']==b['text'],'seoUnchanged':a['seo']==b['seo'] and a['schema']==b['schema'],'linksUnchanged':a['links']==b['links'],'homeBytesUnchanged':old==s if p==root/'index.html' else None})
Path('output/visual-qa/home-system/protection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'pages':len(report),'failures':[r for r in report if not all(r[k] for k in ['contentUnchanged','seoUnchanged','linksUnchanged'])]},ensure_ascii=False))
