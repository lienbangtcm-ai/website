from pathlib import Path
for f in [Path('output/site-preview/services/index.html'),Path('output/site-preview/dist/services/index.html')]:
 t=f.read_text(encoding='utf-8')
 if 'services-compact-20261009.css' not in t:t=t.replace('</body>','<link rel="stylesheet" href="/assets/services-compact-20261009.css">\n</body>')
 f.write_text(t,encoding='utf-8')
