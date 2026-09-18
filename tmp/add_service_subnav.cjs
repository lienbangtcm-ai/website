const fs = require('fs');
const path = require('path');

const root = path.resolve('output/site-preview');
const pages = [
  ['acupuncture/index.html', '/acupuncture/'],
  ['acupuncture-physical-therapy/index.html', '/acupuncture-physical-therapy/'],
  ['針刀/index.html', '/%E9%87%9D%E5%88%80/'],
  ['浮針/index.html', '/%E9%87%9D%E5%88%80/'],
  ['美顏針/index.html', '/%E7%BE%8E%E9%A1%8F%E9%87%9D/'],
  ['埋線/index.html', '/%E5%9F%8B%E7%B7%9A/'],
];
const links = [
  ['/services/', '治療服務總覽'],
  ['/pulse-diagnosis/', '中醫內科／脈診'],
  ['/acupuncture/', '針灸'],
  ['/acupuncture-physical-therapy/', '中醫 × 物理治療'],
  ['/%E9%87%9D%E5%88%80/', '針刀／浮針'],
  ['/%E7%BE%8E%E9%A1%8F%E9%87%9D/', '美顏針'],
  ['/%E5%9F%8B%E7%B7%9A/', '埋線'],
];

for (const [relative, active] of pages) {
  const file = path.join(root, relative);
  let html = fs.readFileSync(file, 'utf8');
  if (!html.includes('/assets/service-subnav.css')) {
    html = html.replace(
      '<link rel="stylesheet" href="/assets/global-shell.css?v=1">',
      '<link rel="stylesheet" href="/assets/global-shell.css?v=1"><link rel="stylesheet" href="/assets/service-subnav.css?v=1">'
    );
  }
  if (!html.includes('class="service-subnav"')) {
    const nav = '<nav class="service-subnav" aria-label="治療服務分頁">' +
      links.map(([href, label]) => '<a href="' + href + '"' + (href === active ? ' aria-current="page"' : '') + '>' + label + '</a>').join('') +
      '</nav>';
    html = html.replace('</header>', '</header>' + nav);
  }
  fs.writeFileSync(file, html, 'utf8');
}
