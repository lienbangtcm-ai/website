"""Symptom series built exclusively from the user-approved character master."""
from pathlib import Path
import hashlib
from lxml import html
from clinic_character_master import PALETTE, face, torso, gerd

def path(d, fill='none', stroke='none', width=1.5):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>'

def line(d, color='var(--brown)', width=1.4):
    return path(d,stroke=color,width=width)

def ellipse(x,y,rx,ry,color,opacity=1):
    return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{color}" opacity="{opacity}"/>'

def skin(d): return path(d,'var(--skin)')
def shade(d): return path(d,'var(--skin_shadow)')
def cue(x,y,r=16):
    return ellipse(x,y,r,r,'var(--terracotta)',.19)+ellipse(x,y,r*.55,r*.55,'var(--terracotta)',.18)

MASTER=gerd()
FAR=MASTER.split('<!-- Relaxed far arm, separate sleeve opening. -->')[1].split('<!-- Soft anatomical')[0]
LOW_HAND=MASTER.split('<!-- Hand rests below the stomach; fingers do not obscure the anatomy. -->')[1].split('<!-- Reflux originates')[0]
NEAR=skin('M121 222L143 230L138 268L150 295Q153 301 149 304Q145 305 141 299L137 294L140 305Q140 311 135 308L125 293Q119 286 119 276Z')+shade('M122 241L123 274Q122 285 134 299L140 305Q140 311 135 308L125 293Q119 286 119 276Z')

def wrap(content):
    style=';'.join(f'--{k}:{v}' for k,v in PALETTE.items())
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 360" style="{style}" aria-hidden="true" focusable="false">'+ellipse(202,193,121,129,'var(--cream)')+ellipse(199,331,92,4,'#ded6c7',.45)+content+'</svg>'

def character(arms, overlay='', head=None):
    return torso()+(face() if head is None else head)+overlay+arms

def badge(content):
    # Same scale and palette as the character; small detail for otherwise hidden limbs.
    return '<g transform="translate(269 246)">'+ellipse(0,0,48,48,'#f8f3e9')+f'<circle r="47" fill="none" stroke="#dbcab8" stroke-width="1.3"/>'+content+'</g>'

def upper_hand():
    return skin('M121 221L143 230L148 253L173 219L180 190L184 177Q188 171 191 175L189 190L199 179Q204 175 205 180L198 193L207 185Q212 184 211 189L201 202L191 216L186 231L160 272Q151 284 140 277Q132 273 129 260Z')+shade('M123 231L133 260Q138 279 150 276L162 263L185 230L186 231L160 272Q151 284 140 277Q132 273 129 260Z')+line('M188 194L185 207M198 193L191 205','#b58e78',1.2)

