from pathlib import Path
from lxml import html
import re,json,shutil,hashlib
from clinic_illustrations_v4 import ART
R=Path(__file__).resolve().parents[1];S=R/'output/site-preview';B=R/'output/identity-backup';B.mkdir(exist_ok=True)
files=[S/'index.html']+list((S/'symptoms').glob('*/index.html'))
def signature(text):
 d=html.fromstring(text);main=d.xpath('//main | //*[contains(concat(" ",normalize-space(@class)," ")," lb-article ")]')[0]
 return {'text':hashlib.sha256(main.text_content().encode()).hexdigest(),'images':[dict(x.attrib) for x in main.xpath('.//img|.//source')],'links':[x.get('href') for x in main.xpath('.//a')]}
checks=[]
for f in files:
 original=f.read_text(encoding='utf-8');backup=B/f.relative_to(S);backup.parent.mkdir(parents=True,exist_ok=True)
 if not backup.exists():shutil.copy2(f,backup)
 before=signature(original)
 if f==S/'index.html':
  d=html.fromstring(original)
  for node in d.xpath('//img[contains(@class,"lbh4-hero-img") or contains(@class,"lbh4-about-img")]'):node.getparent().remove(node)
  for card,key in zip(d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lbh4-service ")]'),['movement','pulse','facial']):
   for img in card.xpath('./img'):card.remove(img)
   if not card.xpath('./svg'):card.insert(0,html.fromstring(ART[key]))
  original='<!doctype html>'+html.tostring(d,encoding='unicode')
 original=re.sub(r'<link[^>]+href="/assets/site-editorial.css[^\"]*"[^>]*>','',original)
 original=original.replace('</body>','<link rel="stylesheet" href="/assets/site-editorial.css?v=1"></body>')
 if f!=S/'index.html':
  assert before==signature(original),str(f)
  checks.append({'page':str(f.relative_to(S)),'text_images_links_unchanged':True})
 f.write_text(original,encoding='utf-8')
shutil.copy2(R/'lienbang-assets/site-editorial.css',S/'assets/site-editorial.css')
(R/'output/release-audit/editorial-content-preservation.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print('Homepage updated; article preservation checked:',len(checks))
