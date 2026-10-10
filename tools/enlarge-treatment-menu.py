from pathlib import Path
import re
root=Path('output/site-preview');home=(root/'index.html').read_text(encoding='utf-8');block=re.search(r'<div class="service-cards">(.*?)</div></div></section>',home,re.S).group(1);srcs=re.findall(r'<img[^>]*src="([^"]+)"',block)
for f in root.rglob('index.html'):
 t=f.read_text(encoding='utf-8');count=[0]
 def change(m):
  i=count[0];count[0]+=1
  return re.sub(r'src="[^"]+"',lambda _:f'src="{srcs[i]}"',m[0],count=1) if i<6 else m[0]
 t=re.sub(r'<a class="global-treatment-card"[^>]*><img[^>]+>',change,t)
 if count[0]:f.write_text(t,encoding='utf-8')
css='''
/* Large, readable treatment navigation; images match homepage service cards. */
@media(min-width:821px){
.global-header .global-treatment-menu{position:fixed!important;top:96px!important;left:50%!important;width:min(1160px,calc(100vw - 48px))!important;max-height:calc(100vh - 112px);overflow-y:auto;padding:24px!important;box-sizing:border-box}
.global-header .global-treatment-menu-head{padding:0 0 16px;margin-bottom:20px}
.global-header .global-treatment-menu-head>strong{font-size:26px!important}
.global-header .global-treatment-menu-head a{font-size:16px!important}
.global-header .global-treatment-grid{grid-template-columns:repeat(3,minmax(0,1fr))!important;gap:18px!important}
.global-header nav .global-treatment-card{display:block!important;padding:0 0 16px!important;border:1px solid #e6ddd3;border-radius:12px!important;overflow:hidden;text-align:left}
.global-header .global-treatment-card img{display:block;width:100%!important;height:140px!important;object-fit:cover;object-position:50% 42%;border-radius:0!important}
.global-header .global-treatment-card>span{display:block;padding:14px 16px 0}
.global-header .global-treatment-card strong{font-size:21px!important;line-height:1.5!important;overflow:visible}
.global-header .global-treatment-card small{font-size:15px!important;line-height:1.6!important;overflow:visible}
}
@media(min-width:821px) and (max-width:1100px){.global-header .global-treatment-menu{top:76px!important;max-height:calc(100vh - 92px)}.global-header .global-treatment-card strong{font-size:18px!important}}
'''
for f in [root/'assets/global-shell.css',root/'dist/assets/global-shell.css']:
 f.write_text(f.read_text(encoding='utf-8')+css,encoding='utf-8')
