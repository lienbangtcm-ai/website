"""Crop supplied service illustrations only; keep semantic website copy and links."""
from pathlib import Path
from shutil import copy2
from PIL import Image
from lxml import html
ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'output/site-preview/assets/service-reference'
SOURCES=[
 ('ChatGPT Image 2026年9月13日 下午02_57_49 (1).png',(2048,683),[
 ('pulse','把脈評估',(146,327,357,530)),('herbs','單味藥組方',(752,327,964,530)),('care','生活照護',(1361,327,1578,530))]),
 ('ChatGPT Image 2026年9月13日 下午02_57_49 (2).png',(2048,683),[
 ('movement','疼痛與活動評估',(110,332,355,534)),('acupuncture','針灸治療',(744,332,989,534)),('integration','中醫 × 物理治療',(1373,332,1624,534))]),
 ('ChatGPT Image 2026年9月13日 下午02_57_59.png',(1983,793),[
 ('acupotomy','針刀',(155,265,431,449)),('fsn','浮針',(1025,265,1298,449)),('facial','美顏針',(156,503,439,692)),('embedding','穴位埋線',(1025,506,1317,692))]),
 ('ChatGPT Image 2026年9月13日 下午02_59_11.png',(1402,1122),[
 ('booking','預約掛號',(75,254,247,454)),('arrival','到院報到',(528,254,722,454)),('consult','醫師看診',(960,254,1140,454)),
 ('symptom','主要不適',(76,735,263,869)),('medicine','目前用藥',(730,735,918,869)),('reports','相關檢查',(76,908,263,1043)),('history','病史資料',(730,908,918,1043))])]

def apply():
 DEST.mkdir(parents=True,exist_ok=True)
 originals=ROOT/'output/illustration-master/services';originals.mkdir(exist_ok=True)
 mapping={}
 for filename,(w,h),items in SOURCES:
  source=Path('C:/Users/yutin/Downloads')/filename
  copy2(source,originals/filename)
  im=Image.open(source)
  for key,label,box in items:
   bounds=tuple(round(v*s) for v,s in zip(box,(im.width/w,im.height/h,im.width/w,im.height/h)))
   crop=im.crop(bounds);crop.save(DEST/f'{key}.png',optimize=True)
   mapping[label]=(key,crop.size)
 for relative in ['output/site-preview/services/index.html','output/services-editorial/services-preview.html','output/services-page.html']:
  page=ROOT/relative
  if not page.exists():continue
  backup=ROOT/'output/identity-backup'/('service-ref-'+page.parent.name+'-'+page.name)
  if not backup.exists():backup.write_bytes(page.read_bytes())
  doc=html.fromstring(page.read_text(encoding='utf-8'))
  entries=doc.xpath('//*[contains(concat(" ",normalize-space(@class)," ")," ls-entry ")]')
  before=[(e.text_content(),e.get('href')) for e in entries]
  count=0
  for entry in entries:
   label=entry.find('.//h3').text_content()
   if label not in mapping:continue
   key,(iw,ih)=mapping[label]
   for node in list(entry):
    if node.tag in ('svg','img'):entry.remove(node)
   entry.insert(0,html.Element('img',{'class':'ls-illustration','src':f'/assets/service-reference/{key}.png','alt':'','width':str(iw),'height':str(ih),'loading':'lazy','decoding':'async','style':'object-fit:contain;border-radius:14px'}))
   count+=1
  assert before==[(e.text_content(),e.get('href')) for e in entries]
  assert count==17,(relative,count)
  page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
 print('17 supplied illustrations applied; existing text and links unchanged. Local files only.')

if __name__=='__main__':apply()
