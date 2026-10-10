from pathlib import Path
import re
root=Path('output/site-preview');home=(root/'index.html').read_text(encoding='utf-8');block=re.search(r'<div class="service-cards">(.*?)</div></div></section>',home,re.S)[1];labels=re.findall(r'<h3>(.*?)</h3><p>(.*?)</p>',block,re.S)
for f in root.rglob('index.html'):
 if 'review' in f.parts:continue
 t=f.read_text(encoding='utf-8');i=[0]
 def update(m):
  n=i[0];i[0]+=1
  if n>=6:return m[0]
  return re.sub(r'<strong>.*?</strong><small>.*?</small>',lambda _:'<strong>'+labels[n][0]+'</strong><small>'+labels[n][1]+'</small>',m[0],flags=re.S)
 t=re.sub(r'<a class="global-treatment-card".*?</a>',update,t,flags=re.S)
 if f.parent.name=='針刀' and '了解浮針療程' not in t:
  t=t.replace('<div class="su-actions"><a href="https://lin.ee/UWWKmse">LINE 預約諮詢</a></div>','<div class="su-actions"><a href="https://lin.ee/UWWKmse">LINE 預約諮詢</a><a href="/%E6%B5%AE%E9%87%9D/">了解浮針療程</a></div>')
 f.write_text(t,encoding='utf-8')
# Remove obsolete preservation claims from the report: later homepage edits were authorized.
p=Path('tools/build-home-system-review.py');t=p.read_text(encoding='utf-8-sig');t=t.replace('首頁原始 HTML 未變更；其他頁面保留文字、SEO、Schema、追蹤腳本與連結。','首頁依後續指示同步六項服務圖片、雙語標題、對齊與移除圓圈箭頭；醫療內容、SEO、Schema、追蹤腳本與既有目的連結保留。');t=t.replace('手機首頁截圖像素相同；桌機第一張服務照片有瀏覽器解碼像素差異，首頁原始碼與幾何尺寸未改動。','六個服務頁已統一主視覺、章節導覽、流程卡片與預約區；各頁長度依原始內容保留差異。');p.write_text(t,encoding='utf-8')
