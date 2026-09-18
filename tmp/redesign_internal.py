from pathlib import Path
import re
from PIL import Image

root=Path('output/site-preview')
page=root/'pulse-diagnosis/index.html'
old=page.read_text(encoding='utf-8')
backup=Path('output/release-audit/pulse-before-editorial.html')
if not backup.exists(): backup.write_text(old,encoding='utf-8')
assets=root/'assets/internal-editorial'
assets.mkdir(exist_ok=True)
im=Image.open(r'C:\Users\yutin\Downloads\ChatGPT Image 2026年9月13日 下午08_32_21.png')
w,h=im.size
for name,box in {'pulse':(0,0,.494,.492),'consult':(.506,0,1,.492),'herbs':(0,.507,.494,1)}.items():
    im.crop(tuple(round(v*(w if i%2==0 else h)) for i,v in enumerate(box))).save(assets/f'{name}.webp',quality=92)
faq=re.search(r'<div class="lb-faq">(.*?)\n      </div>',old,re.S).group(1)
faq=faq.replace('lb-faq__answer','internal-answer')
def photo(name,alt):
    return f'<figure><img src="/assets/internal-editorial/{name}.webp" alt="{alt}（情境示意）" width="760" height="504" decoding="async" loading="{ "eager" if name=="consult" else "lazy"}"><figcaption>情境示意，非診所實景</figcaption></figure>'
def cards(items,cls):
    return f'<div class="{cls}">'+''.join(f'<article><h3>{a}</h3><p>{b}</p></article>' for a,b in items)+'</div>'
