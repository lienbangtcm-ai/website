from pathlib import Path
from lxml import html
import shutil
R=Path(__file__).resolve().parents[1];f=R/'output/site-preview/index.html'
b=R/'output/identity-backup/home-before-structure.html'
if not b.exists():shutil.copy2(f,b)
d=html.fromstring(f.read_text(encoding='utf-8'));main=d.xpath('//main')[0]
def one(cls):return main.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," '+cls+' ")]')[0]
quick=one('lbh4-quick-grid')
for child in list(quick):quick.remove(child)
for href,num,title,desc in [('https://lin.ee/UWWKmse','01','LINE 預約','預約看診與門診詢問'),('https://lienbangtcm.tw/support/#clinic-hours','02','門診時間','查看門診資訊與異動'),('https://lienbangtcm.tw/support/','03','交通位置','地址、捷運與交通導航')]:
 quick.append(html.fromstring(f'<a href="{href}"><b>{num}</b><span><strong>{title}</strong><small>{desc}</small></span><i aria-hidden="true">→</i></a>'))
team=one('lbh4-team').getparent().getparent()
services=d.get_element_by_id('treatment-services')
main.remove(team);main.insert(main.index(services)+1,team)
for card in one('lbh4-team'):
 card.set('class',card.get('class','')+' home-doctor-profile')
for card in one('lbh4-articles'):card.set('class',card.get('class','')+' home-journal-row')
if not one('lbh4-hero-copy').xpath('./p[@class="home-location"]'):
 title=one('lbh4-hero-copy').find('h1');title.addnext(html.fromstring('<p class="home-location">台北松山・中醫內科・針灸傷科</p>'))
f.write_text('<!doctype html>'+html.tostring(d,encoding='unicode'),encoding='utf-8')
print('Homepage shortcuts, team order and journal layout updated')
