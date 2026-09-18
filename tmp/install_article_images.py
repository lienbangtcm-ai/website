from pathlib import Path
from lxml import html, etree
from PIL import Image
import json, shutil, re, subprocess, sys

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'output'
SITE=OUT/'site-preview'
plan=json.loads((OUT/'article-images-three-plan.json').read_text(encoding='utf-8'))['plan']
results={}
for f in (OUT/'article-image-results').glob('*.json'):
    item=json.loads(f.read_text(encoding='utf-8')); results[item['key']]=item['path']

def export_image(source, folder, key):
    folder.mkdir(parents=True,exist_ok=True)
    for ext,fmt in [('webp','WEBP'),('jpg','JPEG')]:
        dest=folder/(key+'.'+ext)
        if dest.exists(): continue
        im=Image.open(source).convert('RGB')
        im.thumbnail((1200,800),Image.Resampling.LANCZOS)
        if im.size!=(1200,800):
            canvas=Image.new('RGB',(1200,800),'#f7f2e9');canvas.paste(im,((1200-im.width)//2,(800-im.height)//2));im=canvas
        for q in [88,82,76,70,64,58,50]:
            im.save(dest,fmt,quality=q,optimize=True)
            if dest.stat().st_size<200000:break
        assert dest.stat().st_size<200000, str(dest)

def serialize(doc):return '<!doctype html>\n'+html.tostring(doc,encoding='unicode',method='html')

done=[]
for page in sorted((SITE/'symptoms').glob('*/index.html')):
    slug=page.parent.name
    entries=[p for p in plan if p['slug']==slug]
    if entries and not all(p['key'] in results for p in entries):continue
    doc=html.fromstring(page.read_text(encoding='utf-8'))
    article=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lb-article ")]')[0]
    if slug in ['gerd','insomnia']:
        for fig in article.xpath('.//figure[contains(@class,"lb-hero-visual")]'):fig.getparent().remove(fig)
        for fig in article.xpath('.//figure[.//img]'):
            if not fig.xpath('./figcaption'):
                etree.SubElement(fig,'figcaption').text='情境示意｜'+fig.xpath('.//img')[0].get('alt','文章照護說明')
    else:
        for p in entries:
            key=p['key']
            folder=OUT/slug/'images'
            export_image(results[key],folder,key)
            (page.parent/'images').mkdir(exist_ok=True)
            for ext in ['webp','jpg']:shutil.copy2(folder/(key+'.'+ext),page.parent/'images'/(key+'.'+ext))
            for fig in article.xpath('.//figure[@data-article-image="'+p['role']+'"]'):fig.getparent().remove(fig)
            headings=article.xpath('.//h2')
            if p['role']=='symptoms': matches=[h for h in headings if '困擾' in ''.join(h.itertext())]
            elif p['role']=='assessment':matches=[h for h in headings if '評估' in ''.join(h.itertext()) and '連邦' in ''.join(h.itertext())]
            else:matches=[h for h in headings if '日常照護' in ''.join(h.itertext())]
            if not matches:raise ValueError(slug+' missing heading '+p['role'])
            target=matches[0].getparent()
            caption=p['caption']
            fig=html.Element('figure',{'class':'lb-figure lb-added-figure','data-article-image':p['role']})
            picture=etree.SubElement(fig,'picture')
            etree.SubElement(picture,'source',srcset='images/'+key+'.webp',type='image/webp')
            alt=p['title']+{'symptoms':'症狀與生活困擾情境插畫','assessment':'就診評估與醫病討論情境插畫','daily-care':'日常照護情境插畫'}[p['role']]
            etree.SubElement(picture,'img',src='images/'+key+'.jpg',alt=alt,width='1200',height='800',loading='lazy',decoding='async')
            etree.SubElement(fig,'figcaption').text=caption
            target.append(fig)
    assert len(article.xpath('.//img'))==3,(slug,len(article.xpath('.//img')))
    page.write_text(serialize(doc),encoding='utf-8')
    standalone=html.fromstring(serialize(doc))
    for node in standalone.xpath('//*[contains(@class,"preview-header") or contains(@class,"preview-related")] | //meta[@name="robots"] | //link[contains(@href,"site-shared.css")]'):
        node.getparent().remove(node)
    style=etree.SubElement(standalone.find('head'),'style');style.text=(ROOT/'lienbang-assets/site-shared.css').read_text(encoding='utf-8')
    for a in standalone.xpath('//a[contains(@href,"lin.ee")]'):
        a.set('href','https://lin.ee/NMa1es5');a.set('target','_blank');a.set('rel','noopener noreferrer')
    folder=OUT/'illustrated-articles'/slug;folder.mkdir(parents=True,exist_ok=True)
    image_folder=folder/'images';image_folder.mkdir(exist_ok=True)
    used={n.get('src') or n.get('srcset') for n in article.xpath('.//img | .//source')}
    for src in used:
        if src and src.startswith('images/'):
            shutil.copy2(page.parent/src,image_folder/Path(src).name)
    for old in image_folder.iterdir():
        if old.is_file() and 'images/'+old.name not in used:old.unlink()
    final=folder/(slug+'-illustrated.html'); final.write_text(serialize(standalone),encoding='utf-8')
    validator=Path('C:/Users/yutin/.codex/skills/lianbang-seo-article/scripts/validate_article.py')
    check=subprocess.run([sys.executable,str(validator),str(final)],capture_output=True,text=True)
    if check.returncode:raise ValueError(slug+': '+check.stdout)
    done.append(slug)
(OUT/'article-images-install-status.json').write_text(json.dumps({'installed':done,'count':len(done),'target':16},indent=2),encoding='utf-8')
print('Installed 3 inline images each: '+', '.join(done))
