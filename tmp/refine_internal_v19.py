from pathlib import Path
from lxml import html
import re,json
p=Path('output/site-preview/pulse-diagnosis/index.html')
old=p.read_text(encoding='utf-8')
backup=Path('output/release-audit/pulse-v18.html')
if not backup.exists(): backup.write_text(old,encoding='utf-8')
old=backup.read_text(encoding='utf-8')
d=html.fromstring(old);main=d.xpath('//main')[0]
before=len(re.sub(r'\s','',main.text_content()))
def one(x): return d.xpath(x)[0]
def settext(x,t):
 e=one(x)
 for c in list(e):e.remove(c)
 e.text=t
def cls(c):return f'//*[@class="{c}"]'
for e in main.xpath('.//figcaption'):e.getparent().remove(e)
settext('//section[contains(@class,"internal-hero")]//p[not(@class)]','從睡眠、腸胃到日常生活，綜合評估並調整治療方向。')
settext(cls('internal-intro'),'從整體狀態，了解反覆不適的原因。')
settext('//*[@id="assessment"]//p[@class="internal-intro"]','把脈不是單獨的判斷，而是和症狀、病史與生活狀態一起閱讀。')
settext('//*[@id="assessment"]//div[@class="internal-split"]/div/p','我們會把脈象、症狀與生活狀態放在一起判斷，再決定當次治療方向。')
settext(cls('internal-points')+'/li[1]','了解主要不舒服的地方')
settext(cls('internal-points')+'/li[3]','回診重新比對變化')
note=one('//*[@id="assessment"]//div[@class="internal-note"]');note.clear();note.set('class','internal-trust')
note.append(html.fragment_fromstring('<div><span class="internal-label">診療理念</span><h3>從脈學教學到診療現場</h3><a href="https://clinical-pulse.com/" target="_blank" rel="noopener noreferrer">認識臨床脈學學院</a></div>'))
note.append(html.fragment_fromstring('<div><p>連邦中醫院長張豫醫師投入脈診教學與臨床整合，將把脈與問診、舌象及病程一起評估，作為治療方向的參考。</p><p>就診時可準備主要不適發生時間、既往病史、檢查資料與目前用藥。</p></div>'))
settext('//*[@id="internal-overview"]//p[@class="internal-intro"]','常見調理需求，仍依個人狀況評估。')
settext('//*[@id="why"]//div/p','每一味藥，都依當下狀態調整。處方不是固定不變，而是隨每次回診重新修正。')
for i,t in enumerate(['依當次狀態調整藥味與比例','不同藥物可分別調整','依每次變化修正處方'],1):settext(cls('internal-benefits')+f'/dd[{i}]',t)
settext('//*[@id="dose"]//h2','處方不是越多越好，而是每一味都有理由。')
settext('//*[@id="dose"]//div/div[2]/p','實際用量會依症狀、體質、病程與濃縮倍率調整，並非每位患者固定使用相同劑量。')
e=one(cls('internal-dose-note'));e.getparent().remove(e)
for i,t in enumerate(['了解主要症狀、病史與目前用藥','依脈象、症狀與生活狀態判斷','說明健保、自費或用藥安排','依每次變化調整方向'],1):settext(cls('internal-flow')+f'/article[{i}]/p',t)
settext('//*[@id="fees"]//p[@class="internal-intro"]','從問診到追蹤，簡單透明。')
e=one('//*[@id="fees"]//p[@class="internal-note"]');e.getparent().replace(e,html.fragment_fromstring('<div class="internal-fee-note"><h3>健保與自費說明</h3><p>如需額外自費藥量，治療前會先說明原因、費用與使用方式。</p></div>'))
answers=['不是。以多味濃縮中藥組成處方，分別調整比例與劑量。','方便依當次狀態調整，不是每人使用相同處方。','不一定，依症狀、舌脈與服藥反應調整。','不是。僅適用部分個案，克數不代表療效，用量須由醫師評估。','依藥袋指示服用，勿重複加服或自行加量。','請告知完整用藥資訊，由醫師評估；勿自行停藥。']
for e,t in zip(d.xpath(cls('internal-answer')),answers):e.text=t
for e in d.xpath('//link[contains(@href,"internal-editorial.css")]'):e.set('href','/assets/internal-editorial.css?v=19')
schema=one('//script[@type="application/ld+json"]');data=json.loads(schema.text)
for item in data['@graph']:
 if item['@type']=='FAQPage':
  for q,a in zip(item['mainEntity'],answers):q['acceptedAnswer']['text']=a
schema.text=json.dumps(data,ensure_ascii=False)
after=len(re.sub(r'\s','',main.text_content()))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
print(json.dumps({'before':before,'after':after,'reduction_percent':round((1-after/before)*100,1),'images':len(main.xpath('.//img')),'captions':len(main.xpath('.//figcaption'))}))
# Update existing tokens and type/spacing rules rather than adding another stylesheet.
c=Path('output/site-preview/assets/internal-editorial.css');s=c.read_text(encoding='utf-8')
for a,b in [('4a3428','4a3024'),('8c6b55','936b4e'),('ddd0c3','ddd0c1'),('f7f2ea','f6f1e8'),('ede1d3','e9d8c3'),('font:16px/1.85','font:17px/1.75'),('padding:96px 0','padding:72px 0'),('font-size:32px','font-size:36px'),('font-size:21px','font-size:24px'),('gap:64px','gap:56px'),('padding:68px 0','padding:56px 0'),('padding:80px 0','padding:64px 0'),('padding:72px 0}.internal-actions','padding:56px 0}.internal-actions')]:s=s.replace(a,b)
s=re.sub(r'\.internal-page figcaption\{[^}]+\}','',s)
s=re.sub(r'\.internal-dose-note\{[^}]+\}','',s)
s=s.replace('.internal-btn:hover{opacity:.85}','')
c.write_text(s,encoding='utf-8')
