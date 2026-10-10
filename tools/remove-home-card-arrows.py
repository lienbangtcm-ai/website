from pathlib import Path
import re
for f in [Path('output/site-preview/index.html'),Path('output/site-preview/dist/index.html')]:
 t=f.read_text(encoding='utf-8');t=re.sub(r'<span(?: class="to-arrow" aria-hidden="true")?>→</span>','',t);f.write_text(t,encoding='utf-8')
