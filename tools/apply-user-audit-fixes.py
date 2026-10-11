from pathlib import Path
from PIL import Image
import re
root=Path('output/site-preview');src=Path('C:/Users/yutin/.codex/generated_images/01a11ef4-d45a-7b91-a596-f6939a8b5606/exec-444f0bce-2eb3-4903-a399-704ce83f4b3d.png');asset=root/'assets/fsn-operation-illustration-20261011.webp'
with Image.open(src) as im:im.convert('RGB').save(asset,'WEBP',quality=88)
for p in root.rglob('index.html'):
 if any(x in p.relative_to(root).parts for x in ['review','assets']):continue
 s=p.read_text(encoding='utf-8');s=s.replace('href="/symptoms/">衛教文章','href="/articles/">衛教文章')
 def fsn(m):return m[0].replace('/assets/symptoms-20261010/frozen-shoulder-1600.webp','/assets/fsn-operation-illustration-20261011.webp').replace('肩部不適情境示意','浮針操作示意圖')
 s=re.sub(r'<a\b[^>]*href="/(?:%E6%B5%AE%E9%87%9D|浮針)/"[^>]*>.*?</a>',fsn,s,flags=re.S)
 if p.parent.name=='浮針':s=s.replace("--su-photo:url('/assets/symptoms-20261010/frozen-shoulder-1600.webp')","--su-photo:url('/assets/fsn-operation-illustration-20261011.webp')")
 summaries={'浮針':'從患肌與活動限制評估，了解浮針是否適合你的疼痛問題。','針刀':'針對軟組織與活動限制進行個別評估，了解針刀的操作與注意事項。','美顏針':'從臉部肌肉、生活習慣與整體狀態評估，討論適合的美顏針安排。'}
 if p.parent.name in summaries:
  s=re.sub(r'(<div class="su-hero-copy">.*?<h1>.*?</h1><p>).*?(</p>)',lambda m:m[1]+summaries[p.parent.name]+m[2],s,count=1,flags=re.S)
 if p.parent.name=='about-lienbang':s=s.replace('認識我們的理念 →','認識連邦理念')
 if p.parent.name=='symptoms':
  t='常見的不適與身體狀況，從中醫角度了解原因，提供個別評估與調理建議。'
  i=s.find(t);j=s.find(t,i+len(t))
  if j>=0:s=s[:j]+'依你的主要困擾，選擇下方分類了解評估與照護方向。'+s[j+len(t):]
 p.write_text(s,encoding='utf-8')
s=(root/'symptoms/index.html').read_text(encoding='utf-8');s=re.sub(r'<title>.*?</title>','<title>衛教文章｜連邦中醫診所</title>',s,count=1);s=s.replace('<h1>常見症狀</h1>','<h1>衛教文章</h1>').replace('COMMON SYMPTOMS','HEALTH EDUCATION');s=s.replace('常見的不適與身體狀況，從中醫角度了解原因，提供個別評估與調理建議。','從症狀認識、中醫辨證到日常照護，閱讀連邦的衛教內容。')
for d in [root/'articles',root/'dist/articles']:d.mkdir(parents=True,exist_ok=True);(d/'index.html').write_text(s,encoding='utf-8')
p=root/'assets/home-design-system-20261009.css';p.write_text(p.read_text(encoding='utf-8')+'''
/* User audit fixes: intrinsic image height, readable captions and compact article rhythm. */
body.home-system .dp-symptom img{width:100%!important;height:auto!important;aspect-ratio:1.28/1!important;object-fit:cover!important}
body.home-system .ab-photo-caption{position:static!important;inset:auto!important;display:block!important;background:#f8f5ef!important;color:#493023!important;padding:14px 18px!important;margin:0!important;font-size:16px!important;text-shadow:none!important;max-width:none!important;transform:none!important}
body.home-system .ab-btn{white-space:nowrap!important}
body.home-system .ab-hero h1,body.home-system .lbsym-hero h1{font-size:58px!important}
body.home-system .lb-table th{background:#eee5da!important;color:#493023!important}
body.home-system .lb-table td{background:#fffdf9!important}
@media(max-width:768px){body.home-system .ab-hero h1,body.home-system .lbsym-hero h1{font-size:38px!important}body.home-system .ab-btn{padding-inline:18px!important;font-size:15px!important}body.home-system .lb-section{padding-block:40px!important}body.home-system .lb-section h2{margin-bottom:22px!important}body.home-system .lb-section p{margin-block:12px!important}}
''',encoding='utf-8')
print('Updated active pages and shared styles; created articles index')

