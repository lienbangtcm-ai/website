import { readFile, writeFile } from 'node:fs/promises';
const file = new URL('./premium-home-v4.html', import.meta.url);
const image = new URL('./lienbang-integrated-hero-v2.png', import.meta.url);
let html = await readFile(file, 'utf8');
const bytes = await readFile(image);
const dataUri = `data:image/png;base64,${bytes.toString('base64')}`;
html = html.replace(/src="https:\/\/lienbangtcm\.tw\/storage\/twyuting10210314859\/2026\/07\/clipboard-3-1024x576\.png"/, `src="${dataUri}"`);
await writeFile(file, html, 'utf8');
console.log(`Embedded hero image (${bytes.length} bytes).`);
