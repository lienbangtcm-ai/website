from pathlib import Path
import re,json
root=Path('output/site-preview')
config={
'gerd':('胃食道逆流','反酸、胸口灼熱與夜間不適','逆流頻率、飲食耐受與夜間症狀'),
'cough':('咳嗽','反覆咳嗽、痰液與夜間咳嗽','咳嗽頻率、痰液與夜間睡眠'),
'insomnia':('失眠','難入睡、夜間醒來與白天疲倦','入睡時間、夜醒次數與白天精神'),
'allergic-rhinitis':('鼻過敏','鼻塞、鼻水、發癢與睡眠影響','發作頻率、鼻部不適與睡眠'),
'diarrhea':('腹瀉','反覆稀便、腹痛與飲食誘發情境','排便次數、腹痛與食慾'),
'constipation':('便秘','排便費力、糞便乾硬與腹脹','排便順暢度、糞便型態與腹部感受'),
'menstrual-pain':('經痛','經期疼痛、出血與伴隨不適','疼痛天數、止痛藥使用與週期變化'),
'fatigue':('疲倦','持續疲倦、睡眠與活動後恢復','精神、睡眠與活動耐受度')}
headings=['認識症狀與身體變化','可能因素與評估時機','連邦可以如何幫助你','日常照護與看診準備','需要先就醫的情況','常見問題']
for folder in [root/'symptoms',root/'dist/symptoms']:
 for slug,(title,concerns,tracking) in config.items():
  p=folder/slug/'index.html';s=p.read_text(encoding='utf-8')
  if 'internal-reader-20261011.css' in s:continue
  starts=list(re.finditer(r'<section\b[^>]*class="lb-section\b[^>]*>',s));chunks=[]
  for m in starts:
   depth=0;end=None
   for t in re.finditer(r'</?section\b[^>]*>',s[m.start():]):
    depth+=-1 if t[0].startswith('</') else 1
    if depth==0:end=m.start()+t.end();break
   if end:chunks.append((m.start(),end,s[m.start():end]))
  groups=[[] for _ in headings]
  for i,(start,end,chunk) in enumerate(chunks):
   # Preserve inter-section illustrations and text in older GERD layout.
   if i+1<len(chunks):chunk+=s[end:chunks[i+1][0]]
   h=re.search(r'<h2[^>]*>(.*?)</h2>',chunk,re.S);name=re.sub('<[^>]+>','',h[1]) if h else ''
   if '常見問題' in name:group=5
   elif '盡快就醫' in name:group=4
   elif '記錄' in name or '照護' in name:group=3
   elif '中醫' in name or '治療' in name:group=2
   elif '因素' in name or '哪些人' in name:group=1
   else:group=0
   if name=='中醫診療方向':chunk='<details class="ir-depth"><summary>進一步了解中醫辨證方向</summary>'+chunk+'</details>'
   # Keep original content but eliminate the second use of the hero photograph.
   chunk=re.sub(r'<figure\b[^>]*data-article-image="symptoms".*?</figure>','',chunk,flags=re.S)
   groups[group].append(chunk)
  result=[]
  for i,items in enumerate(groups):
   if items:result.append(f'<section class="ir-group" id="reader-{i}"><div class="ir-group-heading"><span>0{i+1}</span><h2>{headings[i]}</h2></div>'+''.join(items)+'</section>')
  s=s[:chunks[0][0]]+''.join(result)+s[chunks[-1][1]:]
  help=f'''<section class="ir-help" aria-labelledby="ir-help-title"><div class="lb-shell"><p class="ir-kicker">CARE AT LIEN BANG</p><h2 id="ir-help-title">{title}反覆困擾你？連邦陪你找出調理方向。</h2><p class="ir-intro">從{concerns}開始，醫師會結合問診與脈診辨證，評估適合你的中醫治療；有需要檢查或轉介的情況，也會一起說明。</p><div class="ir-steps"><div><h3>先了解你的困擾</h3><p>整理症狀、生活影響、目前用藥與檢查資料，讓看診有明確起點。</p></div><div><h3>討論個別治療</h3><p>依評估安排中藥處方，並討論是否適合搭配針灸與生活調整。</p></div><div><h3>一起追蹤變化</h3><p>回診比較{tracking}，依身體反應調整治療方向。</p></div></div><div class="ir-help-actions"><a href="https://lin.ee/UWWKmse" class="ir-booking">向連邦預約評估</a><a href="#reader-2">了解評估與治療方式</a></div><p class="ir-note">治療安排與改善情況因人而異，需由醫師依實際狀況評估。</p></div></section>'''
  nav='<nav class="lb-nav ir-nav" aria-label="文章重點導覽"><div class="lb-nav-inner">'+''.join(f'<a href="#reader-{i}">{headings[i]}</a>' for i,items in enumerate(groups) if items)+'</div></nav>'
  s=re.sub(r'<nav class="lb-nav".*?</nav>',help+nav,s,count=1,flags=re.S)
  s=s.replace('class="symptoms-refresh ','class="internal-reader symptoms-refresh ',1)
  s=s.replace('</head>','<link rel="stylesheet" href="/assets/internal-reader-20261011.css"></head>',1)
  warning=re.search(r'<h2[^>]*>什麼情況需要盡快就醫？</h2>\s*<p>(.*?)</p>',s,re.S)
  if warning:warning_text=warning[1].split('。')[0]+'。';target='#reader-4'
  else:warning_text='胸痛也不一定都是胃食道逆流，若無法確定來源，不應只靠胃藥自行判斷。';target='#reader-0'
  note=f'<aside class="ir-alert"><strong>先留意就醫需求</strong><p>{warning_text}</p><a href="{target}">閱讀完整說明</a></aside>'
  s=s.replace('<p class="ir-note">',note+'<p class="ir-note">',1)
  s=s.replace('<h2>常見問題</h2><div class="lb-faq">','<div class="lb-faq">')
  p.write_text(s,encoding='utf-8')
print('Updated 8 internal pages and dist mirrors')
