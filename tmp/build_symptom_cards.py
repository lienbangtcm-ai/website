from pathlib import Path
from lxml import html, etree
import hashlib

# Keep the historical entry point, but never restore the retired illustration sets.
if __name__ == '__main__':
    from clinic_symptom_series import build
    build()
    raise SystemExit(0)

ROOT = Path(__file__).resolve().parents[1]
page = ROOT / 'output/site-preview/symptoms/index.html'
articles = list(page.parent.glob('*/index.html'))
before = {p: hashlib.sha256(p.read_bytes()).hexdigest() for p in articles}
backup = ROOT / 'output/identity-backup/symptoms-before-cards.html'
if not backup.exists():
    backup.write_bytes(page.read_bytes())
doc = html.fromstring(page.read_text(encoding='utf-8'))

def path(d, accent=False, fill='none'):
    return f'<path d="{d}" stroke="{"#c68e61" if accent else "#66564a"}" fill="{fill}"/>'

def circle(x,y,r,fill='none'):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>'

def mark(x,y):
    return f'<circle cx="{x}" cy="{y}" r="17" fill="#dfb18a" stroke="none" opacity=".3"/>'+path(f'M{x-23} {y-12}l-8 -5 M{x+23} {y-12}l8 -5 M{x} {y-25}v-8',True)

head = path('M83 86V65C83 30 135 27 142 57L145 74L155 89L144 94V109Q135 122 119 115V134M84 86V125L59 138Q45 145 44 166M119 134L144 144Q158 151 158 166',fill='#f8eee0')+path('M83 70Q66 33 100 26Q131 16 144 50M131 75h3')
torso = '<path d="M89 31V55Q88 64 68 69Q45 75 45 99V165H78V174H142V165H175V99Q175 75 152 69Q133 64 131 55V31Z" fill="#f8eee0" stroke="none"/>'+path('M89 31V55Q88 64 68 69Q45 75 45 99V165M131 31V55Q133 64 152 69Q175 75 175 99V165M72 103L78 143V174M148 103L142 143V174')
gut = path('M84 98Q75 91 79 81Q84 72 94 80Q101 68 110 79Q120 69 130 81Q142 75 143 90V139Q135 150 125 139H96Q83 149 79 136V111Q85 102 94 110H125V124H98',True)
art = {}
art['gerd'] = path('M103 30V77Q89 64 77 79Q64 97 81 126Q93 146 118 141Q151 134 146 102Q144 83 132 80Q118 81 118 61V30',fill='#f3dfc8')+path('M109 101V55M101 64l8 -9 8 9',True)+path('M87 112Q94 129 116 126',True)
art['cough'] = head+mark(137,104)+path('M158 91l17 -6M160 101h21M155 111l17 7',True)
art['allergic-rhinitis'] = head+path('M143 80l-9 10 13 6',True)+path('M150 106l17 10 -10 24 -29 -12 8 -21Z',False,'#fffaf2')+path('M158 61l8 -8M166 76h10',True)
art['insomnia'] = path('M36 130H180V163H36ZM39 127V96M179 128V111',fill='#eee3d2')+path('M52 128V107Q54 95 73 99L93 112L136 105Q163 108 169 128',fill='#f8eee0')+path('M119 35Q104 62 133 65Q111 80 99 61Q90 43 119 35Z',True,'#e4c59d')+path('M158 45v12M152 51h12',True)
art['diarrhea'] = torso+gut+path('M103 149v21m-7 -7 7 7 7 -7M123 149v21m-7 -7 7 7 7 -7',True)
art['constipation'] = torso+gut+path('M98 151h29M98 161h29',True)+circle(109,121,3,'#c68e61')
art['menstrual-pain'] = torso+path('M78 111Q91 105 102 112Q110 120 119 112Q131 105 143 111Q143 127 126 130L115 153H105L95 130Q79 128 78 111Z',True,'#ecd3bd')+mark(110,134)
art['fatigue'] = path('M90 84Q67 63 82 42Q99 22 119 39Q138 56 119 81Q107 93 90 84Z',fill='#f8eee0')+path('M81 53l43 7M92 68l7 2M110 71l6 1M86 95Q58 109 57 156M117 94Q143 107 153 156M79 112l20 41M131 114l-15 40M48 158h120')+path('M163 45v28m-6 -7 6 7 6 -7',True)
art['frozen-shoulder'] = torso+path('M65 81Q80 80 84 96L93 128L125 116M51 91L58 143Q62 156 75 153L131 130',False,'#f8eee0')+mark(66,83)+path('M29 70Q18 92 28 113m-7 -5 7 5 4 -9',True)
art['neck-shoulder-pain'] = torso+path('M92 22Q108 35 128 22M110 55V108M72 83Q88 89 110 80Q132 89 148 83')+mark(110,68)
art['low-back-pain'] = torso+path('M110 65V160M76 144Q110 127 144 144')+mark(110,140)+path('M101 127h18M101 138h18M101 149h18',True)
art['sciatica'] = path('M75 32L68 88Q62 113 77 127L80 173M141 32L149 91Q151 112 136 129L132 174M77 127Q110 105 136 129M108 118V171',fill='#f8eee0')+path('M113 75Q142 97 123 126L125 168',True)+mark(130,103)
art['knee-pain'] = path('M89 26L80 79Q77 91 91 97L105 92Q122 100 133 90L142 28M87 110Q78 113 79 128L72 173M133 108Q145 117 135 136L127 173',fill='#f8eee0')+path('M90 82Q108 71 126 82M92 121Q109 133 128 121')+circle(110,103,13,'#ecd3bd')+mark(110,103)
art['tennis-elbow'] = path('M91 28L77 103Q73 127 96 132L167 119L164 98L109 101L123 35',False,'#f8eee0')+path('M103 45L93 107L150 111')+mark(93,108)
art['de-quervain'] = path('M79 175L82 129L67 100Q63 89 72 87Q79 87 89 103L87 59Q86 48 94 48Q101 48 102 60L104 83V44Q105 33 112 39L117 81V50Q120 39 126 47L130 85V63Q136 52 140 64L145 112Q143 125 132 137L135 175',False,'#f8eee0')+path('M87 130Q109 138 133 130M103 106Q105 92 92 91')+mark(89,129)
art['plantar-heel-pain'] = path('M94 28L90 92Q89 110 66 131L49 145Q41 157 57 160H151Q166 158 160 145Q156 138 141 138L125 122L131 29',False,'#f8eee0')+path('M65 147Q91 143 103 124M108 52L105 99')+mark(143,148)