ART={'gerd':MASTER}
# Cough: same face in a slight turn, hand covers mouth; restrained movement lines.
cough_hand=skin('M260 226L276 220L278 248Q279 262 267 263Q256 265 250 249L220 163L207 133L194 123Q190 119 192 115Q193 112 197 114L204 118L199 110Q198 105 202 105L210 113L208 104Q210 100 213 104L222 118L226 133L238 155L265 231Z')+shade('M271 225L276 223L278 248Q279 262 267 263Q256 265 250 249L228 180L258 245Q264 258 270 250Z')+line('M201 116L210 122M208 113L215 122M214 109L219 118','#b58e78',1.2)
ART['cough']=wrap(character(NEAR+cough_hand,head='<g transform="rotate(6 200 143)">'+face()+'</g>')+line('M239 104l12 -4M242 116h15M240 128l11 5','var(--terracotta)',2))
# Rhinitis: visible paper folds and fingers holding it against the nose.
tissue=path('M196 96L221 91L240 120L217 136L193 119Z','#fffaf1', '#d9cbbb',1)+line('M204 99L212 122L230 122M212 122L214 133','#ded3c4',1)
nose_hand=skin('M259 226L276 220L277 246Q279 259 267 261Q256 261 251 249L226 153L216 133L208 125Q202 123 204 119Q205 116 210 119L217 123L211 109Q210 104 214 104Q218 106 222 119L231 132L242 149L265 229Z')+shade('M272 225L276 223L277 246Q279 259 267 261Q256 261 251 249L242 217L260 248Q268 257 271 246Z')+line('M216 121L222 128','#b58e78',1.2)
ART['allergic-rhinitis']=wrap(character(NEAR+tissue+nose_hand)+line('M241 88l8 -6M246 100h11','var(--terracotta)',1.8))
# Sleep scene preserves the exact master head size, now resting on a pillow.
bed=path('M59 243H344V267H59Z','var(--blue)')+path('M66 267V305H74V267M330 267V305H338V267','var(--brown)')+path('M65 237Q71 221 87 221H136Q150 222 151 244H65Z','#fffaf1','#dfd3c1',1.2)
sleep_face=face().replace('M186 94Q191 96 196 93M211 93Q216 96 220 94','M186 94Q191 90 196 94M211 94Q216 90 220 94')
sleep_face=sleep_face.replace('<path d="M181 111L180 149Q196 165 214 148L207 112Z" fill="var(--skin)"/>','').replace('<path d="M181 113L207 114L210 133Q195 143 181 135Z" fill="var(--skin_shadow)"/>','')
sleep_face=sleep_face+ellipse(191,93,1.3,1.7,'var(--brown)')+ellipse(216,93,1.3,1.7,'var(--brown)')
sleep_head='<g transform="translate(-69 127) rotate(-65 200 90)">'+sleep_face+'</g>'
blanket=path('M145 214Q171 195 193 202Q246 188 278 208Q318 212 338 245H145Z','var(--sage)')+path('M145 234Q247 216 338 245H145Z','var(--sage_shadow)',width=0)+line('M166 217Q196 208 223 216M232 205Q274 201 302 222','var(--sage_shadow)',1.5)
sleep_arm=skin('M167 224L144 236L125 233L115 229Q111 226 114 223L124 224L135 227L153 216Z')+line('M116 226L124 229','#b58e78',1.1)
moon=path('M282 84Q265 105 290 115Q270 127 258 110Q246 92 266 81Q274 78 282 84Z','var(--mustard)')
ART['insomnia']=wrap(bed+sleep_head+blanket+sleep_arm+moon)
# Abdominal symptoms use the approved translucent anatomy treatment, not new icons.
bowel=path('M184 215Q173 216 175 230V254Q175 261 183 261Q190 261 190 254V231H219V254Q219 261 227 261Q235 261 235 253V227Q235 215 225 215Z','#f3ddc9','#ba937b',1.4)+line('M195 237Q206 230 217 238Q225 246 204 246Q192 246 198 254L211 255','#bc9983',1.5)
ART['diarrhea']=wrap(character(FAR+LOW_HAND, bowel)+line('M201 237V252m-4 -5 4 5 4 -5M213 237V251m-4 -5 4 5 4 -5','var(--terracotta)',2.1))
constipation_overlay=bowel+ellipse(198,231,3,3,'var(--terracotta)',.65)+ellipse(210,231,3,3,'var(--terracotta)',.65)+ellipse(222,231,3,3,'var(--terracotta)',.65)+line('M194 248h24','var(--terracotta)',2.2)
ART['constipation']=wrap(character(FAR+LOW_HAND,constipation_overlay))
uterus=path('M178 223Q190 217 199 225Q205 230 212 225Q224 217 236 223Q235 240 219 241L212 257H201L195 241Q179 240 178 223Z','#ebc4b6','#b58d79',1.3)+line('M184 226Q194 224 199 232L206 248L213 232Q221 224 230 226','var(--terracotta)',1.4)+ellipse(186,235,4,3,'var(--pink)')+ellipse(228,235,4,3,'var(--pink)')
ART['menstrual-pain']=wrap(character(FAR+LOW_HAND,uterus+cue(207,238,19)))
# Fatigue: palm at temple, head inclined. Same head, skin and clothing geometry.
temple_hand=skin('M121 221L143 229L150 244L161 172L169 116L166 96Q167 90 171 93L175 108L177 94Q180 90 182 95L183 114L178 134L176 177L171 252Q169 271 155 273Q141 275 134 259Z')+shade('M124 232L138 256Q145 270 157 266Q167 263 168 249L171 204L171 252Q169 271 155 273Q141 275 134 259Z')+line('M173 110L175 124','#b58e78',1.2)
ART['fatigue']=wrap(character(FAR+temple_hand,head='<g transform="rotate(-10 194 143)">'+face()+'</g>'))
# Shoulder: opposite hand rests directly on the shoulder; a gentle arc suggests limited lift.
shoulder_hand=skin('M121 221L143 229L150 252L218 181L237 169L250 166Q256 166 255 170L244 175L254 173Q260 174 257 178L245 182L253 181Q258 183 253 186L237 190L226 197L164 272Q153 282 142 277Q131 272 128 257Z')+shade('M124 232L134 258Q142 279 154 273L226 197L164 272Q153 282 142 277Q131 272 128 257Z')+line('M240 178L235 182M245 183L238 186','#b58e78',1.2)
ART['frozen-shoulder']=wrap(character(FAR+shoulder_hand)+cue(250,175,18)+line('M295 180Q311 209 300 233m-4 -7 4 7 6 -5','var(--terracotta)',1.8))
# Neck: hand cups side of neck, distinct from the shoulder pose.
neck_hand=skin('M259 226L276 220L282 243Q285 259 272 263Q261 265 254 251L216 178L204 154L199 139Q198 133 202 133Q205 133 209 143L211 129Q214 125 217 130L218 145L224 135Q228 132 230 136L224 153L227 165L269 236Z')+shade('M273 226L276 222L282 243Q285 259 272 263Q261 265 254 251L239 221L261 250Q270 260 275 250Z')+line('M215 144L215 154M221 149L221 157','#b58e78',1.2)
ART['neck-shoulder-pain']=wrap(character(NEAR+neck_hand)+cue(214,145,15))
# Lower back shown with hand at flank and a consistent anatomy detail panel.
hip_hand=skin('M259 225L276 220L284 256Q286 270 273 275L248 282L235 282Q229 280 233 277L245 273L235 274Q230 272 235 269L247 266L257 265L264 258Z')+shade('M276 235L284 256Q286 270 273 275L248 282L235 282Q229 280 233 277L265 269Q276 265 273 254Z')
back_detail=path('M-25 -29Q-17 -16 -24 23Q0 32 24 23Q17 -16 25 -29Z','var(--skin)')+line('M0 -28V23M-16 19Q0 9 16 19','#b48e76',1.4)+cue(0,9,15)+line('M-5 -7H5M-5 1H5M-5 9H5M-5 17H5','var(--terracotta)',1.6)
ART['low-back-pain']=wrap(character(NEAR+hip_hand)+badge(back_detail))
sciatic_detail=path('M-21 -32H20L23 -1L15 36H2L3 4L-2 2L-10 36H-24L-16 0Z','var(--blue)')+path('M-21 -32H20L22 -10Q0 -2 -19 -12Z','var(--sage)')+line('M8 -13Q21 -4 9 10L6 29','var(--terracotta)',2.7)+cue(12,-2,12)
ART['sciatica']=wrap(character(NEAR+hip_hand)+badge(sciatic_detail))
# Limbs keep the master face and overall character size. Detail discs reveal the
# exact affected joint without changing the series into disembodied standalone icons.
knee_detail=path('M-18 -34H8L5 -5Q4 0 14 7L35 28L23 38L-4 16Q-16 11 -16 0Z','var(--skin)')+path('M-20 -34H11L8 -17L-18 -15Z','var(--blue)')+line('M-7 -4Q5 -6 11 5','#b18a72',1.4)+cue(3,6,13)
ART['knee-pain']=wrap(character(NEAR+FAR)+badge(knee_detail))
elbow_pose=skin('M121 221L143 228L146 255L184 257L194 253Q200 252 201 256L198 260L204 260Q209 262 205 266L196 273L153 282Q135 284 128 269Z')+shade('M124 232L134 262Q138 277 153 277L193 269L196 273L153 282Q135 284 128 269Z')
elbow_detail=path('M-24 -32L-2 -28L-9 8L23 7L31 3L37 10L30 17L-8 24Q-25 26 -25 10Z','var(--skin)')+path('M-26 -34L0 -29L-2 -14L-26 -17Z','var(--sage)')+cue(-13,12,13)
ART['tennis-elbow']=wrap(character(FAR+elbow_pose)+badge(elbow_detail))
wrist_hand=skin('M258 226L276 220L276 252Q275 265 261 266L206 271L195 268Q189 264 192 261L204 261L198 256Q196 252 200 251L214 257L251 250L258 239Z')+shade('M273 227L276 222L276 252Q275 265 261 266L206 271L195 268Q189 264 192 261L207 266L260 260Q271 257 271 246Z')
wrist_detail=skin('M-15 36L-14 8L-27 -6Q-30 -13 -25 -14L-12 -4L-13 -24Q-12 -29 -8 -28L-5 -10L-3 -31Q0 -37 3 -30L4 -10L10 -27Q14 -30 15 -25L12 -7L20 -19Q24 -22 25 -17L16 7L8 17L8 36Z')+path('M-16 26H10V38H-16Z','var(--sage)')+line('M-12 12Q-2 18 9 14','#b58e78',1.2)+cue(-10,15,12)
ART['de-quervain']=wrap(character(elbow_pose+wrist_hand)+badge(wrist_detail))
foot_detail=skin('M-5 -34H17L14 0Q15 10 29 21Q39 29 29 33L11 33L-4 27L-25 33L-38 32Q-43 29 -37 24L-13 9Q-4 3 -5 -9Z')+path('M-7 -34H19L17 -17H-6Z','var(--blue)')+line('M4 -7Q6 7 -5 13M21 15Q10 20 15 28','#b58e78',1.2)+cue(23,26,12)
ART['plantar-heel-pain']=wrap(character(NEAR+FAR)+badge(foot_detail))

