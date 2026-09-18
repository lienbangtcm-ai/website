"""Direct crops explicitly requested by user; preserve source, links and articles."""
from pathlib import Path
from PIL import Image
from lxml import html
import hashlib

ROOT=Path(__file__).resolve().parents[1]
SLUGS=['gerd','cough','insomnia','allergic-rhinitis','diarrhea','constipation','menstrual-pain','fatigue']

def apply():
    im=Image.open(ROOT/'output/illustration-master/approved-internal-reference.png')
    dest=ROOT/'output/site-preview/assets/illustrations/reference-crops'
    dest.mkdir(parents=True,exist_ok=True)
    cols=[(39,365),(416,744),(794,1123),(1174,1500)]
    rows=[(40,394),(536,890)]
    sizes={}
    for i,slug in enumerate(SLUGS):
        x1,x2=cols[i%4];y1,y2=rows[i//4]
        box=tuple(round(v*s) for v,s in zip((x1,y1,x2,y2),(im.width/1536,im.height/1024,im.width/1536,im.height/1024)))
        crop=im.crop(box)
        crop.save(dest/f'{slug}.png',optimize=True)
        sizes[slug]=crop.size
    page=ROOT/'output/site-preview/symptoms/index.html'
    backup=ROOT/'output/identity-backup/symptoms-before-internal-reference.html'
    if not backup.exists():backup.write_bytes(page.read_bytes())
    articles={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in page.parent.glob('*/index.html')}
    doc=html.fromstring(page.read_text(encoding='utf-8'))
    unchanged=html.tostring(doc.get_element_by_id('orthopedics'))
    links=[a.get('href') for a in doc.xpath('//ul[@class="lbsym-list"]//a')]
    for a in doc.xpath('//ul[@class="lbsym-list"]//a'):
        slug=a.get('href').strip('/').split('/')[-1]
        if slug not in SLUGS:continue
        for child in list(a):
            if child.tag in ('svg','img'):a.remove(child)
        a.set('class','symptom-master-card reference-crop-card')
        w,h=sizes[slug]
        a.insert(0,html.Element('img',src=f'/assets/illustrations/reference-crops/{slug}.png',alt='',width=str(w),height=str(h),loading='lazy',decoding='async'))
    assert html.tostring(doc.get_element_by_id('orthopedics'))==unchanged
    assert [a.get('href') for a in doc.xpath('//ul[@class="lbsym-list"]//a')]==links
    page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
    assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in articles.items())
    print(f'8 internal crops applied from {im.size}; musculoskeletal section, 16 links and articles unchanged.')

if __name__=='__main__':apply()
