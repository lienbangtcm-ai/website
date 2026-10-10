from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
q=Path('output/visual-qa/home-system/final');paths=sorted(q.glob('*-1440.png'))
for w in [1440,390]:
 for offset in range(0,len(paths),8):
  canvas=Image.new('RGB',(1280,1400),'#eee9e2');d=ImageDraw.Draw(canvas)
  for j,p in enumerate(paths[offset:offset+8]):
   f=p.with_name(p.name.replace('-1440.png',f'-{w}.png'));im=Image.open(f);im=im.crop((0,0,im.width,min(im.height,2200 if w==1440 else 2400)));im.thumbnail((310,650));x=(j%4)*320;y=(j//4)*700;canvas.paste(im,(x,y+30));d.text((x+4,y+5),p.stem[:38],fill='black')
  canvas.save(q.parent/f'latest-contact-{w}-{offset//8}.jpg')
