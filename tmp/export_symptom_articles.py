from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PREVIEW = ROOT / "output" / "site-preview" / "symptoms"

TARGETS = {
    "neck-shoulder-pain": ROOT / "output" / "neck-shoulder-pain" / "neck-shoulder-pain-final.html",
    "low-back-pain": ROOT / "output" / "low-back-pain" / "low-back-pain-final.html",
    "cough": ROOT / "output" / "cough" / "cough-final.html",
    "allergic-rhinitis": ROOT / "output" / "allergic-rhinitis" / "allergic-rhinitis-final.html",
    "constipation": ROOT / "output" / "constipation" / "constipation-final.html",
    "menstrual-pain": ROOT / "output" / "menstrual-pain" / "menstrual-pain-final.html",
    "diarrhea": ROOT / "output" / "diarrhea" / "diarrhea-final.html",
    "fatigue": ROOT / "output" / "fatigue" / "fatigue-final.html",
    "frozen-shoulder": ROOT / "output" / "frozen-shoulder" / "frozen-shoulder-final.html",
    "sciatica": ROOT / "output" / "sciatica" / "sciatica-final.html",
    "knee-pain": ROOT / "output" / "knee-pain" / "knee-pain-final.html",
    "tennis-elbow": ROOT / "output" / "tennis-elbow" / "tennis-elbow-final.html",
    "de-quervain": ROOT / "output" / "de-quervain" / "de-quervain-final.html",
    "plantar-heel-pain": ROOT / "output" / "plantar-heel-pain" / "plantar-heel-pain-final.html",
}

for slug, target in TARGETS.items():
    source = (PREVIEW / slug / "index.html").read_text(encoding="utf-8")
    source = re.sub(r'<meta name="robots" content="noindex,nofollow">', "", source, count=1)
    source = re.sub(r'<style>html,body\{margin:0;overflow-x:hidden\}\.preview-header.*?</style>', "", source, count=1, flags=re.S)
    source = re.sub(r'<header class="preview-header">.*?</header>', "", source, count=1, flags=re.S)
    source = re.sub(r'<aside class="preview-related".*?</aside>', "", source, count=1, flags=re.S)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(source, encoding="utf-8")
    print(target)
