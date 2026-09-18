import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(import.meta.dirname, '..');
const logo = 'https://lienbangtcm.tw/storage/twyuting10210314859/2021/07/%E9%80%A3%E9%82%A6%E4%B8%AD%E9%86%AB%E7%99%BDlogo.png';
const cssLink = '<link rel="stylesheet" href="/assets/global-shell.css?v=1">';
const header = `<header class="global-header"><a class="global-brand" href="/" aria-label="連邦中醫診所首頁"><img src="${logo}" alt="連邦中醫診所" width="2362" height="470"></a><nav aria-label="主要選單"><a href="/">首頁</a><a href="/about-lienbang/">關於連邦</a><a href="/services/">治療服務</a><a href="/symptoms/">常見症狀</a><a href="https://lienbangtcm.tw/team/">醫師團隊</a><a href="https://lienbangtcm.tw/health-blog/">衛教文章</a><a href="https://lienbangtcm.tw/support/">交通資訊</a></nav><a class="global-booking" href="https://lin.ee/UWWKmse">線上預約</a></header>`;
const footer = `<footer id="site-footer" class="global-footer"><div class="global-footer-main"><a class="global-footer-brand" href="/" aria-label="連邦中醫診所首頁"><img src="${logo}" alt="連邦中醫診所" width="2362" height="470" loading="lazy"><p>從問診、辨證到治療評估，陪你理解身體，找回生活的節奏。</p></a><section class="global-footer-links" aria-label="網站導覽"><h2>網站導覽</h2><nav><a href="/">首頁</a><a href="/about-lienbang/">關於連邦</a><a href="/services/">治療服務</a><a href="/symptoms/">常見症狀</a><a href="https://lienbangtcm.tw/team/">醫師團隊</a><a href="https://lienbangtcm.tw/health-blog/">衛教文章</a><a href="https://lienbangtcm.tw/support/">交通資訊</a></nav></section><section class="global-footer-contact" aria-label="預約與聯絡資訊"><h2>預約與門診資訊</h2><address>臺北市松山區南京東路四段69號1樓</address><a class="global-footer-phone" href="tel:+886225795059">02-2579-5059</a><br><a class="global-footer-line" href="https://lin.ee/UWWKmse">LINE 預約</a></section></div><div class="global-footer-bottom"><p>© 2026 連邦中醫診所 版權所有</p><p>LIEN BANG TRADITIONAL CHINESE MEDICINE</p></div></footer>`;

function collectIndexFiles(dir, files = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) collectIndexFiles(full, files);
    else if (entry.name.toLowerCase() === 'index.html') files.push(full);
  }
  return files;
}

let changed = 0;
for (const file of collectIndexFiles(root)) {
  let html = fs.readFileSync(file, 'utf8');
  const before = html;
  if (!html.includes('/assets/global-shell.css')) html = html.replace('</head>', `${cssLink}</head>`);
  html = html.replace(/<header class="(?:site-header|preview-header)"[\s\S]*?<\/header>/, header);
  html = html.replace('<footer class="global-footer">', '<footer id="site-footer" class="global-footer">');
  if (html.includes('<footer') && !html.includes('class="global-footer"')) {
    html = html.replace(/<footer(?:\s[^>]*)?>[\s\S]*?<\/footer>/, footer);
  } else if (!html.includes('class="global-footer"')) {
    html = html.replace('</body>', `${footer}</body>`);
  }
  if (html !== before) {
    fs.writeFileSync(file, html);
    changed += 1;
  }
}
console.log(`Synchronized global header/footer in ${changed} pages.`);
