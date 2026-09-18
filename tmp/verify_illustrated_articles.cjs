const {chromium}=require('C:/Users/yutin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs=require('fs'),path=require('path');
const root=path.resolve(__dirname,'../output/site-preview/symptoms');
const output=path.resolve(__dirname,'../output/release-audit');
(async()=>{
const browser=await chromium.launch({headless:true,channel:'msedge'});
const checks=[];
for(const width of [390,1440]){
 const page=await browser.newPage({viewport:{width,height:900}});
 for(const slug of fs.readdirSync(root).filter(x=>fs.statSync(path.join(root,x)).isDirectory())){
  if(process.argv[2] && slug!==process.argv[2])continue;
  await page.goto('http://127.0.0.1:8765/symptoms/'+slug+'/',{waitUntil:'networkidle'});
  await page.evaluate(async()=>{await Promise.all(Array.from(document.images).map(i=>{i.loading='eager';return Promise.race([i.decode().catch(()=>{}),new Promise(r=>setTimeout(r,12000))])}))});
  const result=await page.evaluate(()=>({count:document.querySelectorAll('.lb-article img').length,broken:Array.from(document.images).filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src),overflow:document.documentElement.scrollWidth>innerWidth,figures:Array.from(document.querySelectorAll('.lb-article figure')).map(f=>({caption:f.querySelector('figcaption')?.textContent,inside:f.getBoundingClientRect().right<=innerWidth+1}))}));
  checks.push({slug,width,...result});
  if(['cough','knee-pain'].includes(slug))await page.screenshot({path:path.join(output,slug+'-illustrated-'+width+'.png'),fullPage:true});
  console.log(width+' '+slug+' '+result.count+' images');
 }
 await page.close();
}
await browser.close();
const errors=checks.filter(c=>c.count!==3||c.broken.length||c.overflow||c.figures.some(f=>!f.caption||!f.inside));
fs.writeFileSync(path.join(output,process.argv[2]?'illustrated-'+process.argv[2]+'-browser-check.json':'illustrated-articles-browser-check.json'),JSON.stringify({checks,errors},null,2));
console.log(JSON.stringify({combinations:checks.length,errors},null,2));process.exitCode=errors.length?1:0;
})().catch(e=>{console.error(e);process.exit(1)});
