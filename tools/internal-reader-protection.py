from pathlib import Path
import re,subprocess,json
root=Path('output/site-preview');slugs=['gerd','cough','insomnia','allergic-rhinitis','diarrhea','constipation','menstrual-pain','fatigue'];report=[]
for slug in slugs:
 p=root/'symptoms'/slug/'index.html';new=p.read_text(encoding='utf-8');old=subprocess.check_output(['git','show','HEAD:'+p.as_posix()]).decode('utf-8')
 medical=lambda s:[re.sub(r'\s+',' ',re.sub('<[^>]*>','',m)).strip() for m in re.findall(r'<(?:p|li)\b[^>]*>.*?</(?:p|li)>',s,re.S)]
 missing=[x for x in medical(old) if x not in medical(new)]
 seo=lambda s:re.findall(r'<meta\b[^>]*>|<title>.*?</title>|<script\b[^>]*>.*?</script>',s,re.S)
 report.append({'slug':slug,'medicalParagraphsPreserved':not missing,'missing':missing,'seoAndScriptsUnchanged':seo(old)==seo(new)})
Path('output/visual-qa/internal-content-review/protection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(report,ensure_ascii=False))
