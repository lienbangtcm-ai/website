from pathlib import Path
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
for slug,key in [('針刀','acupotomy'),('pulse-diagnosis','pulse')]:
 page=ROOT/'output/site-preview'/slug/'index.html'
 doc=html.fromstring(page.read_text(encoding='utf-8'))
 hero=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," lb-hero ")]')[0]
 box=hero.find('div')
 if 'detail-illustrated-hero' not in box.get('class',''):
  box.set('class',box.get('class','')+' detail-illustrated-hero')
  if slug=='針刀':
   text=html.Element('div',{'class':'detail-hero-text'})
   for node in list(box):text.append(node)
   box.append(text)
 for old in box.xpath('./figure'):box.remove(old)
 figure=html.Element('figure',{'class':'detail-hero-art'})
 figure.append(html.Element('img',src=f'/assets/service-reference/{key}.png',alt='',width='280',height='220',decoding='async',fetchpriority='high'))
 box.append(figure)
 for old in doc.xpath('//link[contains(@href,"detail-illustrations.css")]'):old.getparent().remove(old)
 doc.find('body').append(html.Element('link',rel='stylesheet',href='/assets/detail-illustrations.css?v=1'))
 page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
 print('Added approved illustration:',slug)