button='<a class="internal-btn" href="https://lin.ee/UWWKmse" target="_blank" rel="noopener noreferrer">LINE 預約諮詢</a>'
main=f'''<main class="internal-page">
<section class="internal-section internal-hero"><div class="internal-shell internal-split"><div><h1>中醫內科</h1><p class="internal-subtitle">從脈象、症狀與生活狀態，<br>理解身體現在發生什麼。</p><p>不只處理單一症狀，我們會一起了解睡眠、腸胃、精神狀態、生理週期與日常生活，依每次身體狀態調整治療方向。</p><div class="internal-actions">{button}<a class="internal-btn secondary" href="https://lienbangtcm.tw/support/" target="_blank" rel="noopener noreferrer">查看門診時間</a></div></div>{photo('consult','醫師與患者討論身體狀況')}</div></section>
<nav class="internal-nav internal-shell" aria-label="中醫內科頁內導覽"><a href="#assessment">把脈評估</a><a href="#why">單味藥組方</a><a href="#internal-overview">常見調理</a><a href="#fees">健保與費用</a></nav>
<section class="internal-section"><div class="internal-shell"><h2>你可能正遇到這些狀況</h2><p class="internal-intro">很多內科的不舒服，不一定只來自單一部位。我們會從整體狀態一起評估。</p>{cards([('睡了還是很累','容易失眠、淺眠或半夜醒來'),('腸胃總是不舒服','胃脹、消化不良、排便不穩定'),('生理週期反覆不穩','經痛、週期不規律、更年期不適'),('常常頭暈、心悸','精神不集中，影響日常生活'),('檢查正常，卻一直不舒服','想進一步了解身體的狀態'),('感冒後恢復很慢','反覆咳嗽或容易生病')],'internal-situations')}</div></section>
<section class="internal-section" id="assessment"><div class="internal-shell"><h2>我們怎麼看你的問題</h2><p class="internal-intro">把脈不是單獨存在的一個判斷，而是與症狀、病史與生活狀態一起閱讀。</p><div class="internal-split">{photo('pulse','手指輕按手腕進行脈診')}<div><h3>不只看一個症狀</h3><p>我們會把脈象、睡眠、飲食、排便、精神狀態、生理週期與既往病史放在一起判斷，再決定當次的治療方向。</p><ol class="internal-points"><li>先了解主要不舒服的地方</li><li>用脈象補充身體狀態的線索</li><li>每次回診重新比對變化</li></ol></div></div><div class="internal-note"><h3>從脈學教學到連邦的診療理念</h3><p>連邦中醫診所院長張豫醫師創辦臨床脈學學院，投入脈診教學與臨床整合。連邦也重視把脈辨證：細察脈象，並結合問診、舌象與病程，作為評估與處方安排的依據。</p><a href="https://clinical-pulse.com/" target="_blank" rel="noopener noreferrer">認識臨床脈學學院</a><p>就診時可準備主要不適與發生時間、既往病史、檢查資料及目前中西藥與保健品資訊，也歡迎記下這次最想詢問的問題。</p></div></div></section>
<section class="internal-section" id="internal-overview"><div class="internal-shell"><h2>常見調理方向</h2><p class="internal-intro">以下是門診中常見的內科調理需求，實際仍會依每個人的狀況評估。</p>{cards([('腸胃與消化','胃脹、胃食道逆流、消化不良、排便異常'),('睡眠與自律神經','難入睡、淺眠、容易醒、心悸'),('婦科與生理週期','經痛、月經不規律、更年期不適'),('疲勞與體質調理','容易累、怕冷、反覆不舒服'),('呼吸與過敏','鼻過敏、咳嗽、感冒後恢復慢'),('兒童體質','食慾、睡眠、容易反覆感冒')],'internal-cards')}</div></section>
<section class="internal-section" id="why"><div class="internal-shell internal-split" id="process">{photo('herbs','分別陳列的中藥材')}<div><span class="internal-label">單味藥組方</span><h2>為什麼我們使用<br>單味藥組方？</h2><p>每一味藥，都可以依照當下的狀態調整比例與劑量。醫師能更清楚掌握處方結構，並依每次回診的變化重新調整，而不是固定使用同一張成方。</p><dl class="internal-benefits"><dt>配伍更彈性</dt><dd>依每次狀態調整藥味與比例</dd><dt>劑量更容易掌握</dt><dd>不同藥物可分別調整，不必整包一起增加</dd><dt>適合持續追蹤</dt><dd>回診時依症狀與脈象變化重新修正</dd></dl></div></div></section>
<section class="internal-section internal-dose-section" id="dose"><div class="internal-shell internal-dose"><div><div class="internal-number">18–25g</div><p>部分個案的每日濃縮粉總量</p></div><div><h2>處方不是藥味越多、<br>總量越高越好</h2><p>實際使用量會依每個人的症狀、體質與治療階段調整。重點不是單純增加藥量，而是讓每一味藥都有清楚的角色。</p><p class="internal-dose-note">18–25g 並非每位患者的固定劑量，也不代表劑量越高效果越好。實際用量須考量藥材種類、濃縮倍率、體質、病程、年齡、既往用藥與服用反應，由醫師評估後決定。</p></div></div></section>
<section class="internal-section" id="fees"><div class="internal-shell"><h2>看診方式</h2><p class="internal-intro">從第一次問診到後續追蹤，流程會保持簡單透明。</p>{cards([('掛號與問診','先了解主要症狀、病史與目前用藥。'),('把脈與整體評估','依脈象、症狀與生活狀態綜合判斷。'),('確認治療方式','依需求說明健保、自費或用藥安排。'),('回診追蹤','依每次身體變化調整處方與方向。')],'internal-flow')}<p class="internal-note">實際健保與自費項目，會由現場人員於治療前說明。若評估需要額外自費藥量，會先說明原因、每日總量與金額，經患者了解並同意後安排。藥袋會清楚標示服用方式，避免重複服用。</p></div></section>
<section class="internal-section" id="faq"><div class="internal-shell internal-faq"><h2>常見問題</h2>{faq}</div></section>
<section class="internal-ending"><div class="internal-shell"><h2>不知道自己的狀況適不適合中醫內科？</h2><p>可以先把目前主要症狀告訴我們，<br>我們會協助安排合適的門診。</p>{button}</div></section>
</main>'''
new=re.sub(r'<style>.*?</style>','',old,count=1,flags=re.S)
new=re.sub(r'<main class="lb-herb">.*?</main>',lambda m:main,new,count=1,flags=re.S)
new=re.sub(r'<a class="lb-float-line".*?</a>','',new,flags=re.S)
new=new.replace('</body>','<link rel="stylesheet" href="/assets/internal-editorial.css?v=18"></body>')
page.write_text(new,encoding='utf-8')
print('Updated existing pulse page; 3 supplied image crops; preserved 6 FAQ entries.')
