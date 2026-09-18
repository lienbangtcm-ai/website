from pathlib import Path
from lxml import html
import shutil,urllib.request
root=Path('output/site-preview');p=root/'index.html';s=p.read_text(encoding='utf-8');backup=Path('output/release-audit/home-v22.html')
if not backup.exists():backup.write_text(s,encoding='utf-8')
d=html.fromstring(s);main=d.xpath('//main')[0];assets=root/'assets/doctors';assets.mkdir(exist_ok=True)
doctors=[('張豫','院長','脈診辨證・中醫內科','profile','https://lienbangtcm.tw/storage/twyuting10210314859/2026/07/LINE_ALBUM_202378%E5%85%A8%E5%AE%B6%E7%A6%8F%E7%85%A7%E7%89%87-%E5%80%8B%E4%BA%BA%E5%BD%A2%E8%B1%A1%E7%85%A7_260206_1-Photoroom.png'),('戴宣元','醫師','譚氏平衡針法・美顏針','dai-xuan-yuan','https://lienbangtcm.tw/storage/twyuting10210314859/2026/07/dai-xuan-yuan-doctor-profile.jpg'),('張祐銘','醫師','中醫內科・婦兒體質','zhang-you-ming',''),('蔡如慧','醫師','女性健康・美顏針灸','tsai-ru-hui','')]
cards=[]
for name,role,desc,slug,url in doctors:
 ext='.jpg' if slug=='dai-xuan-yuan' else '.png';dest=assets/(slug+ext)
 if url:
  if not dest.exists():
   req=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'});dest.write_bytes(urllib.request.urlopen(req,timeout=30).read())
 else:shutil.copy2(Path('lienbang-site-audit/new-doctors-2026-07-28')/(slug+'-doctor.png'),dest)
 cards.append(f'<a href="https://lienbangtcm.tw/{slug}/"><img src="/assets/doctors/{slug}{ext}" alt="{name}{role}" loading="lazy"><h3>{name} <small>{role}</small></h3><p>{desc}</p><span>了解醫師 →</span></a>')
team=html.fragment_fromstring('<section class="hr-section hr-doctors"><div class="hr-wrap"><div class="hr-heading"><h2>醫師介紹</h2><p>以人為本，從傾聽開始。</p><a href="https://lienbangtcm.tw/team/">查看醫師團隊 →</a></div><div class="hr-doctor-grid">'+''.join(cards)+'</div></div></section>')
about=d.xpath('//section[@class="hr-about"]')[0];about.addprevious(team)
articles=[]
for slug,label,desc in [('insomnia','失眠','了解睡眠困擾的評估與日常照護。'),('gerd','胃食道逆流','了解胃食道逆流與生活照護方向。'),('allergic-rhinitis','鼻過敏','了解鼻部不適與日常照護。')]:
 doc=html.fromstring((root/'symptoms'/slug/'index.html').read_text(encoding='utf-8'));imgs=doc.xpath('//main//img/@src');src=next((i for i in imgs if 'hero' in i),imgs[0] if imgs else f'/assets/illustrations/reference-crops/{slug}.png')
 if not src.startswith(('http','/')):src=f'/symptoms/{slug}/'+src
 articles.append(f'<a href="/symptoms/{slug}/"><img src="{src}" alt="" loading="lazy"><div><h3>{label}</h3><p>{desc}</p><span>閱讀全文 →</span></div></a>')
about.addprevious(html.fragment_fromstring('<section class="hr-section hr-articles"><div class="hr-wrap"><div class="hr-heading"><h2>文章導覽／健康專欄</h2><a href="https://lienbangtcm.tw/health-blog/">查看全部文章 →</a></div><div class="hr-article-grid">'+''.join(articles)+'</div></div></section>'))
about.xpath('.//img')[0].set('src','/assets/clinic-photos/reception.jpg');about.xpath('.//img')[0].set('alt','連邦中醫實際櫃台與品牌牆')
info=d.xpath('//*[@id="clinic-info"]')[0]
info.clear();info.set('id','clinic-info');info.set('class','hr-section')
info.append(html.fragment_fromstring('''<div class="hr-wrap"><div class="hr-heading"><h2>門診與交通</h2></div><div class="hr-contact-grid"><div><dl><dt>地址</dt><dd>105臺北市松山區南京東路四段69號1樓</dd><dt>電話</dt><dd><a href="tel:+886225795059">02-2579-5059</a></dd><dt>預約</dt><dd><a href="https://lin.ee/UWWKmse">官方 LINE 預約與門診詢問</a></dd><dt>門診時間</dt><dd><a href="https://lienbangtcm.tw/support/#clinic-hours">查看目前門診資訊 →</a></dd></dl><p>最新門診異動請以官方 LINE 公告為準。</p><div class="hr-actions"><a class="hr-btn" href="https://www.google.com/maps/search/?api=1&amp;query=105臺北市松山區南京東路四段69號1樓">地圖／交通 →</a><a class="hr-btn" href="https://lin.ee/UWWKmse">LINE 預約 →</a></div></div><iframe title="連邦中醫診所位置地圖" src="https://maps.google.com/maps?q=105%E8%87%BA%E5%8C%97%E5%B8%82%E6%9D%BE%E5%B1%B1%E5%8D%80%E5%8D%97%E4%BA%AC%E6%9D%B1%E8%B7%AF%E5%9B%9B%E6%AE%B569%E8%99%9F&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div></div>'''))
for e in d.xpath('//aside[@class="preview-related"]'):e.getparent().remove(e)
footer=html.fragment_fromstring('<footer class="hr-footer"><div class="hr-wrap"><strong>連邦中醫診所</strong><nav><a href="/">首頁</a><a href="/services/">治療服務</a><a href="/symptoms/">常見症狀</a><a href="https://lienbangtcm.tw/team/">醫師團隊</a><a href="/about-lienbang/">關於連邦</a></nav><p>臺北市松山區南京東路四段69號1樓<br><a href="tel:+886225795059">02-2579-5059</a></p></div></footer>');main.addnext(footer)
d.xpath('//body')[0].append(html.fragment_fromstring('<link rel="stylesheet" href="/assets/home-polish.css?v=23">'))
p.write_text('<!doctype html>\n'+html.tostring(d,encoding='unicode'),encoding='utf-8')
