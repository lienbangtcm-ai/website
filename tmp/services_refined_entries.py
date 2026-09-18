from lxml import html
from clinic_icon_system import svg
from pathlib import Path
def entry(key,title,words,url=None):
 tag='a' if url else 'div'
 visual=svg(key)
 image=Path(__file__).resolve().parents[1]/f'output/site-preview/assets/service-reference/{key}.png'
 if image.exists():
  visual=f'<img class="ls-illustration" src="/assets/service-reference/{key}.png" alt="" loading="lazy" decoding="async" style="object-fit:contain;border-radius:14px">'
 arrow='<span class="ls-entry-arrow" aria-hidden="true">→</span>' if url else ''
 return f'<{tag} class="ls-entry"'+(f' href="{url}"' if url else '')+'>'+visual+f'<div><h3>{title}</h3><p>{words}</p></div>'+arrow+f'</{tag}>'
def simplify(doc):
 def el(id):return doc.get_element_by_id(id)
 def serialize(node):return html.tostring(node,encoding='unicode')
 def index(id):return serialize(el(id).xpath('.//*[@class="ls-index"]')[0])
 motif='<svg class="ls-motif" viewBox="0 0 300 150" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><path d="M18 102c30 0 34-24 58-24 27 0 31 31 59 31 27 0 33-40 63-40 25 0 28 20 54 20 16 0 23-8 30-16"/><path d="M18 115c32 0 35-22 58-22 25 0 31 29 59 29 30 0 35-39 63-39 24 0 29 19 54 19 13 0 23-5 30-13"/><circle cx="77" cy="78" r="4"/><circle cx="135" cy="109" r="4"/><path d="M208 31c8-9 18-7 22 3-4 8-12 13-22 12-4-5-4-10 0-15Z"/><path d="M211 43c11-2 18-5 24-11M221 47v22"/></svg>'
 motif=(Path(__file__).resolve().parents[1]/'output/services-editorial/hero-consultation.svg').read_text(encoding='utf-8')
 body='<header class="ls-hero"><div class="ls-shell ls-hero-layout"><h1>治療服務</h1></div></header>'
 body+='<nav class="ls-nav" aria-label="治療服務段落導覽"><div class="ls-shell"><a href="#internal">中醫內科</a><a href="#orthopedics">針灸傷科</a><a href="#self-pay">自費診療</a><a href="#approach">初次就診</a></div></nav>'
 groups=[('internal','中醫內科','從脈象、問診與身體狀態理解目前需求。',[('pulse','把脈評估','脈診・問診・舌診','/pulse-diagnosis/#assessment'),('herbs','單味藥組方','藥材・比例・劑量','/pulse-diagnosis/#why'),('care','生活照護','作息・飲食・追蹤','/pulse-diagnosis/#assessment')]),('orthopedics','針灸傷科','從疼痛位置、活動表現與組織狀態進行評估。',[('movement','疼痛與活動評估','疼痛・活動度・功能','/acupuncture/#process'),('acupuncture','一般針灸／不留針','穴位・局部・筋膜','/acupuncture/'),('integration','中醫 × 物理治療','活動度・肌力・動作','/acupuncture-physical-therapy/')])]
 groups[0][3][2]=('care','生活照護','作息・飲食・追蹤')
 groups[1][3][1]=('acupuncture','針灸治療','穴位・局部・筋膜','/acupuncture/')
 for id,title,description,items in groups:
  body+=f'<section class="ls-section ls-clinical" id="{id}"><div class="ls-shell"><div class="ls-service-panel"><div class="ls-section-intro"><span class="ls-section-number">{"01" if id=="internal" else "02"}</span><h2>'+title+'</h2><p>'+description+'</p></div><div class="ls-service-rows">'+''.join(entry(*x) for x in items)+'</div></div><div class="ls-symptoms"><h3>'+('常見診療項目' if id=='internal' else '常見疼痛項目')+'</h3>'+index(id)+'</div></div></section>'
 pay=[('acupotomy','針刀','沾黏・纖維化・活動受限','/針刀/'),('fsn','浮針','肌肉・筋膜・疼痛','/浮針/'),('facial','美顏針','臉部・循環・張力','/美顏針/'),('embedding','穴位埋線','穴位・體態・調理','/埋線/')]
 body+='<section class="ls-section ls-clinical" id="self-pay"><div class="ls-shell"><div class="ls-service-panel"><div class="ls-section-intro"><span class="ls-section-number">03</span><h2>自費診療</h2><p>經醫師評估並說明方式、注意事項與費用後，再決定是否安排。</p></div><div class="ls-service-rows ls-service-rows-pay">'+''.join(entry(*x) for x in pay)+'</div></div></div></section>'
 body+='<section class="ls-section ls-flow" id="approach"><div class="ls-shell"><h2>就診流程</h2><div class="ls-flow-grid">'+entry('booking','預約掛號','確認門診時間與預約方式','#appointment')+entry('arrival','到院報到','攜帶證件，完成初診資料')+entry('consult','醫師看診','說明不適，討論治療安排')+'</div></div></section>'
 prep=[('symptom','主要不適','記下不適多久、何時加重。'),('medicine','目前用藥','帶藥單或藥袋，也請告知保健品。'),('reports','相關檢查','若有近期報告或影像，可一併帶來。'),('history','病史資料','告知過敏、既往病史及是否懷孕。')]
 body+='<section class="ls-section ls-soft" id="visit"><div class="ls-shell"><h2>初診準備</h2><div class="ls-prep-grid">'+''.join(entry(*x) for x in prep)+'</div></div></section>'
 body+='<section class="ls-section ls-cta" id="appointment"><div class="ls-shell"><h2>預約與門診資訊</h2><div class="ls-cta-actions"><a class="ls-button" href="https://lin.ee/NMa1es5" target="_blank" rel="noopener noreferrer">LINE 預約</a><a href="https://lienbangtcm.tw/support/">查看門診時間 <span aria-hidden="true">→</span></a><a href="tel:+886225795059">02-2579-5059</a></div></div></section>'
 for child in list(doc):doc.remove(child)
 for child in html.fragments_fromstring(body):doc.append(child)
 # One compact page header with navigation, followed directly by service content.
 header=doc.find('header')
 nav=doc.find('nav')
 links=nav.find('div')
 for link in list(links):nav.append(link)
 nav.remove(links)
 header.find('div').append(nav)
 for number in doc.xpath('.//*[@class="ls-section-number"]'):
  number.getparent().remove(number)
