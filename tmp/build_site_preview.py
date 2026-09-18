from pathlib import Path
import re, html, shutil, json
root=Path(__file__).resolve().parents[1]
dest=root/'output/site-preview'
dest.mkdir(exist_ok=True)
template=(root/'output/insomnia/insomnia-review.html').read_text(encoding='utf-8')
header='''<header class="preview-header"><a class="preview-brand" href="/" aria-label="連邦中醫首頁">連邦中醫</a><nav aria-label="主要選單"><a href="/">首頁</a><a href="/services/">治療服務</a><a href="/symptoms/">常見症狀</a><a href="https://lienbangtcm.tw/team/">醫師團隊</a><a href="https://lienbangtcm.tw/health-blog/">健康專欄</a><a href="/about-lienbang/">關於連邦</a><a href="https://lienbangtcm.tw/support/">門診與交通</a><a class="preview-line" href="https://lin.ee/UWWKmse" target="_blank" rel="noopener noreferrer">LINE 預約</a></nav></header>'''
css='''<style>html,body{margin:0;overflow-x:hidden}.preview-header{display:flex;justify-content:space-between;align-items:center;gap:28px;padding:18px max(24px,calc((100% - 1240px)/2));background:#fff;color:#3f332e;font:700 15px/1.6 "Noto Sans TC","PingFang TC","Microsoft JhengHei",sans-serif;border-bottom:1px solid #e4d9cd}.preview-header a{text-decoration:none;color:inherit;white-space:nowrap}.preview-header nav{display:flex;align-items:center;justify-content:flex-end;gap:22px;flex-wrap:wrap}.preview-brand{color:#4a3028!important;font-size:22px;letter-spacing:.08em}.preview-line{padding:9px 16px;border-radius:999px;background:#4a3028;color:#fff!important}.preview-related{padding:30px 24px;text-align:center;background:#f7f2e9;color:#4a3028}.preview-related a{display:inline-block;margin:8px 16px}.lbh4,.lbsv,.lbft,.lbsym{width:100%!important;margin-left:0!important;margin-top:0!important}section[id]{scroll-margin-top:24px}@media(max-width:900px){.preview-header{display:block;padding:18px 20px 0}.preview-brand{display:block;padding-bottom:16px;text-align:center}.preview-header nav{display:grid;grid-template-columns:1fr 1fr;margin:0 -20px;gap:0;border-top:1px solid #e4d9cd;font-size:14px}.preview-header nav a,.preview-line{display:flex;align-items:center;justify-content:center;min-height:48px;margin:0;padding:0 8px!important;border-right:1px solid #e4d9cd;border-bottom:1px solid #e4d9cd;border-radius:0;background:#fff;color:#4a3028!important;text-align:center}.preview-header nav a:nth-child(2n){border-right:0}.preview-article .preview-header{padding-top:12px}.preview-article .preview-brand{padding-bottom:10px;font-size:19px}.preview-article .preview-header nav{grid-template-columns:repeat(4,1fr);font-size:12px}.preview-article .preview-header nav a,.preview-article .preview-line{min-height:40px;padding:0 3px!important}.preview-article .preview-header nav a:nth-child(2n){border-right:1px solid #e4d9cd}.preview-article .preview-header nav a:nth-child(4n){border-right:0}}a:focus-visible{outline:3px solid #b68a6b;outline-offset:-3px}</style>'''
articles={'gerd':'胃食道逆流','insomnia':'失眠','neck-shoulder-pain':'肩頸痛','low-back-pain':'腰背痛','cough':'咳嗽','allergic-rhinitis':'鼻過敏','diarrhea':'腹瀉','constipation':'便秘','menstrual-pain':'經痛','fatigue':'疲倦','frozen-shoulder':'五十肩','sciatica':'坐骨痛','knee-pain':'膝痛','tennis-elbow':'網球肘','de-quervain':'媽媽手','plantar-heel-pain':'足底痛'}
pain_articles={'neck-shoulder-pain','low-back-pain','frozen-shoulder','sciatica','knee-pain','tennis-elbow','de-quervain','plantar-heel-pain'}
related='<aside class="preview-related" aria-label="其他症狀文章"><a href="/symptoms/">常見症狀</a>'+''.join(f'<a href="/symptoms/{slug}/">{title}</a>' for slug,title in articles.items())+'</aside>'
routes={
 '/':root/'lienbang-assets/premium-home-v4.html',
 '/services/':root/'output/services-page.html',
 '/symptoms/':root/'output/featured-treatments.html',
 '/about-lienbang/':root/'output/about-lienbang/about-lienbang-final.html',
 '/acupuncture/':root/'output/acupuncture/acupuncture-final.html',
 '/pulse-diagnosis/':root/'output/pulse-diagnosis/pulse-diagnosis-final.html',
 '/acupuncture-physical-therapy/':root/'output/integration-page.html',
 '/針刀/':root/'output/selfpay-content/acupotomy.html',
 '/浮針/':root/'output/selfpay-content/fsn.html',
 '/美顏針/':root/'output/selfpay-content/facial-acupuncture.html',
 '/埋線/':root/'output/selfpay-content/acupoint-embedding.html'}

