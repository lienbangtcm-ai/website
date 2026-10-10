from pathlib import Path
for f in [Path('output/site-preview/services/index.html'),Path('output/site-preview/dist/services/index.html')]:
 t=f.read_text(encoding='utf-8').replace('<link rel="stylesheet" href="/assets/services-compact-20261009.css">\n','');f.write_text(t,encoding='utf-8')
css='''
/* Slightly smaller expanded menu, retaining clear service photographs. */
@media(min-width:821px){
.global-header .global-treatment-menu{width:min(1000px,calc(100vw - 48px))!important;padding:20px!important}
.global-header .global-treatment-grid{gap:14px!important}
.global-header .global-treatment-menu-head>strong{font-size:23px!important}
.global-header .global-treatment-card img{height:115px!important}
.global-header .global-treatment-card>span{padding:12px 14px 0!important}
.global-header nav .global-treatment-card{padding-bottom:13px!important}
.global-header .global-treatment-card strong{font-size:19px!important}
.global-header .global-treatment-card small{font-size:14px!important}
}
'''
for f in [Path('output/site-preview/assets/global-shell.css'),Path('output/site-preview/dist/assets/global-shell.css')]:f.write_text(f.read_text(encoding='utf-8')+css,encoding='utf-8')
