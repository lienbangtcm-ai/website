from PIL import Image,ImageDraw
from pathlib import Path
q=Path('output/visual-qa/six-services-audit')
for w in [1440,390]:
 canvas=Image.new('RGB',(1500,1600),'#eae5df');d=ImageDraw.Draw(canvas)
 for i in range(6):
  im=Image.open(q/f'{i}-{w}.png');im=im.crop((0,0,im.width,min(im.height,3000)));im.thumbnail((480,750));x=i%3*500;y=i//3*800;canvas.paste(im,(x,y+25));d.text((x+5,y+4),['Internal medicine','Acupuncture','Integration','Acupotomy','Facial','Embedding'][i],fill='black')
 canvas.save(q/f'contact-{w}.jpg')
