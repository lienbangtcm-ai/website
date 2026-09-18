from pathlib import Path
from lxml import html
p=Path('output/site-preview/index.html');s=p.read_text(encoding='utf-8')
b=Path('output/release-audit/home-v23.html')
if not b.exists():b.write_text(s,encoding='utf-8')
d=html.fromstring(s)
im=d.xpath('//section[@class="hr-about"]//img')[0]
im.set('src','/assets/clinic-photos/lobby.webp');im.set('alt','連邦中醫診所入口與接待空間實景')
for a in d.xpath('//div[@class="hr-doctor-grid"]/a'):
 im=a.find('img');a.remove(im);fig=html.Element('div',{'class':'hr-doctor-portrait'});fig.append(im);a.insert(0,fig)
 if 'dai-xuan' in im.get('src'):a.set('class','doctor-dai')
d.xpath('//body')[0].append(html.fragment_fromstring('<link rel="stylesheet" href="/assets/home-photo-refinement.css?v=24">'))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
