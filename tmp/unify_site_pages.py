"""Apply audited local style repairs without rewriting medical text or article images."""
from pathlib import Path
from shutil import copy2
from lxml import html
import hashlib,json
ROOT=Path(__file__).resolve().parents[1];SITE=ROOT/'output/site-preview'
copy2(ROOT/'lienbang-assets/site-unified.css',SITE/'assets/site-unified.css')
copy2(ROOT/'output/selfpay-content/shared-selfpay.css',SITE/'assets/shared-selfpay.css')
records=[]
for page in SITE.rglob('index.html'):
    rel=page.relative_to(SITE)
    backup=ROOT/'output/identity-backup/style-unification'/rel
    backup.parent.mkdir(parents=True,exist_ok=True)
    if not backup.exists():backup.write_bytes(page.read_bytes())
    doc=html.fromstring(page.read_text(encoding='utf-8'))
    def signature():
        # Exclude style/script text only; links and actual content are preserved.
        text=''.join(doc.xpath('//body//text()[not(ancestor::style) and not(ancestor::script)]'))
        return hashlib.sha256(text.encode()).hexdigest(),[a.get('href') for a in doc.xpath('//a')]
    original=signature()
    images=[dict(i.attrib) for i in doc.xpath('//img')]
    for link in doc.xpath('//link[contains(@href,"shared-selfpay.css")]'):link.set('href','/assets/shared-selfpay.css?v=1')
    for link in doc.xpath('//link[contains(@href,"site-unified.css")]'):link.getparent().remove(link)
    doc.find('body').append(html.Element('link',rel='stylesheet',href='/assets/site-unified.css?v=1'))
    if page==SITE/'index.html':
        cards=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lbh4-service ")]')
        for card,key in zip(cards,['movement','pulse','facial']):
            for child in list(card):
                if child.tag in ('svg','img'):card.remove(child)
            card.insert(0,html.Element('img',{'class':'home-service-reference','src':f'/assets/service-reference/{key}.png','alt':'','loading':'lazy','width':'144','height':'116'}))
    assert signature()==original,rel
    if page!=SITE/'index.html':assert [dict(i.attrib) for i in doc.xpath('//img')]==images,rel
    page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
    records.append({'page':str(rel),'text_and_links_unchanged':True,'article_images_unchanged':page!=SITE/'index.html'})
(ROOT/'output/release-audit/style-unification-preservation.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf-8')
print('Updated',len(records),'pages; all text and links unchanged. Only homepage service illustrations replaced.')
