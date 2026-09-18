const { chromium } = require('C:/Users/yutin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname,'../output/site-preview');
const out = path.resolve(__dirname,'../output/release-audit');
function pages(dir) { return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e => e.isDirectory()?pages(path.join(dir,e.name)):e.name==='index.html'?[path.join(dir,e.name)]:[]); }
(async()=>{
 const browser=await chromium.launch({headless:true,channel:'msedge'});
 const results=[];
 for(const width of [390,1440]) {
  const page=await browser.newPage({viewport:{width,height:900}});
  for(const file of pages(root)) {
   const route='/'+path.relative(root,file).replaceAll('\\','/').replace(/index\.html$/,'');
   if(process.argv.includes('--images-only') && !['/symptoms/gerd/','/symptoms/insomnia/'].includes(route)) continue;
   if(process.argv.includes('--about-only') && route!='/about-lienbang/') continue;
   await page.goto('http://127.0.0.1:8765'+route,{waitUntil:'networkidle'});
   await page.evaluate(async()=>{await Promise.all(Array.from(document.images).map(async i=>{i.loading='eager';await Promise.race([i.decode().catch(()=>{}),new Promise(r=>setTimeout(r,10000))])}))});
   await page.waitForTimeout(300);
   const data=await page.evaluate(()=>({
    title:document.title,
    overflow:document.documentElement.scrollWidth>innerWidth,
    brokenImages:Array.from(document.images).filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.getAttribute('src')),
    outside:Array.from(document.querySelectorAll('h1,h2,h3,p,img,button')).filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+2||r.left< -2)}).slice(0,10).map(e=>({tag:e.tagName,text:e.textContent.slice(0,50)}))
   }));
   results.push({route,width,...data});
   console.log(width+' '+route+' checked');
   if(['/', '/symptoms/', '/symptoms/insomnia/', '/symptoms/cough/'].includes(route))
    await page.screenshot({path:path.join(out,(route==='/'?'home':route.split('/').filter(Boolean).join('-'))+'-'+width+'.png'),fullPage:true});
  }
  await page.close();
 }
 await browser.close();
 fs.writeFileSync(path.join(out,process.argv.includes('--about-only')?'about-layout-recheck.json':process.argv.includes('--images-only')?'image-render-recheck.json':'layout-checks.json'),JSON.stringify(results,null,2));
 console.log(JSON.stringify({checks:results.length,issues:results.filter(r=>r.overflow||r.brokenImages.length||r.outside.length)},null,2));
})().catch(e=>{console.error(e);process.exit(1)});
