from pathlib import Path
from lxml import html
import re,json,shutil
R=Path(__file__).resolve().parents[1];D=R/'output/services-editorial'
old=html.fromstring((D/'services-before.html').read_text(encoding='utf-8'))
def inner(el):return ''.join(html.tostring(x,encoding='unicode') for x in el)
def figure(key,alt,hero=False):
 return f'<figure><picture><source srcset="/services/images/{key}.webp" type="image/webp"><img src="/services/images/{key}.jpg" alt="{alt}（情境示意）" width="1536" height="1024" loading="{"eager" if hero else "lazy"}" decoding="async"'+(' fetchpriority="high"' if hero else '')+f'></picture><figcaption>AI 情境示意｜{alt}，非診所實拍或實際處置紀錄。</figcaption></figure>'
def section(id):return old.get_element_by_id(id)
def services(el):
 cards=el.xpath('.//div[contains(@class,"sv-grid")][1]/article')
 out='<div class="ls-services">'
 for i,c in enumerate(cards,1):out+=f'<article class="ls-service"><span class="ls-service-number">0{i}</span>'+inner(c)+'</article>'
 return out+'</div>'
def index(el):
 anchors=el.xpath('.//div[contains(@class,"sv-grid-four")]//a')
 return '<div class="ls-index">'+''.join(f'<a href="{a.get("href")}">{a.text_content().replace("→","").strip()}<span aria-hidden="true">→</span></a>' for a in anchors)+'</div>'
main='''<main class="lb-services"><header class="ls-hero"><div class="ls-shell ls-hero-copy"><p class="ls-eyebrow">LIENBANG MEDICAL SERVICES</p><h1>治療服務</h1><p class="ls-lead">從理解身體開始，<br>找到適合當下狀況的照護方式。</p></div>'''+figure('hero','問診與醫病溝通',True)+'''</header><nav class="ls-nav" aria-label="治療服務段落導覽"><div class="ls-shell ls-nav-inner"><a href="#approach">如何看診</a><a href="#internal">中醫內科</a><a href="#orthopedics">針灸傷科</a><a href="#self-pay">自費診療</a></div></nav>
<section class="ls-section" id="approach"><div class="ls-shell"><p class="ls-eyebrow">連邦的診療方式</p><h2>我們會做什麼？</h2><p class="ls-lead">從你最在意的不適開始，整理症狀、病程與生活狀況。醫師依評估討論治療選項，並在回診時檢視反應與調整安排。</p><div class="ls-steps">'''
for i,c in enumerate(section('approach').xpath('.//article'),1):
 title=c.find('h3').text_content()[3:];main+=f'<article class="ls-step"><span class="ls-number" aria-hidden="true">0{i}</span><h3>{title}</h3>'+html.tostring(c.find('p'),encoding='unicode')+'</article>'
main+='</div></div></section>'
for id,key,alt,rev in [('internal','pulse','把脈評估',False),('orthopedics','movement','肩部活動評估',True)]:
 el=section(id);copy=el.xpath('.//div[@class="sv-banner"]/div')[0]
 copyhtml=inner(copy).replace('sv-label','ls-eyebrow')
 main+=f'<section class="ls-section" id="{id}"><div class="ls-shell"><div class="ls-feature'+(' ls-feature-reverse' if rev else '')+'">'+figure(key,alt)+'<div class="ls-feature-copy">'+copyhtml+'</div></div><h3>我們會做什麼</h3>'+services(el)+'<h3>常見診療項目</h3>'+index(el)+'</div></section>'
