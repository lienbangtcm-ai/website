from pathlib import Path
import re
root=Path('output/site-preview');s=(root/'services/index.html').read_text(encoding='utf-8');cards=re.search(r'<div class="to-wrap to-service-grid">(.*?)</div></nav>',s,re.S).group(1);cards=cards.replace('class="to-service-card"','class="home-service-card"').replace('<h2>','<h3>').replace('</h2>','</h3>').replace('<img src=','<img loading="lazy" decoding="async" src=')
for f in [root/'index.html',root/'dist/index.html']:
 t=f.read_text(encoding='utf-8');t=re.sub(r'(<div class="service-cards">).*?(</div></div></section>)',lambda m:m[1]+cards+m[2],t,count=1,flags=re.S)
 if 'service-cards-unified.css' not in t:t=t.replace('</body>','<link rel="stylesheet" href="/assets/service-cards-unified.css">\n</body>')
 f.write_text(t,encoding='utf-8')
