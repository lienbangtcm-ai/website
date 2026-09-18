from pathlib import Path
from lxml import html
p=Path('output/site-preview/pulse-diagnosis/index.html');s=p.read_text(encoding='utf-8')
b=Path('output/release-audit/pulse-v19.html')
if not b.exists():b.write_text(s,encoding='utf-8')
s=b.read_text(encoding='utf-8')
d=html.fromstring(s)
def one(x):return d.xpath(x)[0]
def text(x,t):
 e=one(x)
 for c in list(e):e.remove(c)
 e.text=t
def remove(x):
 for e in d.xpath(x):e.getparent().remove(e)
hero=one('//section[contains(@class,"internal-hero")]')
h=hero.xpath('.//h1')[0];h.addprevious(html.fragment_fromstring('<span class="internal-label">中醫內科</span>'))
h.text='從脈象與症狀，';h.append(html.fragment_fromstring('<br>'));h[-1].tail='理解身體現在的狀態'
remove('//p[@class="internal-subtitle"]')
text('//section[contains(@class,"internal-hero")]//p','從睡眠、腸胃、生理週期到反覆疲勞，我們會將症狀與整體狀態一起評估。')
for a,t in zip(hero.xpath('.//a'),['LINE 預約','門診時間']):a.text=t
im=hero.xpath('.//img')[0];im.set('src','/assets/internal-editorial/pulse.webp');im.set('alt','把脈評估（情境示意）')
text('//div[@class="internal-situations"]/../h2','常見內科狀況')
remove('//p[@class="internal-intro"]')
for a,(title,desc) in zip(d.xpath('//div[@class="internal-situations"]/article'),[('睡眠與疲勞','失眠、淺眠、容易累'),('腸胃與消化','胃脹、消化不良、排便不穩'),('生理週期','經痛、月經不規律、更年期不適'),('頭暈與心悸','容易疲勞、精神不集中'),('反覆不舒服','檢查正常但身體狀態不佳'),('呼吸與過敏','鼻過敏、咳嗽、感冒後恢復慢')]):
 a.find('h3').text=title;a.find('p').text=desc
remove('//*[@id="assessment"]/div/h2')
e=one('//*[@id="assessment"]//h3');e.tag='h2'
text('//*[@id="assessment"]//div[@class="internal-split"]/div/p','我們會把脈象、症狀與生活狀態一起判斷，再決定當次治療方向。')
for e,t in zip(d.xpath('//ol[@class="internal-points"]/li'),['了解主要不舒服','脈象補充身體線索','回診重新比對變化']):e.text=t
trust=one('//div[@class="internal-trust"]');trust.getparent().remove(trust)
one('//*[@id="assessment"]//div[@class="internal-split"]/div').append(html.fragment_fromstring('<div class="internal-trust"><p>院長張豫醫師亦投入脈診教學與臨床整合。</p><a href="https://clinical-pulse.com/" target="_blank" rel="noopener noreferrer">認識臨床脈學學院 →</a></div>'))
for e,t in zip(d.xpath('//div[@class="internal-cards"]/article/p'),['胃脹、胃食道逆流、排便異常','失眠、容易醒、心悸','經痛、週期不規律、更年期','容易累、怕冷、反覆不舒服','鼻過敏、咳嗽、恢復慢','食慾、睡眠、反覆感冒']):e.text=t
text('//*[@id="why"]//h2','依每次狀態，重新調整處方')
text('//*[@id="why"]//div/p','每一味藥都可依當下狀態調整，處方會隨每次回診重新修正。')
remove('//dl[@class="internal-benefits"]/dd')
text('//*[@id="dose"]//div/div[1]/p','部分個案每日濃縮粉總量')
text('//*[@id="dose"]//div/div[2]/p','實際用量會依症狀、體質、病程與濃縮倍率調整。')
for e,t in zip(d.xpath('//div[@class="internal-flow"]/article/p'),['了解症狀與目前用藥','搭配症狀與生活狀態判斷','說明健保、自費與用藥安排','依每次變化調整方向']):e.text=t
e=one('//div[@class="internal-fee-note"]');e.getparent().replace(e,html.fragment_fromstring('<p class="internal-fee-note">如有自費項目，治療前會先說明。</p>'))
ending=one('//section[@class="internal-ending"]');ending.tag='div';ending.getparent().remove(ending);one('//*[@id="faq"]').append(ending)
for e in d.xpath('//link[contains(@href,"internal-editorial.css")]'):e.set('href','/assets/internal-editorial.css?v=20')
one('//body').append(html.fragment_fromstring('<link rel="stylesheet" href="/assets/internal-service-layout.css?v=20">'))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
