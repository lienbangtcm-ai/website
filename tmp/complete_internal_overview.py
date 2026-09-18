from pathlib import Path
block='''<section class="lb-section lb-section--ivory" id="internal-overview"><div class="lb-shell"><h2>我們會做什麼</h2><p class="lb-lead">先了解症狀與生活狀況，透過把脈辨證綜合評估；需要用藥時，再安排單味藥組方，並於回診追蹤變化。</p><div class="lb-cross"><a href="#assessment">把脈評估 →</a><a href="#why">單味藥組方 →</a></div><h2 style="margin-top:42px">有哪些診療項目</h2><div class="lb-cards">'''
for title,links in [('腸胃與消化',[('gerd','胃食道逆流'),('constipation','便秘'),('diarrhea','腹瀉')]),('呼吸道與鼻部',[('cough','咳嗽'),('allergic-rhinitis','鼻過敏')]),('睡眠、精神與經期',[('insomnia','失眠'),('fatigue','疲倦'),('menstrual-pain','經痛')])]:
 block+='<article class="lb-card"><h3>'+title+'</h3>'+''.join(f'<p><a href="/symptoms/{slug}/">{name} →</a></p>' for slug,name in links)+'</article>'
block+='</div><p>可點選症狀了解評估與照護資訊，實際診療安排依醫師評估決定。</p></div></section>'
for p in [Path('output/pulse-diagnosis/pulse-diagnosis-final.html'),Path('output/site-preview/pulse-diagnosis/index.html')]:
 s=p.read_text(encoding='utf-8');assert 'id="internal-overview"' not in s
 s=s.replace('<section class="lb-section" id="assessment">',block+'<section class="lb-section" id="assessment">',1)
 s=s.replace('<a href="#dose">劑量調整</a>','<a href="#internal-overview">診療項目</a>')
 p.write_text(s,encoding='utf-8')