# Female member of the same character family: shared face and skin rendering,
# with an original tied-back hairstyle. Pelvic discomfort is below the navel.
def female_face():
    node=html.fromstring('<div>'+face()+'</div>')
    for element in list(node):
        if element.get('fill') in ('var(--hair)','var(--hair_light)'):
            node.remove(element)
    rear=path('M167 89Q151 67 165 48Q180 30 207 41Q231 44 235 69L229 102L220 91L171 102Z','var(--hair)')+ellipse(157,99,15,22,'var(--hair)')
    fringe=path('M165 86Q157 61 175 49Q196 35 219 52Q233 63 228 87L220 82L217 66Q199 70 185 56Q182 77 172 87L171 96L167 95Z','var(--hair)')+path('M169 65Q181 43 202 48Q188 48 181 62L172 79Z','var(--hair_light)')
    return rear+''.join(html.tostring(e,encoding='unicode') for e in node)+fringe

chair=path('M129 256H272V273H129Z','var(--mustard)')+path('M142 272L135 326H142L152 272M252 272L260 326H267L262 272','var(--brown)')
lap=path('M155 245Q196 234 235 249Q251 264 246 278L222 323H201L217 277L198 268L181 322H159L170 276Q149 268 155 245Z','var(--blue)')+path('M198 268L210 273L190 296L181 322H172L186 278Z','#7c909b')
female_top=path('M174 145Q150 148 140 165L124 211L146 221L154 200L153 250Q196 266 239 253L234 201L244 222L266 211L255 169Q248 151 217 145Q195 163 174 145Z','var(--pink)')+path('M234 170Q243 207 239 253L222 257Q225 222 218 201Z','#b58c85')+path('M173 145Q195 162 217 145L220 153Q194 171 170 153Z','var(--cream)')+line('M152 179L154 199M234 180V198M166 240Q183 246 193 244','#a97f78',1.3)
# Hands cradle the low abdomen, under the navel; no organ drawn over the chest.
left_low=skin('M126 209L146 216L150 237L175 243L189 239Q195 238 197 242L189 246L198 246Q203 248 199 251L187 254L172 253L144 250Q133 248 131 237Z')+shade('M128 217L137 238Q138 247 151 247L174 250L187 251L199 249L199 251L187 254L172 253L144 250Q133 248 131 237Z')
right_low=skin('M244 217L263 211L261 238Q260 249 248 253L215 260L202 259Q196 257 199 254L211 252L201 251Q196 248 201 246L216 247L242 239Z')+shade('M258 217L263 213L261 238Q260 249 248 253L215 260L202 259Q196 257 199 254L215 255L245 248Q254 244 254 235Z')+line('M184 247L191 247M210 253L217 252','#b58e78',1.2)
female_seated=female_top+female_face()+cue(203,237,21)+left_low+right_low
ART['menstrual-pain']=wrap(chair+lap+'<g transform="rotate(6 196 246)">'+female_seated+'</g>')
# Vary body language as well as hands: fatigue leans into a supporting desk;
# abdominal cramping hunches forward. The underlying character is unchanged.
desk=path('M104 278H288V289H104Z','var(--mustard)')+path('M115 289V327H122V289M272 289V327H279V289','var(--brown)')
ART['fatigue']=wrap('<g transform="translate(0 8) rotate(-9 178 250)">'+character(FAR+temple_hand,head='<g transform="rotate(-10 194 143)">'+face()+'</g>')+'</g>'+desk)
ART['diarrhea']=wrap('<g transform="rotate(9 195 264)">'+character(FAR+LOW_HAND,bowel)+line('M201 237V251m-4 -5 4 5 4 -5M213 237V251m-4 -5 4 5 4 -5','var(--terracotta)',2.1)+'</g>')

