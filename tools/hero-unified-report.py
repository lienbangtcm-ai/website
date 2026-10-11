from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, shutil, html, subprocess, re

root=Path('output/site-preview');out=root/'review/hero-unified';out.mkdir(parents=True,exist_ok=True)
qa=Path('output/visual-qa/hero-unified-final');rows=json.loads((qa/'report.json').read_text(encoding='utf-8'))
baseline=Path('output/visual-qa/home-system/user-audit-final-20261011');full=Path('output/visual-qa/home-system/hero-unified-verified')
font=ImageFont.truetype('C:/Windows/Fonts/msjh.ttc',20)
desktop=[x for x in rows if x['width']==1440 and x['route']!='home'];montage=Image.new('RGB',(1440,240*10),'#fffdf9');draw=ImageDraw.Draw(montage)
sections=[];checks=[]
for i,x in enumerate(desktop):
    route=x['route'];name=route.replace('/','--');title=next(t for t in x['text'] if t['tag']=='H1')['text']
    im=Image.open(qa/x['file']).crop((0,96,1440,696)).resize((480,200));col=i%3;row=i//3;montage.paste(im,(col*480,row*240+32));draw.text((col*480+10,row*240+4),title,font=font,fill='#493023')
    cards=[]
    for width in [1440,390]:
        before=baseline/(name+'-'+str(width)+'.jpg');after=full/(name+'-'+str(width)+'.jpg')
        assert before.exists() and after.exists(),route
        bn='before-'+name+'-'+str(width)+'.jpg';an='after-'+name+'-'+str(width)+'.jpg';shutil.copy2(before,out/bn);shutil.copy2(after,out/an)
        # Hero snapshots support direct alignment comparison, full page images remain available.
        cn='hero-'+name+'-'+str(width)+'.jpg';shutil.copy2(qa/(name+'-'+str(width)+'.jpg'),out/cn)
        cards.append('<h3>'+str(width)+'px</h3><div class="pair"><figure><figcaption>修改前</figcaption><a href="'+bn+'"><img loading="lazy" src="'+bn+'"></a></figure><figure><figcaption>修改後</figcaption><a href="'+an+'"><img loading="lazy" src="'+an+'"></a></figure></div><a href="'+cn+'">查看修改後首屏</a>')
    sections.append('<details><summary>'+html.escape(title)+' <a href="/'+route+'/">操作頁面</a></summary>'+''.join(cards)+'</details>')
    for y in [z for z in rows if z['route']==route]:
        h=next(t for t in y['text'] if t['tag']=='H1');sub=next(t for t in y['text'] if 'vh-subtitle' in t['cls']);summ=next((t for t in y['text'] if 'vh-summary' in t['cls']),None)
        checks.append({'route':route,'viewport':y['width'],'title':h,'hero_height':y['hero']['height'],'overlap':bool(summ and sub['y']+sub['height']>summ['y']+1),'desktop_geometry_pass':y['width']!=1440 or (abs(h['x']-57)<1 and abs(h['y']-172)<1 and y['hero']['height']==600)})
montage.save(out/'all-heroes.jpg',quality=86)
(qa/'geometry-checks.json').write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
assert all(not x['overlap'] and x['desktop_geometry_pass'] for x in checks)
report='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>全站首屏統一｜修改前後驗收</title><style>body{max-width:1320px;margin:auto;padding:30px 20px;background:#fffdf9;color:#493023;font:18px/1.8 "Microsoft JhengHei",sans-serif}h1{font-size:32px}.pair{display:grid;grid-template-columns:1fr 1fr;gap:20px}figure{margin:0}img{max-width:100%;display:block}.pair img{max-height:720px;object-fit:contain;object-position:top;width:100%}details{border-top:1px solid #ddd;padding:20px 0}summary{cursor:pointer;font-weight:700}a{color:#8d5837}summary a{margin-left:20px;font-size:16px}@media(max-width:700px){.pair{grid-template-columns:1fr}}</style><h1>全站首屏統一：修改前後對照</h1><p>30 個內頁：五個總覽、六個療程、十六個症狀、三位醫師。首頁保留既有設計；已停止提供的埋線公告保留。</p><p>桌機標題統一 58px／700、副標 26px、摘要 19px、英文 12px、按鈕 16px；1440px 下左邊界 57px、標題上緣 172px、首屏高度 600px。手機改為內容自適應，標題 38px、副標 22px、摘要 17px，皆先文字後圖片。</p><p>保留修改前基準、第一至第三輪及最終截圖；最終 32 頁 × 1440／768／390px 共 96 組功能測試通過。圖片比例依人物照、情境照保留差異；沒有宣稱像素級完全相同。衛教與症狀仍引用同一批 16 篇醫療文章，閱讀分類與入口說明不同。</p><p>尚待人工確認：現有示意圖片的臨床適用性及新增導覽副標措辭。未部署正式 WordPress。此報告的修改前截圖來自本次修改前的 user-audit-final-20261011，修改後來自最終回歸測試。</p><h2>30 頁首屏並排檢視</h2><a href="all-heroes.jpg"><img src="all-heroes.jpg" alt="全部內頁首屏並排比較"></a><h2>逐頁桌機／手機完整截圖</h2>'''+''.join(sections)+'</html>'
(out/'index.html').write_text(report,encoding='utf-8')
print('30 pages, 60 before/after pairs, geometry and overlap checks passed')
