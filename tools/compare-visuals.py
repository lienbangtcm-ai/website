from pathlib import Path
from PIL import Image, ImageChops, ImageDraw
import sys,json
round_name=sys.argv[1]
out=Path(__file__).resolve().parents[1]/'output/visual-qa'/round_name
downloads=Path('C:/Users/yutin/Downloads')
temp=Path('C:/Users/yutin/AppData/Local/Temp')
refs={'home':temp/'codex-clipboard-9f491d43-786c-4f2c-9e75-e6f05ce95682.png','services':downloads/'ChatGPT 圖像 2026年10月9日 下午01_33_14-1.png','symptoms':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_13-2.png','team':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_15-3.png','about-lienbang':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_11-1.png','acupuncture':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_16-4.png','pulse-diagnosis':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_19-5.png','acupuncture-physical-therapy':downloads/'ChatGPT 圖像 2026年10月9日 下午01_42_22-6.png'}
metrics=[]
for route,ref in refs.items():
 for width in [1440,768,390]:
  reference=ref
  if route=='home' and width==390:reference=temp/'codex-clipboard-9899697d-156f-44df-b0ea-4fc1ed05a20a.png'
  actual=Image.open(out/f'{route}-{width}.png').convert('RGB')
  source=Image.open(reference).convert('RGB')
  target=source.resize((width,round_int:=int(source.height*width/source.width)),Image.Resampling.LANCZOS)
  height=max(actual.height,target.height)
  a=Image.new('RGB',(width,height),'#eee');a.paste(actual)
  b=Image.new('RGB',(width,height),'#eee');b.paste(target)
  side=Image.new('RGB',(width*2,height),'white');side.paste(b);side.paste(a,(width,0));side.save(out/f'{route}-{width}-compare.jpg',quality=85)
  Image.blend(b,a,.5).save(out/f'{route}-{width}-overlay.jpg',quality=85)
  ImageChops.difference(b,a).save(out/f'{route}-{width}-diff.jpg',quality=85)
  metrics.append({'route':route,'width':width,'actualHeight':actual.height,'scaledReferenceHeight':target.height,'heightRatio':round(actual.height/target.height,3),'comparison':'reference scaled proportionally; phone/tablet adaptation lacks separate reference' if width!=1440 and route!='home' else 'proportional reference at same width; differing assets/content affect pixel differences'})
(out/'comparison.json').write_text(json.dumps(metrics,indent=2),encoding='utf-8')
