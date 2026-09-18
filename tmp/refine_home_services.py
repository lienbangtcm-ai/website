from pathlib import Path
import re
R=Path(__file__).resolve().parents[1]
groups=[('內科與日常調理','從身體的不適，找到想了解的照護資訊。',[('gerd','胃食道逆流'),('cough','咳嗽'),('insomnia','失眠'),('allergic-rhinitis','鼻過敏'),('diarrhea','腹瀉'),('constipation','便秘'),('menstrual-pain','經痛'),('fatigue','疲倦')]),('疼痛與活動困擾','依疼痛部位，了解評估與日常照護。',[('frozen-shoulder','五十肩'),('neck-shoulder-pain','肩頸痛'),('low-back-pain','腰背痛'),('sciatica','坐骨痛'),('knee-pain','膝痛'),('tennis-elbow','網球肘'),('de-quervain','媽媽手'),('plantar-heel-pain','足底痛')])]
cards='<div class="lb-symptom-directory">'+''.join('<article class="lb-symptom-panel"><h3>'+title+'</h3><p>'+desc+'</p><div class="lb-symptom-options">'+''.join(f'<a href="/symptoms/{slug}/">{label}<span aria-hidden="true">↗</span></a>' for slug,label in links)+'</div></article>' for title,desc,links in groups)+'</div>'
css='''<style id="home-symptom-refinement">.lb-symptom-directory{display:grid;grid-template-columns:1fr 1fr;gap:32px}.lb-symptom-panel{padding:36px;background:#f8f4ee;border-top:3px solid #99735e;border-radius:0 0 16px 16px}.lb-symptom-panel h3{font-size:28px;color:#4a3028;margin:0 0 10px}.lb-symptom-panel>p{font-size:15px;color:#776a61;margin:0 0 24px}.lb-symptom-options{display:grid;grid-template-columns:1fr 1fr;gap:0 24px}.lb-symptom-options a{display:flex;align-items:center;justify-content:space-between;gap:8px;min-height:58px;border-bottom:1px solid #ded3c6;color:#4a3028!important;text-decoration:none!important;font-size:17px}.lb-symptom-options a span{color:#987961}.lb-symptom-options a:hover{background:#eee5da}.lb-symptom-options a:focus-visible{outline:2px solid #99735e;outline-offset:2px}@media(max-width:700px){.lb-symptom-directory{grid-template-columns:1fr;gap:24px}.lb-symptom-panel{padding:26px 22px}.lb-symptom-panel h3{font-size:25px}.lb-symptom-options{gap:0 16px}.lb-symptom-options a{font-size:16px}}</style>'''
for path in [R/'lienbang-assets/premium-home-v4.html',R/'output/site-preview/index.html']:
 s=path.read_text(encoding='utf-8')
 s=re.sub(r'<div class="lbh4-symptom-stories">.*?</section>',cards+'</div></section>',s,flags=re.S)
 s=s.replace('</style>', '</style>'+css,1)
 s=s.replace('一般針灸、不留針、針刀、浮針、針灸整合物理治療。','一般針灸、不留針與針灸整合物理治療。')
 s=s.replace('<h3>中醫內科</h3>','<h3>脈診辨證</h3>').replace('查看中醫內科 →','了解辨證與組方 →').replace('脈診辨證、單味藥組方與內科診療說明。','脈診辨證：綜合問診、舌象與脈象評估。<br>單味藥組方：逐味安排藥材、比例與劑量。')
 path.write_text(s,encoding='utf-8')
for path in [R/'output/services-page.html',R/'output/site-preview/services/index.html']:
 s=path.read_text(encoding='utf-8').replace('中醫內科','脈診辨證')
 start=s.index('<article class="lbsv-service-row" id="orthopedics">');end=s.index('</article>',start)
 part=s[start:end]
 part=re.sub(r'<a href="[^"]+">(?:針刀|浮針)</a>','',part)
 s=s[:start]+part+s[end:]
 s=s.replace('脈診辨證／單味藥組方</a>','單味藥組方：藥材、比例與劑量</a>')
 s=s.replace('<h3>脈診辨證</h3><div class="lbsv-service-links">','<h3>脈診辨證</h3><p>綜合問診、舌象、脈象與病程，了解當次身體狀況。</p><p>辨證是評估的過程；單味藥組方則是依評估安排處方，兩者分開說明。</p><div class="lbsv-service-links">')
 path.write_text(s,encoding='utf-8')
print('Updated home and services sources and previews')
