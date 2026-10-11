from pathlib import Path
import re,json
root=Path('output/site-preview')
config={
'frozen-shoulder':('五十肩','穿衣要慢慢來，手伸不到背後，連翻身也被肩痛打斷？','抬手、外轉與手伸到背後','疼痛與僵硬對穿衣、梳頭及睡眠的影響',['抬手與外轉','穿衣與手伸背後','夜間疼痛與睡眠']),
'neck-shoulder-pain':('肩頸痛','工作一整天肩頸越來越緊，轉頭卡住，休息後又再痛？','轉頭、抬手與工作動作','頸部、肩胛活動與手臂麻木或無力的情況',['轉頭與頸部活動','肩胛與上背感受','工作與日常動作']),
'low-back-pain':('腰背痛','坐久站起來腰就痛，彎腰拿東西、翻身都要特別小心？','彎腰、起身與走路','腰背動作、日常負荷與是否伴隨腿部症狀',['坐站與翻身','彎腰與搬提','走路與日常活動']),
'sciatica':('坐骨痛','痛從臀部一路延伸到腿，坐也不舒服，走路又麻又痛？','腿痛、腰髖活動與行走','疼痛路徑、麻木、肌力與神經相關表現',['腿痛與麻木範圍','坐站與行走','肌力與感覺變化']),
'knee-pain':('膝痛','上下樓先想哪隻腳出力，蹲下或站起來總被膝痛提醒？','走路、蹲起與上下樓','疼痛位置、腫脹、穩定度與下肢動作',['走路與承重','蹲下與起身','上下樓功能']),
'tennis-elbow':('網球肘','沒打網球，提水壺、擰毛巾，甚至拿杯子卻讓手肘痛？','握、提與扭轉動作','手肘壓痛、握力、前臂活動與工作負荷',['握力與拿杯子','提物與扭轉','工作與運動負荷']),
'de-quervain':('媽媽手','抱小孩、提袋子或開瓶蓋時，拇指側手腕總是痛？','拇指活動、握提與抱提動作','肌腱滑動、手腕活動與日常手部使用情況',['拇指與手腕活動','握提與拿取物品','抱提與工作動作']),
'plantar-heel-pain':('足底痛','早上下床第一步就刺痛，站久、走遠又開始痛？','第一步痛與站走功能','足底痛點、足踝活動、小腿張力與鞋具負荷',['起床與久坐後起步','站立與走路','運動與鞋具負荷'])}
for folder in [root/'symptoms',root/'dist/symptoms']:
 for slug,(title,hook,function,assessment,goals) in config.items():
  p=folder/slug/'index.html';s=p.read_text(encoding='utf-8')
  if 'msk-patient-20261011.css' in s:continue
  s=re.sub(r'(<h1[^>]*>.*?</h1>)',lambda m:m[1]+f'<p class="msk-recognition">{hook}</p>',s,count=1,flags=re.S)
  s=re.sub(r'<figure\b[^>]*data-article-image="symptoms".*?</figure>','',s,flags=re.S)
  intro=f'<p class="msk-treatment-intro">在連邦，治療從你最困擾的動作開始。醫師會先評估{assessment}，再討論適合的針灸與功能訓練安排；治療後比較{function}的變化，作為後續調整的依據。</p><div class="msk-goals" aria-label="本頁功能追蹤重點">'+''.join(f'<span>{g}</span>' for g in goals)+'</div>'
  s=s.replace('<h2>連邦中醫的治療方式</h2>','<h2>連邦中醫的治療方式</h2>'+intro,1)
  start=s.index('<h2>連邦中醫的治療方式</h2>');end=s.index('</section>',start)
  chunk=s[start:end]
  chunk=re.sub(r'(<h3>浮針與針刀</h3>\s*<p>.*?</p>)',r'\1<div class="msk-method-links"><span>兩者為不同療程，由醫師評估適用方式。</span><a href="/浮針/">了解浮針</a><a href="/針刀/">了解針刀</a></div>',chunk,count=1,flags=re.S)
  booking=f'<div class="msk-invite"><p>想讓{title}不再佔據你的日常？先把最困擾的動作告訴我們。</p><a href="https://lin.ee/UWWKmse" target="_blank" rel="noopener noreferrer">預約{title}評估</a><small>治療安排與改善情況因人而異，需由醫師依實際狀況評估。</small></div>'
  # Append invitation before the section's outer shell closes.
  pos=chunk.rfind('</div>');chunk=chunk[:pos]+booking+chunk[pos:]
  s=s[:start]+chunk+s[end:]
  if slug=='low-back-pain':extra='<p class="msk-crosslink">若疼痛延伸至臀部或腿部，並伴隨麻木、刺痛或無力，也可閱讀<a href="/symptoms/sciatica/">坐骨痛的評估說明</a>；症狀名稱仍需由醫師確認。</p>'
  elif slug=='sciatica':extra='<p class="msk-crosslink">若主要是局部腰背不適，也可閱讀<a href="/symptoms/low-back-pain/">腰背痛的評估說明</a>；實際來源需由醫師確認。</p>'
  else:extra=''
  if extra:s=s.replace('<h2>常見相關因素</h2>','<h2>常見相關因素</h2>'+extra,1)
  s=s.replace('第一走越痛越要踩開嗎？','第一步越痛越要踩開嗎？')
  s=s.replace('class="symptoms-refresh ','class="msk-patient symptoms-refresh ',1).replace('</head>','<link rel="stylesheet" href="/assets/msk-patient-20261011.css"></head>',1)
  p.write_text(s,encoding='utf-8')
print('Updated 8 patient-focused musculoskeletal pages and mirrors')
