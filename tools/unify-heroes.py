from pathlib import Path
import re, json

root = Path('output/site-preview')
if 'data-hero-system' in (root/'about-lienbang/index.html').read_text(encoding='utf-8'):
    raise SystemExit('One-time migration already applied; edit the shared hero stylesheet for follow-up changes.')
routes = {'about-lienbang':'ab-hero','services':'to-hero','team':'team-hero','symptoms':'lbsym-hero','articles':'lbsym-hero'}
for x in ['pulse-diagnosis','acupuncture','acupuncture-physical-therapy','浮針','針刀','美顏針']: routes[x]='su-hero'
for p in (root/'symptoms').glob('*/index.html'): routes[str(p.parent.relative_to(root)).replace('\\','/')] = 'lb-hero'
for p in (root/'team').glob('*/index.html'): routes[str(p.parent.relative_to(root)).replace('\\','/')] = 'dp-hero'
subtitles = {'team':'不同專長，同一個照護方向','acupuncture':'依個別狀況，安排針灸照護','acupuncture-physical-therapy':'中醫與物理治療，從評估開始整合','浮針':'從患肌評估，了解疼痛與動作','針刀':'先確認來源，再評估軟組織處理','美顏針':'從臉部與整體狀態，討論調理方向','articles':'認識中醫，理解身體的日常變化'}
def addclass(html, name):
    if re.search(r'^<\w+[^>]*\bclass=',html): return re.sub(r'^(<\w+[^>]*\bclass=")',r'\1'+name+' ',html,count=1)
    return re.sub(r'^(<\w+)',r'\1 class="'+name+'"',html,count=1)
def para(text,cls): return '<p class="'+cls+'">'+text+'</p>'
changed=[]
for route, oldclass in routes.items():
    p=root/route/'index.html'; s=p.read_text(encoding='utf-8')
    m=re.search(r'<(section|header)\b[^>]*class="[^"]*\b'+oldclass+r'\b[^>]*>',s)
    assert m,route
    end=s.index('</'+m[1]+'>',m.end())+len(m[1])+3; old=s[m.start():end]
    h=re.search(r'<h1\b[^>]*>.*?</h1>',old,re.S)[0]; title=re.sub('<[^>]+>','',h)
    paragraphs=re.findall(r'<p\b[^>]*>.*?</p>',old,re.S)
    links=re.findall(r'<a\b[^>]*>.*?</a>',old,re.S)
    kicker=next((x for x in paragraphs if re.search('eyebrow|kicker|brand',x)),None)
    other=[x for x in paragraphs if x!=kicker and not re.search('aria-hidden|hero-english',x)]
    summary=''; subtitle=''; media=''; extra=''
    kind='overview'
    if oldclass=='su-hero':
        kind='service'; photo=re.search(r"url\(['\"]?([^'\"\)]+)",old)[1]
        if route=='pulse-diagnosis': subtitle=other[0];summary=other[1]
        else: subtitle=para(subtitles[route],'');summary=other[0]
        media='<figure class="vh-media"><img src="'+photo+'" alt="'+title+'照護情境" decoding="async"></figure>'
    elif oldclass=='lb-hero':
        kind='article'; kicker=para('SYMPTOM GUIDE','')
        recognition=next((x for x in other if 'msk-recognition' in x),None)
        subtitle=recognition or para(title+'的評估與日常照護','')
        summary=next(x for x in other if 'lb-lead' in x)
        media=re.search(r'<figure\b.*?</figure>',old,re.S)[0]
    elif oldclass=='dp-hero':
        kind='profile'; subtitle=next(x for x in other if 'dp-role' in x)
        summary=re.search(r'<div class="dp-tags">.*?</div>',old,re.S)[0]
        img=re.search(r'<img\b[^>]*>',old)[0];media='<figure class="vh-media">'+img+'</figure>'
        aside=re.search(r'<div class="dp-hero-aside">.*?</div>',old,re.S)
        if aside:extra='<div class="vh-profile-note">'+aside[0]+'</div>'
    elif route=='about-lienbang':
        kicker=para('ABOUT LIEN BANG',''); subtitle=other[0];summary=other[1]
        media=re.search(r'<figure\b.*?</figure>',old,re.S)[0]
    elif route=='services':
        kicker=para('OUR SERVICES','');subtitle=next(x for x in other if 'to-lead' in x);summary=next(x for x in other if 'to-summary' in x)
        media='<figure class="vh-media">'+re.search(r'<img\b[^>]*>',old)[0]+'</figure>'
    elif route=='team':
        subtitle=para(subtitles[route],'');summary=other[0]
        # Same existing team hero photograph as the stylesheet.
        css=s
        image=re.search(r'\.team-hero[^{}]*\{[^}]*url\([\'\"]?([^\'\"\)]+)',css)
        photo='/assets/user-20261009/team.webp'
        media='<figure class="vh-media"><img src="'+photo+'" alt="連邦診療照護情境" decoding="async"></figure>'
    else:
        subtitle=other[0];summary=other[1]
        photo='/assets/user-20261009/symptoms-hero.webp'
        if route=='articles':
            subtitle=para(subtitles[route],'')
            summary=para('從症狀解析、治療方式到日常照護，閱讀中醫觀點，了解就診評估時可以討論的問題。','')
            photo='/assets/user-20261009/pulse-hero.webp'
        media='<figure class="vh-media"><img src="'+photo+'" alt="'+title+'中醫照護情境" decoding="async"></figure>'
    if not links:links=['<a href="https://lin.ee/UWWKmse">LINE 預約諮詢</a>']
    links.sort(key=lambda x:0 if 'lin.ee' in x else 1)
    actions=''.join(addclass(x,'vh-primary' if i==0 else 'vh-secondary') for i,x in enumerate(links))
    content=addclass(kicker,'vh-eyebrow')+addclass(h,'vh-title')+addclass(subtitle,'vh-subtitle')+addclass(summary,'vh-summary')+'<div class="vh-actions">'+actions+'</div>'
    media=addclass(media,'vh-media') if 'class="vh-media"' not in media else media
    opening=addclass(m[0],'vh-hero vh-'+kind)
    new=opening+'<div class="vh-shell"><div class="vh-copy">'+content+'</div>'+media+'</div></'+m[1]+'>'+extra
    s=s[:m.start()]+new+s[end:]
    s=s.replace('</head>','<link rel="stylesheet" href="/assets/hero-consistent-20261011.css?v=1"></head>',1)
    s=re.sub(r'<body\b', '<body data-hero-system="20261011"',s,count=1)
    if route=='articles':
        s=s.replace('aria-label="症狀分類"','aria-label="衛教閱讀分類"').replace('>內科與體質</a>','>內科調理與日常照護</a>').replace('>筋骨疼痛與針灸</a>','>疼痛與治療知識</a>')
        s=s.replace('<h2>內科與體質</h2>','<h2>內科調理與日常照護</h2>').replace('<h2>筋骨疼痛與針灸</h2>','<h2>疼痛與治療知識</h2>')
    p.write_text(s,encoding='utf-8');dist=root/'dist'/route/'index.html'
    if dist.exists():dist.write_text(s,encoding='utf-8')
    changed.append(route)
print(json.dumps(changed,ensure_ascii=True))
