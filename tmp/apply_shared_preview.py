from pathlib import Path
import re, shutil

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'output/site-preview'
assets=SITE/'assets'; assets.mkdir(exist_ok=True)
shutil.copy2(ROOT/'lienbang-assets/site-shared.css',assets/'site-shared.css')
logo='https://lienbangtcm.tw/storage/twyuting10210314859/2021/07/連邦中醫白logo.png'
for file in SITE.rglob('*.html'):
    doc=file.read_text(encoding='utf-8')
    doc=re.sub(r'<style>html,body\{margin:0;overflow-x:hidden\}\.preview-header.*?</style>','',doc,flags=re.S)
    doc=re.sub(r'(<a class="preview-brand"[^>]*>).*?(</a>)',lambda m:m[1]+f'<img src="{logo}" alt="連邦中醫診所" width="2362" height="470" fetchpriority="high">'+m[2],doc,flags=re.S)
    def update_header(m):
        header=m[0]
        for slug in ['team','health-blog','support']:
            header=re.sub(r'<a href="https://lienbangtcm.tw/'+slug+r'/"[^>]*>(.*?)</a>',lambda a:f'<a href="https://lienbangtcm.tw/{slug}/" target="_blank" rel="noopener noreferrer" title="現有正式網站，於新分頁開啟">'+re.sub(r'<span.*?</span>','',a[1])+ '<span class="external-mark" aria-hidden="true">↗</span></a>',header)
        return header
    doc=re.sub(r'<header class="preview-header">.*?</header>',update_header,doc,flags=re.S)
    doc=re.sub(r'<link[^>]+href="/assets/site-shared.css[^\"]*"[^>]*>','',doc)
    doc=doc.replace('</body>','<link rel="stylesheet" href="/assets/site-shared.css?v=2"></body>')
    file.write_text(doc,encoding='utf-8')
print('Applied shared logo, navigation and warm palette to all preview pages')
