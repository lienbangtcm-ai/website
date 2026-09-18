const fs = require('fs');
const path = require('path');

const root = path.resolve(process.argv[2]);
const files = [];
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    else files.push(full);
  }
}
walk(root);

const htmlFiles = files.filter((file) => file.endsWith('.html'));
const missing = [];
for (const file of htmlFiles) {
  const html = fs.readFileSync(file, 'utf8');
  const refs = [...html.matchAll(/(?:href|src)=["']([^"']+)["']/gi)].map((match) => match[1]);
  for (const ref of refs) {
    if (!ref || ref.startsWith('#') || /^(?:https?:|mailto:|tel:|data:|javascript:)/i.test(ref)) continue;
    const pathname = decodeURIComponent(ref.split(/[?#]/)[0]);
    if (!pathname) continue;
    let target = pathname.startsWith('/')
      ? path.join(root, pathname.replace(/^\/+/, ''))
      : path.resolve(path.dirname(file), pathname);
    if (pathname.endsWith('/')) target = path.join(target, 'index.html');
    if (!fs.existsSync(target)) missing.push(path.relative(root, file) + ' -> ' + ref);
  }
}

console.log(JSON.stringify({ htmlFiles: htmlFiles.length, totalFiles: files.length, missing }, null, 2));
if (missing.length) process.exit(1);
