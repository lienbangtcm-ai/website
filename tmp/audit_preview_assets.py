from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse, unquote, quote
from urllib.request import Request, urlopen
from concurrent.futures import ThreadPoolExecutor
import csv, json

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'output/site-preview'
OUT = ROOT / 'output/release-audit'
OUT.mkdir(exist_ok=True)

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(); self.assets = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'img' and a.get('src'): self.assets.append(a['src'])
        if tag in ('img', 'source') and a.get('srcset'):
            self.assets.extend(x.strip().split()[0] for x in a['srcset'].split(',') if x.strip())

rows = []
for file in sorted(SITE.rglob('*.html')):
    p = Parser(); p.feed(file.read_text(encoding='utf-8'))
    for src in sorted(set(p.assets)):
        u = urlparse(src)
        local = None if u.scheme or u.netloc else (SITE / unquote(u.path).lstrip('/') if u.path.startswith('/') else file.parent / unquote(u.path))
        rows.append({'page': file.relative_to(SITE).as_posix(), 'source': src,
                     'kind': 'remote' if local is None else 'local',
                     'local_exists': '' if local is None else local.exists(),
                     'bytes': '' if local is None or not local.exists() else local.stat().st_size})

def check(url):
    try:
        with urlopen(Request(quote(url, safe=':/%?=&+#'), headers={'User-Agent': 'Mozilla/5.0'}), timeout=25) as r:
            return {'url': url, 'status': r.status, 'content_type': r.headers.get('Content-Type',''), 'final_url': r.url}
    except Exception as e:
        return {'url': url, 'error': str(e)}

urls = sorted({r['source'] for r in rows if r['kind']=='remote'} | {'https://lin.ee/UWWKmse', 'https://lin.ee/NMa1es5'})
with ThreadPoolExecutor(max_workers=6) as pool: checks = list(pool.map(check, urls))
with (OUT/'image-manifest.csv').open('w', encoding='utf-8-sig', newline='') as f:
    w=csv.DictWriter(f, fieldnames=['page','source','kind','local_exists','bytes']); w.writeheader(); w.writerows(rows)
(OUT/'remote-checks.json').write_text(json.dumps(checks, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'references':len(rows), 'remote_urls_checked':len(checks), 'failed':[c for c in checks if 'error' in c], 'line':[c for c in checks if 'lin.ee' in c['url']]}, ensure_ascii=False, indent=2))
