from pathlib import Path
from lxml import html
p=Path('output/site-preview/pulse-diagnosis/index.html');s=p.read_text(encoding='utf-8')
b=Path('output/release-audit/pulse-v20.html')
if not b.exists():b.write_text(s,encoding='utf-8')
d=html.fromstring(s)
def one(x):return d.xpath(x)[0]
assessment=one('//*[@id="assessment"]//img');assessment.set('src','/assets/internal-editorial/consult.webp');assessment.set('alt','醫師與患者問診（情境示意）')
right=one('//*[@id="assessment"]//div[@class="internal-split"]/div');right.insert(0,html.fragment_fromstring('<span class="internal-label">把脈與診療方式</span>'))
# The reference combines the duplicated condition/service lists into one scan row.
e=one('//*[@id="internal-overview"]');e.getparent().remove(e)
one('//div[@class="internal-situations"]/..').set('id','internal-overview')
nav=one('//nav[@class="internal-nav internal-shell"]');nav.getparent().remove(nav)
split=one('//*[@id="process"]');fig=split.find('figure');copy=split.find('div');benefits=copy.find('dl');copy.remove(benefits);split.remove(fig);split.insert(1,fig);split.append(benefits)
for dt,desc in zip(benefits.findall('dt'),['依當次狀態調整藥味','不同藥物可分別調整','依每次變化修正處方']):
 dd=html.Element('dd');dd.text=desc;dt.addnext(dd)
fees=one('//*[@id="fees"]/div');h=fees.find('h2');intro=html.Element('div',{'class':'internal-flow-intro'});fees.remove(h);intro.append(h);fees.insert(0,intro)
note=one('//p[@class="internal-fee-note"]');note.tag='div';note.text=None
note.append(html.fragment_fromstring('<strong>健保與自費說明</strong>'));note.append(html.fragment_fromstring('<span>如有自費項目，治療前會先說明原因、費用與使用方式。</span>'));note.append(html.fragment_fromstring('<a class="internal-btn" href="https://lin.ee/UWWKmse" target="_blank" rel="noopener noreferrer">LINE 預約 →</a>'))
one('//body').append(html.fragment_fromstring('<link rel="stylesheet" href="/assets/internal-reference-layout.css?v=21">'))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