def render(content):
 out=[]
 for block in content.strip().split('\n\n'):
  if block.startswith('### '): out.append('<h3>'+html.escape(block[4:])+'</h3>')
  elif block.startswith('- '):out.append('<ul>'+''.join('<li>'+html.escape(x[2:])+'</li>' for x in block.splitlines())+'</ul>')
  else:out.append('<p>'+html.escape(block)+'</p>')
 return '\n'.join(out)

for slug,title in articles.items():
 if slug=='gerd':
  doc=(root/'output/symptom-article-demo/gerd-illustrated.html').read_text(encoding='utf-8')
  shutil.copytree(root/'output/symptom-article-demo/images',dest/'symptoms/gerd/images',dirs_exist_ok=True)
 elif slug=='insomnia':
  doc=template
  shutil.copytree(root/'output/insomnia/images',dest/'symptoms/insomnia/images',dirs_exist_ok=True)
 else:
  md=(root/f'output/symptom-article-drafts/{slug}.md').read_text(encoding='utf-8')
  md=re.sub('大部分患者的([^。]+)可以獲得良好改善。',r'治療目標是改善\1，實際變化需依回診評估追蹤。',md)
  md=md.replace('大部分患者可以獲得良好改善。','治療目標是減輕疼痛並改善日常功能，實際反應因人而異。')
  parts=re.split(r'^## ',md,flags=re.M)
  lead=parts[0].split('\n\n',1)[1].strip()
  doc=template.split('<body>')[0].replace('失眠｜',title+'｜')
  doc=re.sub(r'<meta name="description"[^>]+>',f'<meta name="description" content="{title}的常見表現、相關因素、中醫辨證、針灸傷科評估與日常照護。">',doc)
  chunks=[p.split('\n',1) for p in parts[1:] if not p.startswith('預約與門診資訊')]
  doc+='<body><article class="lb-article"><header class="lb-hero"><div class="lb-shell lb-hero-grid"><h1>'+title+'</h1><p class="lb-lead">'+lead+'</p></div></header>'
  doc+='<nav class="lb-nav" aria-label="文章段落導覽"><div class="lb-nav-inner">'+''.join(f'<a href="#section-{i}">{t}</a>' for i,(t,c) in enumerate(chunks))+'</div></nav>'
  for i,(t,c) in enumerate(chunks):
   body=render(c)
   if t=='常見問題':body='<div class="lb-faq">'+''.join('<details><summary>'+x.split('\n',1)[0]+'</summary><div class="lb-answer">'+render(x.split('\n',1)[1])+'</div></details>' for x in c.split('### ')[1:])+'</div>'
   doc+=f'<section class="lb-section {"lb-section--soft" if i%2 else ""}" id="section-{i}"><div class="lb-shell lb-narrow"><h2>{t}</h2>{body}</div></section>'
  cta=template[template.index('  <section class="lb-cta">'):]
  if slug in pain_articles:
   cta=cta.replace('就診前可先準備一至兩週睡眠紀錄，以及目前使用的處方藥、成藥與保健品，由醫師安排問診與脈診辨證。','就診時可說明疼痛位置、持續時間、誘發動作、外傷史及麻木或無力的情況，並攜帶目前用藥及檢查資料。')
  else:
   cta=cta.replace('就診前可先準備一至兩週睡眠紀錄，以及目前使用的處方藥、成藥與保健品，由醫師安排問診與脈診辨證。','就診前可先記錄症狀開始時間、最明顯的時段、誘發情境與伴隨症狀，並攜帶目前用藥及檢查資料。')
  doc+=cta
 routes['/symptoms/'+slug+'/']=doc

