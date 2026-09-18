from pathlib import Path
import re, html

root = Path(__file__).resolve().parents[1]
template = (root/'output/symptom-article-demo/gerd-illustrated.html').read_text(encoding='utf-8')
md = (root/'output/symptom-article-drafts/insomnia.md').read_text(encoding='utf-8')
md = md.replace('大部分患者的入睡時間、夜醒情形、睡眠穩定度與白天精神可以獲得良好改善。', '治療目標是改善入睡困難、夜醒與白天精神，實際反應需透過回診追蹤，不能預先保證效果。')
md = md.replace('經過完整辨證並配合作息調整，常能取得較好的改善。', '可由醫師評估中醫治療是否適合作為整體照護的一部分，並追蹤睡眠日誌及白天功能。針灸與中藥治療失眠的研究仍有品質與一致性限制，不能據此推定每位患者都會有效。')
md = md.replace('## 可以先記錄什麼？', '## 哪些人比較容易出現睡眠困擾？\n\n作息不固定、輪班、長期承受工作或照顧壓力，或伴隨疼痛、更年期不適與情緒困擾的人，可能較容易出現睡眠問題。有這些因素不代表一定罹患失眠，仍需一起評估睡眠機會與白天功能。\n\n## 可以先記錄什麼？')
md = md.replace('## 日常照護', '### 慢性失眠的整體照護\n\n慢性失眠通常優先考慮失眠認知行為治療（CBT-I），由受過訓練的專業人員協助調整睡眠行為與對睡眠的擔憂。一般作息建議不能完全取代 CBT-I；需要時可與睡眠或身心相關專科共同安排。\n\n## 日常照護')
parts = re.split(r'^## ', md, flags=re.M)
intro = parts[0].split('\n\n',1)[1].strip()
sections = []
for part in parts[1:]:
    title, content = part.split('\n',1)
    if title == '預約與門診資訊': continue
    sections.append((title,content.strip()))

def render(content):
    out=[]
    for block in content.split('\n\n'):
        if block.startswith('### '): out.append('<h3>'+html.escape(block[4:])+'</h3>')
        elif block.startswith('- '): out.append('<ul>'+''.join('<li>'+html.escape(x[2:])+'</li>' for x in block.splitlines())+'</ul>')
        else: out.append('<p>'+html.escape(block)+'</p>')
    return '\n'.join(out)

head=template.split('<body>')[0].replace('胃食道逆流｜','失眠｜').replace('胃食道逆流的常見症狀、中醫辨證與連邦中醫治療方式。','失眠、淺眠與半夜醒來的常見原因、睡眠紀錄、中醫辨證與治療評估，了解日常照護與需要就醫的情況。')
head=head.replace('</style>', '\n.lb-section{scroll-margin-top:84px}.lb-narrow{width:min(1040px,calc(100% - 48px))}.lb-section h3{margin-top:30px}.lb-lead{max-width:850px}.lb-nav a:focus-visible,.lb-btn:focus-visible,summary:focus-visible{outline:3px solid #b48b62;outline-offset:4px}\n</style>')
out=[head,'<body><article class="lb-article">', '<header class="lb-hero"><div class="lb-shell lb-hero-grid"><h1>失眠</h1><p class="lb-lead">'+html.escape(intro)+'</p></div></header>']
out.append('<nav class="lb-nav" aria-label="文章段落導覽"><div class="lb-nav-inner">'+''.join(f'<a href="#section-{i}">{html.escape(t)}</a>' for i,(t,c) in enumerate(sections))+'</div></nav>')
for i,(title,content) in enumerate(sections):
    style=' lb-section--soft' if i%3==1 else (' lb-section--mint' if i%3==2 else '')
    body=render(content)
    if title=='常見問題':
        body='<div class="lb-faq">'+''.join('<details><summary>'+html.escape(x.split('\n',1)[0])+'</summary><div class="lb-answer">'+render(x.split('\n',1)[1].strip())+'</div></details>' for x in content.split('### ')[1:])+'</div>'
    out.append(f'<section class="lb-section{style}" id="section-{i}"><div class="lb-shell lb-narrow"><h2>{html.escape(title)}</h2>{body}</div></section>')
cta=template[template.index('  <section class="lb-cta">'):]
cta=cta.replace('https://lin.ee/UWWKmse','https://lin.ee/NMa1es5').replace('讓專業團隊成為您的健康後盾','🏥 讓專業團隊成為您的健康後盾').replace('可先準備近期症狀紀錄、用藥及檢查資料，再由醫師安排問診與脈診辨證。','就診前可先準備一至兩週睡眠紀錄，以及目前使用的處方藥、成藥與保健品，由醫師安排問診與脈診辨證。')
out.append(cta)
dest=root/'output/insomnia'
dest.mkdir(exist_ok=True)
(dest/'insomnia-review.html').write_text('\n'.join(out),encoding='utf-8')
(dest/'REVIEW.md').write_text('''# 失眠文章製作紀錄

- 版型來源：output/symptom-article-demo/gerd-illustrated.html（2026-09-01 本機版本）。
- 內容來源：output/symptom-article-drafts/insomnia.md；依統一架構補齊族群與慢性失眠照護。
- 本次為無圖審閱版：失眠初稿沒有指定圖片數量或插槽，未生成圖片。
- 胃食道逆流依使用者告知列為完成；本次未變更該檔案，也未發布新文章。
- 移除缺乏依據的普遍療效宣稱，保留辨證、單味藥組方與針灸評估內容。尚無確認案例，不顯示案例段落。
- LINE 採已安裝技能的固定網址 NMa1es5；舊胃食道逆流模板使用 UWWKmse，兩者有差異，正式發布前須核對院方預約入口。
- 待續初稿：肩頸痛、腰背痛。

醫療查核來源（編輯用，不另增文章參考資料區塊）：
- https://www.nhlbi.nih.gov/health/insomnia/treatment — CBT-I 與日常照護。
- https://www.nccih.nih.gov/health/sleep-disorders-and-complementary-health-approaches — 輔助療法的證據限制。
''',encoding='utf-8')
print(dest/'insomnia-review.html')
