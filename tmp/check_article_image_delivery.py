from pathlib import Path
from lxml import html
from PIL import Image
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'
rows=[]
for f in sorted((OUT/'illustrated-articles').glob('*/*-illustrated.html')):
    slug=f.parent.name
    doc=html.fromstring(f.read_text(encoding='utf-8'))
    article=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lb-article ")]')[0]
    images=article.xpath('.//img'); assert len(images)==3,slug
    files=[]
    for im in images:
        assert im.get('alt') and im.get('loading')=='lazy',slug
        source=f.parent/im.get('src'); assert source.exists(),str(source)
        with Image.open(source) as bitmap:
            bitmap.verify()
        files.append({'path':source.relative_to(OUT).as_posix(),'bytes':source.stat().st_size})
    for s in article.xpath('.//source[@srcset]'):
        source=f.parent/s.get('srcset'); assert source.exists(),str(source)
        with Image.open(source) as bitmap:bitmap.verify()
    baseline=OUT/slug/(slug+'-final.html')
    text_preserved=None
    if baseline.exists():
        old=html.fromstring(baseline.read_text(encoding='utf-8'))
        def content(d):
            return [' '.join(''.join(e.itertext()).split()) for e in d.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lb-article ")]//*[self::h1 or self::h2 or self::h3 or self::p or self::li or self::summary][not(ancestor::figure)]')]
        text_preserved=content(old)==content(doc)
        assert text_preserved,slug+' article text differs'
    rows.append({'slug':slug,'inlineImages':3,'textPreserved':text_preserved,'files':files})
assert len(rows)==16,len(rows)
result={'articles':16,'inlineImages':48,'checks':rows}
(OUT/'release-audit/article-image-delivery.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print('PASS: 16 articles, 48 inline images; valid files, alt text, lazy loading and existing article text preserved')