known=set(routes)
def local_link(m):
 url=m.group(1)
 if url.startswith('https://lienbangtcm.tw'):url=url[len('https://lienbangtcm.tw'):]
 path=url.split('#')[0].split('?')[0]
 if path in known:return 'href="'+url+'"'
 if url.startswith('/') and not url.startswith('//'):return 'href="https://lienbangtcm.tw'+url+'"'
 return 'href="'+url+'"'

for route,source in routes.items():
 doc=source.read_text(encoding='utf-8') if isinstance(source,Path) else source
 doc=re.sub(r'margin-top:\s*-(?:110|120)px', 'margin-top:0', doc)
 doc=doc.replace('margin:-120px 0 0','margin:0')
 if route=='/about-lienbang/':
  doc=doc.replace('<div class="lb-about-title" aria-hidden="true">關於連邦｜一個從台大開始的約定</div>','<h1 class="lb-about-title">關於連邦｜一個從台大開始的約定</h1>')
 if route=='/acupuncture/':
  for key,name in [('NO_RETENTION_HERO_URL','no-retention-acupuncture-hero.webp'),('NO_RETENTION_ASSESSMENT_URL','no-retention-acupuncture-assessment.webp')]:
   (dest/'acupuncture').mkdir(exist_ok=True)
   shutil.copy2(root/'output/acupuncture'/name,dest/'acupuncture'/name)
   doc=doc.replace('{{'+key+'}}','/acupuncture/'+name)
 if route=='/':
  doc=doc.replace('特色治療','常見症狀')
 if route=='/symptoms/':
  doc=doc.replace('特色治療','常見症狀')
  for slug,title in articles.items():
   label='胃逆流' if slug=='gerd' else title
   doc=doc.replace('>'+label+'</li>',f'><a href="/symptoms/{slug}/">{title}</a></li>')
 doc=re.sub(r'href="([^"]+)"',local_link,doc)
 if '<head>' not in doc:
  doc='<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>連邦中醫診所</title></head><body>'+doc+'</body></html>'
 doc=doc.replace('</head>','<meta name="robots" content="noindex,nofollow">'+css+'</head>')
 body_start='<body class="preview-article">' if route.startswith('/symptoms/') and route!='/symptoms/' else '<body>'
 doc=doc.replace('<body>',body_start+header,1).replace('</body>',related+'</body>')
 target=dest/route.strip('/')/'index.html'
 target.parent.mkdir(parents=True,exist_ok=True)
 target.write_text(doc,encoding='utf-8')

(dest/'robots.txt').write_text('User-agent: *\nDisallow: /\n')
(root/'output/PREVIEW_RELEASE_PLAN.md').write_text('''# 整批預覽與發布

目前階段：本機預覽，未上傳、未替換正式頁面。

第一批新症狀頁：胃食道逆流（原完成版）、失眠、肩頸痛、腰背痛。
整合頁：首頁、常見症狀入口。
同站預覽現有頁：治療服務、關於連邦、一般針灸、脈診辨證、針灸整合物理治療、針刀、浮針、美顏針、埋線。
醫師團隊、健康專欄、門診交通及原文章仍連正式站，未冒稱已改版。

使用者決定先一次預覽，確認後整批上傳並替換頁面。本機症狀路徑只是預覽路徑，尚未建立正式 canonical 或 Sitemap。
三篇新文章尚未配置圖片；胃食道逆流沿用既有圖片。沒有虛构患者案例。
LINE：既有頁 UWWKmse 與技能固定 NMa1es5 不一致，發布前須統一確認。

發布準備：備份待替換的正式頁內容與媒體對照；確認既有相關文章的網址，避免建立重複症狀頁；依審閱後定稿更新內容與首頁入口；成功發布後驗證連結、圖片、canonical、手機版與 Sitemap。

醫療查核：
- https://www.nccih.nih.gov/health/acupuncture-effectiveness-and-safety
- https://www.nccih.nih.gov/health/low-back-pain-and-complementary-health-approaches-what-you-need-to-know
- https://www.nhs.uk/symptoms/neck-pain-and-stiff-neck/
''',encoding='utf-8')
print(f'Built {len(routes)} local preview pages at {dest}')
import runpy
runpy.run_path(str(root/'tmp/apply_shared_preview.py'))
if (root/'output/article-images-three-plan.json').exists():
 runpy.run_path(str(root/'tmp/install_article_images.py'))
