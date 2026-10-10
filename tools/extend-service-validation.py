from pathlib import Path
for name in ['tools/six-services-validation.cjs','tools/six-services-audit.cjs']:
 p=Path(name);t=p.read_text(encoding='utf-8-sig').replace("'針刀','美顏針','埋線'","'針刀','美顏針','埋線','浮針'").replace('18 page/viewport','21 page/viewport');p.write_text(t,encoding='utf-8')
