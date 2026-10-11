from pathlib import Path
import subprocess,re
root=Path('output/site-preview');slugs=['gerd','cough','insomnia','allergic-rhinitis','diarrhea','constipation','menstrual-pain','fatigue']
for folder in [root/'symptoms',root/'dist/symptoms']:
 for slug in slugs:
  p=folder/slug/'index.html';s=subprocess.check_output(['git','show','c02dd0b:'+p.as_posix()]).decode('utf-8')
  s=re.sub(r'<figure\b[^>]*data-article-image="symptoms".*?</figure>','',s,flags=re.S)
  s=s.replace('</head>','<link rel="stylesheet" href="/assets/internal-classic-polish-20261011.css"></head>',1)
  p.write_text(s,encoding='utf-8')
print('Restored 8 classic articles and dist mirrors; removed duplicate hero photos')
