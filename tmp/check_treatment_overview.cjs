const fs = require('fs');
const path = require('path');

const root = path.resolve('output/site-preview');
const html = fs.readFileSync(path.join(root, 'services/index.html'), 'utf8');
const ids = [...html.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
const duplicateIds = [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))];
const refs = [...html.matchAll(/(?:src|href)="(\/[^"#?]+)(?:[?#][^"]*)?"/g)]
  .map((match) => match[1])
  .filter((ref) => !ref.endsWith('/'));
const missingLocalFiles = [...new Set(refs.filter((ref) => !fs.existsSync(path.join(root, decodeURIComponent(ref.slice(1))))))];
const requiredIds = ['treatment-title'];
const missingRequiredIds = requiredIds.filter((id) => !ids.includes(id));
const result = {
  htmlBytes: html.length,
  ids: ids.length,
  duplicateIds,
  missingLocalFiles,
  missingRequiredIds,
  hasViewport: /name="viewport"/.test(html),
  hasTitle: /<title>[^<]+<\/title>/.test(html),
};

console.log(JSON.stringify(result, null, 2));
if (duplicateIds.length || missingLocalFiles.length || missingRequiredIds.length) process.exit(1);
