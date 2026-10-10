from pathlib import Path
for f in [Path('output/site-preview/index.html'),Path('output/site-preview/dist/index.html')]:
 t=f.read_text(encoding='utf-8').replace('<p>探索你所需要的<br>調理方式</p>','')
 f.write_text(t,encoding='utf-8')
p=Path('output/site-preview/assets/service-cards-unified.css')
p.write_text(p.read_text(encoding='utf-8')+'\n/* Service section heading: one clear title and a single overview link. */\n.home-reference-match .services-showcase .section-intro{display:flex!important;align-items:center!important;justify-content:space-between!important;flex-wrap:nowrap!important;gap:20px!important;margin-bottom:28px!important;padding:0!important;min-height:0!important}\n.home-reference-match .services-showcase .section-intro h2{flex-shrink:0;line-height:1.4!important}\n.home-reference-match .services-showcase .section-intro a{position:static!important;display:block!important;flex-shrink:0;margin:0!important;line-height:1.6!important;text-align:right}\n@media(max-width:760px){.home-reference-match .services-showcase .section-intro{gap:12px!important;margin-bottom:20px!important}.home-reference-match .services-showcase .section-intro a{font-size:12px!important}}\n',encoding='utf-8')
