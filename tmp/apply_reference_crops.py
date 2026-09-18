"""User-authorized direct cropping of supplied master; no generative edits."""
from pathlib import Path
from PIL import Image
from lxml import html
import hashlib

ROOT=Path(__file__).resolve().parents[1]
SLUGS=['frozen-shoulder','neck-shoulder-pain','low-back-pain','sciatica',
       'knee-pain','tennis-elbow','de-quervain','plantar-heel-pain']

def apply():
    source=ROOT/'output/illustration-master/approved-master-reference.png'
    im=Image.open(source)
    print('Master dimensions:',im.size)
    dest=ROOT/'output/site-preview/assets/illustrations/reference-crops'
    dest.mkdir(parents=True,exist_ok=True)
    # Coordinates measured in the supplied 1536 × 1024 reference. Exclude text,
    # arrows and card borders, but retain every hand/toe and the background circle.
    columns=[(39,365),(416,744),(794,1123),(1174,1500)]
    rows=[(48,402),(548,888)]
    for n,slug in enumerate(SLUGS):
        left,right=columns[n%4];top,bottom=rows[n//4]
        box=tuple(round(v*s) for v,s in zip((left,top,right,bottom),(im.width/1536,im.height/1024,im.width/1536,im.height/1024)))
        im.crop(box).save(dest/f'{slug}.png',optimize=True)
    page=ROOT/'output/site-preview/symptoms/index.html'
    articles={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in page.parent.glob('*/index.html')}
    doc=html.fromstring(page.read_text(encoding='utf-8'))
    internal=html.tostring(doc.get_element_by_id('internal'))
    backup=ROOT/'output/identity-backup/symptoms-before-reference-crops.html'
    if not backup.exists():backup.write_bytes(page.read_bytes())
    for a in doc.xpath('//ul[@class="lbsym-list"]//a'):
        slug=a.get('href').strip('/').split('/')[-1]
        if slug not in SLUGS:continue
        for node in list(a):
            if node.tag in ('svg','img'):a.remove(node)
        a.set('class','symptom-master-card reference-crop-card')
        image=html.Element('img',src=f'/assets/illustrations/reference-crops/{slug}.png',alt='',width='328',height='350',loading='lazy',decoding='async')
        a.insert(0,image)
    for node in doc.xpath('//link[contains(@href,"reference-crops.css")]'):node.getparent().remove(node)
    doc.find('body').append(html.Element('link',rel='stylesheet',href='/assets/reference-crops.css?v=1'))
    assert html.tostring(doc.get_element_by_id('internal'))==internal
    page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
    for section in doc.xpath('//section[@class="lbsym-block"]'):
        if section.get('id')=='internal':section.getparent().remove(section)
    doc.xpath('//h1')[0].text='筋骨疼痛・原圖套用預覽'
    (page.parent/'musculoskeletal-study.html').write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
    assert all(hashlib.sha256(p.read_bytes()).hexdigest()==v for p,v in articles.items())
    print('8 original-image crops applied; internal cards and article files unchanged.')

if __name__=='__main__':apply()
