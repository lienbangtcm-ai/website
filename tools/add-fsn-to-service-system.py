from pathlib import Path
p=Path('tools/unify-six-services.py');t=p.read_text(encoding='utf-8-sig');t=t.replace("'美顏針','埋線'];photos=","'美顏針','埋線','浮針'];photos=").replace("'/assets/service-embedding-real-v3.png']","'/assets/service-embedding-real-v3.png','/services/images/fsn.webp']");p.write_text(t,encoding='utf-8')
