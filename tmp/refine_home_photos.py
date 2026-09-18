"""Local homepage composition using user-provided clinic photographs, unmodified."""
from pathlib import Path
from shutil import copy2
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
page=ROOT/'output/site-preview/index.html'
backup=ROOT/'output/identity-backup/home-before-real-photos.html'
if not backup.exists():backup.write_bytes(page.read_bytes())
dest=ROOT/'output/site-preview/assets/clinic-photos';dest.mkdir(exist_ok=True)
files={'unnamed (5).webp':'entrance.webp','unnamed (4).webp':'hallway-detail.webp','unnamed (3).webp':'reception-wide.webp','unnamed (2).webp':'hallway.webp','unnamed (1).webp':'lobby.webp','2026-07-15.jpg':'reception.jpg'}
for original,name in files.items():copy2(Path('C:/Users/yutin/Downloads')/original,dest/name)
doc=html.fromstring(page.read_text(encoding='utf-8'))
def cls(name):return doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," '+name+' ")]')
hero=cls('lbh4-hero')[0]
new=html.fromstring('''<section class="lbh4-hero home-real-hero"><div class="lbh4-wrap home-hero-grid"><div class="home-hero-text"><p class="home-eyebrow">LIEN BANG TCM · 台北松山</p><h1>連邦中醫診所</h1><p class="home-hero-lead">從身體的不適，<br>開始好好照顧自己。</p><p class="home-hero-description">中醫內科・針灸傷科・日常調理</p><div class="lbh4-actions"><a class="lbh4-btn primary" href="https://lin.ee/UWWKmse" target="_blank" rel="noopener noreferrer">LINE 預約</a><a class="lbh4-btn" href="/symptoms/">查看常見症狀 ↗</a></div><p class="home-address">臺北市松山區南京東路四段 69 號 1 樓</p></div><figure class="home-hero-photo"><img src="/assets/clinic-photos/reception.jpg" alt="連邦中醫診所櫃台、品牌牆與暖色吊燈" width="1080" height="1440" fetchpriority="high"><figcaption>連邦中醫 · 診所實景</figcaption></figure></div></section>''')
hero.getparent().replace(hero,new)
# Exact approved illustrations accompany the existing sixteen symptom destinations.
directory=doc.get_element_by_id('common-symptoms')
for a in directory.xpath('.//div[@class="lb-symptom-options"]/a'):
    for old in a.findall('img'):a.remove(old)
    slug=a.get('href').strip('/').split('/')[-1]
    existing=a.find('span[@class="home-symptom-label"]')
    label=existing.text if existing is not None else (a.text or '')
    if existing is not None:
        for child in list(existing):a.append(child)
        a.remove(existing)
    a.text=None
    caption=html.Element('span',{'class':'home-symptom-label'});caption.text=label
    for old in list(a):caption.append(old)
    a.append(caption)
    a.insert(0,html.Element('img',src=f'/assets/illustrations/reference-crops/{slug}.png',alt='',loading='lazy',width='328',height='350'))
head=directory.xpath('.//div[@class="lbh4-head"]')[0]
if not head.xpath('.//a'):
    head.append(html.fromstring('<a class="home-all-symptoms" href="/symptoms/">瀏覽所有症狀 ↗</a>'))
# Place intuitive symptom navigation immediately after the three visit shortcuts.
quick=cls('lbh4-quick')[0]
directory.getparent().remove(directory);quick.addnext(directory)
# Real-space photographs accompany the existing clinic story without rewriting it.
about=cls('lbh4-about')[0]
for old in about.xpath('./figure[@class="home-story-photo"]'):about.remove(old)
about.insert(0,html.fromstring('<figure class="home-story-photo"><img src="/assets/clinic-photos/hallway.webp" alt="連邦中醫診間走廊與候診長椅" width="765" height="1020" loading="lazy"></figure>'))
for old in doc.xpath('//section[@id="clinic-space"]'):old.getparent().remove(old)
gallery=html.fromstring('''<section class="lbh4-section home-space" id="clinic-space"><div class="lbh4-wrap"><div class="lbh4-head"><div><p class="lbh4-kicker">OUR SPACE</p><h2>來連邦，先認識環境</h2></div></div><div class="home-space-grid"><figure><img src="/assets/clinic-photos/entrance.webp" alt="連邦中醫診所入口與招牌" width="765" height="1020" loading="lazy"><figcaption><span>01</span> 診所入口</figcaption></figure><figure><img src="/assets/clinic-photos/reception-wide.webp" alt="診所櫃台與候診區實景" width="765" height="1020" loading="lazy"><figcaption><span>02</span> 櫃台與候診區</figcaption></figure><figure><img src="/assets/clinic-photos/lobby.webp" alt="從診所內看入口與接待空間" width="765" height="1020" loading="lazy"><figcaption><span>03</span> 接待空間</figcaption></figure></div><p class="home-space-note">初次就診或門診問題，歡迎先透過 LINE 詢問。</p></div></section>''')
info=doc.get_element_by_id('clinic-info');info.addprevious(gallery)
for link in doc.xpath('//link[contains(@href,"home-real-photos.css")]'):link.getparent().remove(link)
doc.find('body').append(html.Element('link',rel='stylesheet',href='/assets/home-real-photos.css?v=1'))
page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
print('Homepage updated; original photos copied without pixel edits. Local preview only.')