from symptom_art_v2 import ART as art

for image in doc.xpath('//header[@class="lbsym-hero"]/img | //img[@class="lbsym-photo"]'):
    image.getparent().remove(image)
for section in doc.xpath('//section[@class="lbsym-block"]'):
    for a in section.xpath('.//ul[@class="lbsym-list"]//a'):
        slug = a.get('href').strip('/').split('/')[-1]
        existing_caption = a.find('span[@class="symptom-caption"]')
        label = (existing_caption.text if existing_caption is not None else a.text_content()).strip()
        for child in list(a):
            a.remove(child)
        a.text = None
        colored = art[slug].replace('#f8eee0', '#efd0b4').replace('#f3dfc8', '#dfad92').replace('#ecd3bd', '#d9947e').replace('#eee3d2', '#aebbb0').replace('#e4c59d', '#e3be74')
        svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 200" aria-hidden="true" focusable="false">{colored}</svg>'
        a.append(html.fromstring(svg))
        caption = etree.SubElement(a,'span',{'class':'symptom-caption'})
        caption.text = label
        arrow = etree.SubElement(caption,'span',{'aria-hidden':'true'})
        arrow.text = '↗'
for link in doc.xpath('//link[contains(@href,"symptom-cards") or contains(@href,"site-editorial")]'):
    link.getparent().remove(link)
body = doc.find('body')
etree.SubElement(body,'link',rel='stylesheet',href='/assets/site-editorial.css?v=1')
etree.SubElement(body,'link',rel='stylesheet',href='/assets/symptom-cards.css?v=1')
doc.find('head/title').text = '常見症狀｜連邦中醫診所'
page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
assert all(hashlib.sha256(p.read_bytes()).hexdigest()==h for p,h in before.items())
print(f'Built {len(art)} symptom cards; {len(before)} article files unchanged.')
