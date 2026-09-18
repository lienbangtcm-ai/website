const {chromium}=require('C:/Users/yutin/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
(async()=>{
 const b=await chromium.launch({channel:'msedge',headless:true});
 for(const width of [1440,768,390]){
  const p=await b.newPage({viewport:{width,height:1000}});
  await p.route('https://**/*',r=>r.abort());
  await p.goto('http://127.0.0.1:8765/symptoms/');
  const result=await p.evaluate(()=>{
   const cards=[...document.querySelectorAll('.symptom-master-card')];
   return {width:innerWidth,overflow:document.documentElement.scrollWidth>innerWidth,
    cards:cards.length,characters:[...new Set(cards.map(a=>a.querySelector('svg').dataset.character))],
    valid:cards.every(a=>a.querySelectorAll('svg').length===1&&a.querySelectorAll('.symptom-caption').length===1&&a.querySelector('svg').getBoundingClientRect().bottom<a.querySelector('.symptom-caption').getBoundingClientRect().top),
    magnifiers:document.querySelectorAll('.symptom-master-card svg circle').length};
  });
  console.log(result);
  if(result.overflow||!result.valid||result.cards!==16||result.characters.length!==4||result.magnifiers!==0)throw Error('Phase 2 check failed');
  await p.locator('.lbsym-content').screenshot({path:`output/release-audit/phase2-${width}.png`});
  await p.close();
 }
 await b.close();
})().catch(e=>{console.error(e);process.exit(1)});
