from pathlib import Path
from lxml import html
p=Path('output/site-preview/index.html');s=p.read_text(encoding='utf-8');b=Path('output/release-audit/home-before-v22.html')
if not b.exists():b.write_text(s,encoding='utf-8')
d=html.fromstring(s);old=d.xpath('//main')[0]
info=old.xpath('.//*[@id="clinic-info"]')[0]
line='https://lin.ee/UWWKmse'
def btn(url,label):return f'<a class="hr-btn" href="{url}">{label}</a>'
services=[('中醫內科','脈診辨證、單味藥組方與日常調理','/pulse-diagnosis/','pulse'),('針灸傷科','疼痛、筋膜與活動受限的評估與處理','/acupuncture/','acupuncture'),('中醫 × 物理治療','協助理解症狀來源與後續方向','/acupuncture-physical-therapy/','integration'),('自費診療','針刀、浮針、美顏針與其他自費項目','/services/#self-pay','facial')]
cards=''.join(f'<a class="hr-service" href="{u}"><div><h3>{t}</h3><p>{desc}</p><span>了解更多 →</span></div><img src="/assets/service-reference/{im}.png" alt="" loading="lazy"></a>' for t,desc,u,im in services)
symptoms=[('gerd','胃食道逆流'),('cough','咳嗽'),('insomnia','失眠'),('allergic-rhinitis','鼻過敏'),('neck-shoulder-pain','肩頸痛'),('low-back-pain','腰背痛'),('menstrual-pain','經痛'),('fatigue','疲倦')]
sc=''.join(f'<a href="/symptoms/{slug}/"><img src="/assets/illustrations/reference-crops/{slug}.png" alt="" loading="lazy"><h3>{title}</h3></a>' for slug,title in symptoms)
new=html.fragment_fromstring(f'''<main class="home-reference"><section class="hr-hero"><div class="hr-wrap hr-hero-inner"><div class="hr-hero-copy"><span class="hr-label">連邦中醫診所</span><h1>把脈、問診與整體評估，<br>找到適合你的調理方向</h1><p>提供中醫內科、針灸傷科、中醫 × 物理治療與自費診療。<br>先從身體現在的狀態開始理解。</p><div class="hr-actions">{btn(line,'LINE 預約 →')}{btn('#clinic-info','門診與交通')}</div></div><img class="hr-real-photo" src="/assets/clinic-photos/reception.jpg" alt="連邦中醫診所實際櫃台與品牌牆" fetchpriority="high"></div></section><section class="hr-section"><div class="hr-wrap"><div class="hr-heading"><h2>治療服務</h2><p>從整體出發，提供適合你的治療方案。</p><a href="/services/">查看所有服務 →</a></div><div class="hr-services">{cards}</div></div></section><section class="hr-section" id="common-symptoms"><div class="hr-wrap"><div class="hr-heading"><h2>常見症狀</h2><p>從常見困擾找到適合你的入口。</p><a href="/symptoms/">查看全部症狀 →</a></div><div class="hr-symptoms">{sc}</div></div></section><section class="hr-about"><div class="hr-wrap hr-about-inner"><div><h2>認識連邦</h2><p>連邦重視問診、把脈與整體評估，協助患者理解目前的狀態，討論合適的照護方向。</p>{btn('/about-lienbang/','關於連邦 →')}</div><img src="/assets/clinic-photos/hallway.webp" alt="連邦中醫診所實際診間與候診走廊" loading="lazy"></div></section></main>''')
old.getparent().replace(old,new);new.append(info)
# Preserve actual contact data and navigation; do not copy the mockup's schedule/map.
for e in info.xpath('.//h2'):
 if e.text=='院所資訊':e.text='門診與交通'
for e in d.xpath('//a[@class="lb-float-line"]'):e.getparent().remove(e)
d.xpath('//body')[0].append(html.fragment_fromstring('<link rel="stylesheet" href="/assets/home-reference.css?v=22">'))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