def build():
    # The user selected exact reference crops; do not restore superseded SVGs.
    if (Path(__file__).resolve().parents[1]/'output/site-preview/assets/illustrations/reference-crops/frozen-shoulder.png').exists():
        from apply_reference_crops import apply
        apply()
        return
    from clinic_phase2 import refine
    artwork=refine(ART)
    from clinic_musculoskeletal import illustrations
    artwork.update(illustrations())
    root=Path(__file__).resolve().parents[1]
    page=root/'output/site-preview/symptoms/index.html'
    articles=list(page.parent.glob('*/index.html'))
    hashes={p:hashlib.sha256(p.read_bytes()).hexdigest() for p in articles}
    backup=root/'output/identity-backup/symptoms-before-approved-series.html'
    if not backup.exists(): backup.write_bytes(page.read_bytes())
    doc=html.fromstring(page.read_text(encoding='utf-8'))
    links=doc.xpath('//ul[@class="lbsym-list"]//a')
    assert len(links)==len(ART)==16
    dest=root/'output/site-preview/assets/illustrations'
    dest.mkdir(exist_ok=True)
    for a in links:
        slug=a.get('href').strip('/').split('/')[-1]
        label=a.find('span[@class="symptom-caption"]').text
        for child in list(a): a.remove(child)
        a.text=None
        a.set('class','symptom-master-card')
        a.insert(0,html.fromstring(artwork[slug]))
        caption=html.Element('span',{'class':'symptom-caption'})
        caption.text=label
        arrow=html.Element('span',{'aria-hidden':'true'});arrow.text='↗'
        caption.append(arrow);a.append(caption)
        (dest/f'{slug}-master.svg').write_text(artwork[slug],encoding='utf-8')
    for node in doc.xpath('//style[@id="symptom-master-pilot"] | //link[contains(@href,"symptom-series")]'):
        node.getparent().remove(node)
    doc.find('body').append(html.Element('link',rel='stylesheet',href='/assets/symptom-series.css?v=1'))
    page.write_text('<!doctype html>\n'+html.tostring(doc,encoding='unicode'),encoding='utf-8')
    selected=list(illustrations())
    study=html.fromstring(html.tostring(doc,encoding='unicode'))
    for card in study.xpath('//ul[@class="lbsym-list"]//a'):
        if card.get('href').strip('/').split('/')[-1] not in selected:
            card.getparent().getparent().remove(card.getparent())
    for section in study.xpath('//section[@class="lbsym-block"]'):
        if not section.xpath('.//li'):section.getparent().remove(section)
    study.xpath('//h1')[0].text='筋骨疼痛・局部插畫'
    (page.parent/'musculoskeletal-study.html').write_text('<!doctype html>\n'+html.tostring(study,encoding='unicode'),encoding='utf-8')
    assert all(hashlib.sha256(p.read_bytes()).hexdigest()==v for p,v in hashes.items())
    print('16 approved-master cards, 16 exported SVGs; article hashes unchanged.')

if __name__=='__main__': build()
