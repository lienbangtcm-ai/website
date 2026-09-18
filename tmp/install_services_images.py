from pathlib import Path
from PIL import Image
import json,re,shutil
R=Path(__file__).resolve().parents[1];D=R/'output/services-editorial'
target=R/'output/site-preview/services/images';target.mkdir(exist_ok=True)
for f in D.glob('*-result.json'):
 r=json.loads(f.read_text(encoding='utf-8'));src=Path(re.search(r'as (C:.*?\.png) by default',r['output_hint']).group(1))
 im=Image.open(src).convert('RGB');im.thumbnail((1600,1200))
 for ext,fmt in [('jpg','JPEG'),('webp','WEBP')]:
  out=D/'images'/(r['key']+'.'+ext)
  for quality in [88,82,76,70,64]:
   im.save(out,fmt,quality=quality,optimize=True)
   if out.stat().st_size<200000:break
  shutil.copy2(out,target/out.name)
 print(r['key'],im.size)