main+='''<section class="ls-section ls-soft" id="integration"><div class="ls-shell ls-brand"><h2>疼痛改善之後，<br>還要讓身體重新會動。</h2><div><p>部分疼痛與活動限制除了局部治療，也可能與關節活動度、肌力、姿勢或動作控制有關。需要時，可進一步安排物理治療評估與訓練。</p><a href="/acupuncture-physical-therapy/">了解中醫 × 物理治療整合 →</a></div></div></section>
<section class="ls-section" id="self-pay"><div class="ls-shell"><p class="ls-eyebrow">03 / 自費診療</p><h2>依需求討論進一步的診療選項</h2><p>先經醫師評估，確認適用情況、處置方式、注意事項與費用後，再決定是否安排。</p><div class="ls-treatment-grid">'''
for key,c,alt in zip(['acupotomy','fsn','facial','embedding'],section('self-pay').xpath('.//article'),['肩部模型與處置說明','前臂評估','臉部評估','埋線前需求諮詢']):
 main+='<article class="ls-treatment">'+figure(key,alt)+inner(c)+'</article>'
main+='''</div></div></section><section class="ls-section ls-soft" id="visit"><div class="ls-shell ls-visit"><h2>第一次來診，<br>可以這樣準備。</h2><ol class="ls-preparation">'''
for i,li in enumerate(section('visit').xpath('.//li'),1):main+=f'<li><span aria-hidden="true">0{i}</span><div>{li.text_content()}</div></li>'
main+='''</ol></div></section><section class="ls-section ls-cta" id="appointment"><div class="ls-shell"><h2>一起找到適合目前狀況的照護方向</h2><p>不確定該預約哪一項？<br>先告訴我們你現在最主要的困擾。</p><div class="ls-cta-actions"><a class="ls-button" href="https://lin.ee/NMa1es5" target="_blank" rel="noopener noreferrer">LINE 預約諮詢</a><a href="https://lienbangtcm.tw/support/">查看門診時間 →</a></div><a class="ls-phone" href="tel:+886225795059">02-2579-5059</a></div></section></main>'''
docmain=html.fromstring(main)
# Keep the service information; remove generated scenes and decorative labels.
for node in docmain.xpath('.//*[@class="ls-eyebrow"] | .//*[@class="ls-number"] | .//*[@class="ls-service-number"]'):
 node.getparent().remove(node)
for id,title in [('internal','中醫內科'),('orthopedics','針灸傷科'),('integration','中醫與物理治療整合'),('self-pay','自費診療'),('visit','初診準備'),('appointment','預約與門診資訊')]:
 heading=docmain.get_element_by_id(id).find('.//h2');heading.clear();heading.text=title
lead=docmain.xpath('.//*[contains(@class,"ls-hero-copy")]/*[@class="ls-lead"]')[0]
lead.clear();lead.set('class','ls-lead');lead.text='先了解你的症狀與病程，再決定適合的治療方式。'
for node in docmain.xpath('.//*[@class="ls-feature ls-feature-reverse"]'):node.set('class','ls-feature')
from services_refined_entries import simplify
simplify(docmain)
main=html.tostring(docmain,encoding='unicode')
schema=old.xpath('//script[@type="application/ld+json"]')[0]
css=(D/'services-refined.css').read_text(encoding='utf-8')
source='<style>\n'+css+'\n</style>\n'+main+html.tostring(schema,encoding='unicode')
(R/'output/services-page.html').write_text(source,encoding='utf-8')
preview=html.fromstring((R/'output/site-preview/services/index.html').read_text(encoding='utf-8'))
header=html.tostring(preview.xpath('//header[contains(@class,"preview-header")]')[0],encoding='unicode')
doc='<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>治療服務｜連邦中醫診所</title><meta name="description" content="了解連邦中醫把脈辨證、單味藥組方、針灸傷科、中醫整合物理治療及自費診療，查閱常見症狀與初診準備。"><link rel="stylesheet" href="/assets/site-shared.css?v=2"></head><body>'+header+source+'</body></html>'
(R/'output/site-preview/services/index.html').write_text(doc,encoding='utf-8')
(D/'services-preview.html').write_text(doc,encoding='utf-8')
print('New stylesheet and semantic page built; legacy styles and floating CTA removed')
