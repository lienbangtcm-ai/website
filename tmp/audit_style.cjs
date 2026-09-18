const fs=require('fs'),path=require('path');
const {chromium}=require('C:/Users/yutin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const base=path.resolve('output/site-preview'),out=path.resolve('output/release-audit/style-audit');fs.mkdirSync(out,{recursive:true});
function walk(dir){return fs.readdirSync(dir,{withFileTypes:true}).flatMap(e=>e.isDirectory()?walk(path.join(dir,e.name)):e.name==='index.html'?[path.join(dir,e.name)]:[])}
(async()=>{const b=await chromium.launch({channel:'msedge',headless:true});const report=[];let n=0;
 for(const file of walk(base)){
  const route='/'+path.relative(base,path.dirname(file)).replaceAll('\\','/')+(file===path.join(base,'index.html')?'':'/');
  for(const width of [1440,390]){
   const p=await b.newPage({viewport:{width,height:1000}});
   // Remote assets can be blocked in the sandbox. Keep that limitation explicit.
   await p.route('https://**/*',r=>r.abort());
   await p.goto('http://127.0.0.1:8765'+route,{waitUntil:'domcontentloaded'});
   const data=await p.evaluate(()=>{
    const val=n=>{if(!n)return null;const s=getComputedStyle(n);return {text:n.textContent.trim().slice(0,65),font:s.fontFamily,size:s.fontSize,color:s.color,background:s.backgroundColor,radius:s.borderRadius}};
    return {title:document.title,h1:val(document.querySelector('h1')),header:val(document.querySelector('.preview-header')),cta:val(document.querySelector('.preview-line')),h2:val(document.querySelector('h2')),overflow:document.documentElement.scrollWidth>innerWidth,styles:[...document.querySelectorAll('link[rel=stylesheet]')].map(n=>n.getAttribute('href')),images:[...document.images].map(i=>({src:i.getAttribute('src'),alt:i.alt})),svg:document.querySelectorAll('svg').length};
   });
   report.push({route,width,...data});
   await p.screenshot({path:path.join(out,`${n}-${width}.png`),fullPage:width===1440});
   await p.close();
  } console.log(n,route);n++;
 }
 fs.writeFileSync(path.join(out,'report.json'),JSON.stringify(report,null,2));
 const p=await b.newPage({viewport:{width:1600,height:1100}});
 const ids=report.filter(x=>x.width===1440).map((r,i)=>({r,i}));
 for(let start=0;start<ids.length;start+=9){
  const group=ids.slice(start,start+9);
  await p.setContent('<style>*{box-sizing:border-box}body{margin:0;background:#ddd;font:16px sans-serif}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}article{height:720px;overflow:hidden;background:white}h3{height:35px;margin:0;padding:6px;font-size:14px}img{width:100%;display:block}</style><div class=grid>'+group.map(({r,i})=>`<article><h3>${i}: ${r.route}</h3><img src="data:image/png;base64,${fs.readFileSync(path.join(out,i+'-1440.png')).toString('base64')}"></article>`).join('')+'</div>');
  await p.screenshot({path:path.join(out,'sheet-'+start+'.png'),fullPage:true});
 }
 await b.close();console.log('DONE',report.length);
})().catch(e=>{console.error(e);process.exit(1)});
