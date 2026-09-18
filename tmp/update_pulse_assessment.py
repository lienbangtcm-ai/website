from pathlib import Path
import re
block='''<section class="lb-section" id="assessment">
  <div class="lb-shell">
    <h2>把脈評估</h2>
    <p class="lb-lead">把脈是中醫診察的一環。醫師將指下感受與問診、舌象及病程一起判讀，了解當次狀況，再討論照護方向。</p>
    <div class="lb-cards">
      <article class="lb-card"><span class="lb-card__no">01</span><h3>有步驟地觀察</h3><p>從手部姿勢、取脈位置到按壓力道，依序觀察脈象，讓前後比較有一致的基礎。</p></article>
      <article class="lb-card"><span class="lb-card__no">02</span><h3>描述指下感受</h3><p>整理脈的位置、快慢、形態與力量等特徵，進一步理解不同特徵的組合。</p></article>
      <article class="lb-card"><span class="lb-card__no">03</span><h3>與其他資訊核對</h3><p>脈象需與症狀、舌象和病程互相參照；遇到不一致的資訊，還需要補問與釐清。</p></article>
    </div>
    <div style="margin-top:36px;padding-top:28px;border-top:1px solid var(--lb-line)">
      <h3>從把脈到整體評估</h3>
      <p>臨床脈學學院重視操作練習與臨床整合。這份介紹參考其教學架構，將重點轉為就診時容易理解的說明；脈象不能脫離其他診察資料單獨作結論。</p>
      <a href="https://clinical-pulse.com/" target="_blank" rel="noopener noreferrer">認識臨床脈學學院 →</a>
    </div>
    <h3 style="margin-top:36px">就診時可以準備哪些資訊？</h3>
    <ul class="lb-checks">
      <li>主要不適及發生時間</li><li>睡眠、腸胃、精神、經期與生活狀態</li><li>既往病史與檢查資料</li><li>目前使用的中藥、西藥及保健品</li><li>服用後的變化與不適</li><li>本次最想詢問的問題</li>
    </ul>
    <div class="lb-actions"><a class="lb-btn lb-btn--gold" href="https://lin.ee/NMa1es5" target="_blank" rel="noopener noreferrer">立即預約評估 (LINE)</a><a class="lb-btn" href="#why">接著了解單味藥組方 →</a></div>
  </div>
</section>'''
for p in [Path('output/pulse-diagnosis/pulse-diagnosis-final.html'),Path('output/site-preview/pulse-diagnosis/index.html')]:
 s=p.read_text(encoding='utf-8')
 s,n=re.subn(r'<section class="lb-section" id="assessment">.*?</section>',block,s,flags=re.S)
 assert n==1
 s=s.replace('連邦中醫的處方設計，從當次辨證與單味藥材開始。醫師綜合問診、脈象、舌象、症狀與病程，逐味選擇需要的藥材，並安排每一味藥在處方中的角色、比例與劑量。','中醫內科從把脈評估與完整問診開始，綜合舌象、症狀與病程了解當次狀況。需要用藥時，再依辨證逐味安排藥材、比例與劑量。')
 s=s.replace('<a class="lb-btn lb-btn--line" href="#why">了解逐味組方</a>','<a class="lb-btn lb-btn--line" href="#assessment">了解把脈評估</a>')
 p.write_text(s,encoding='utf-8')
print('Updated assessment in source and preview')
