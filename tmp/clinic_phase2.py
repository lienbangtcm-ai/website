"""Second-stage refinement. Layout is unchanged; four reusable adult characters.
All faces use the approved geometry. Clothing changes via named palette tokens.
No external assets, raster generation, gradients, or anatomy magnifier badges.
"""
from lxml import etree
from clinic_character_master import face, PALETTE

COLORS={
 'sage':('#9cae9c','#819783'), 'blue':('#99aeba','#7f97a5'),
 'terracotta':('#c59984','#ad806e'), 'mustard':('#ccba8c','#b29e74'),
 'pink':('#c5a2a0','#af8988'), 'beige':('#c5b6a0','#ab9a84'),
 'lavender':('#b3abc3','#9990aa'),
}
CAST={
 'gerd':('adult','sage'), 'cough':('middle','blue'),
 'insomnia':('young','blue'), 'allergic-rhinitis':('woman','lavender'),
 'diarrhea':('young','mustard'), 'constipation':('middle','beige'),
 'menstrual-pain':('woman','pink'), 'fatigue':('young','blue'),
 'frozen-shoulder':('middle','terracotta'), 'neck-shoulder-pain':('woman','sage'),
 'low-back-pain':('middle','blue'), 'sciatica':('adult','beige'),
 'knee-pain':('middle','sage'), 'tennis-elbow':('adult','mustard'),
 'de-quervain':('woman','lavender'), 'plantar-heel-pain':('young','terracotta'),
}
def p(d,c='none',s='none',w=1.4):
 return f'<path d="{d}" fill="{c}" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def skin(d):return p(d,'var(--skin)')
def ink(d):return p(d,s='#b58e78',w=1.2)
def symptom(d):return p(d,s='var(--terracotta)',w=2.5)
def e(x,y,rx,ry,c,opacity=1):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" opacity="{opacity}"/>'
def glow(x,y):return e(x,y,15,13,'var(--terracotta)',.18)
def head(x=200,y=90,angle=0):
 return f'<g transform="translate({x-200} {y-90}) rotate({angle} 200 140)">'+face()+'</g>'
def shirt(d):return p(d,'var(--sage)')
def pants(d):return p(d,'var(--blue)')
def scene(content):
 style=';'.join(f'--{k}:{v}' for k,v in PALETTE.items())
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 360" style="{style}" aria-hidden="true" focusable="false">'+e(202,193,121,129,'var(--cream)')+e(199,325,93,4,'#ded6c7',.4)+content+'</svg>'

def direct_poses():
 out={}
 # Three-quarter side view with mild forward bend, hand flat against lumbar area.
 lower=pants('M163 244L225 239L235 314H217L199 271L186 317H164L177 270Z')
 body=shirt('M183 137Q161 140 153 159L146 211L160 247Q191 263 229 244L222 207L231 184Q237 158 211 144Z')+p('M211 148Q223 172 214 207L228 244L211 249L201 203Z','var(--sage_shadow)')
 arms=skin('M152 180L166 184L164 227L172 247Q177 253 173 256L163 250Q153 242 151 231Z')+skin('M225 178L239 183L250 217Q250 228 238 235L219 241L207 241Q201 238 206 235L219 231L209 232Q204 230 210 227L231 220L231 214Z')+ink('M216 234L225 231')
 out['low-back-pain']=scene(lower+body+head(195,86,10)+arms+glow(218,233))
 # Same profile, posterior thigh line lies on clothing rather than in a circle.
 out['sciatica']=scene(pants('M163 241L225 238Q237 253 225 275L215 317H194L204 267L191 263L174 318H153L165 267Z')+body+head(195,86,8)+arms+symptom('M213 243Q230 257 215 274L208 302')+glow(219,253))
 # One foot planted on a low step; knee bent and hand clearly rests on knee.
 step=p('M228 304H299V322H228Z','var(--mustard)')
 legs=pants('M154 218L211 216Q230 224 252 244Q260 251 256 267L250 305H229L235 267L199 250L181 315H158L170 256Z')
 top=shirt('M166 132Q147 141 143 160L137 207L154 226Q183 242 216 225L211 181L223 169Q222 146 200 137Z')
 arms=skin('M145 174L160 180L176 215L227 242L242 246Q248 249 245 253L229 250L218 248L164 230Q158 228 155 220Z')+skin('M211 165L226 171L232 201L247 237L249 248Q247 254 244 250L238 241L230 233L217 207Z')
 out['knee-pain']=scene(step+legs+top+head(180,80,7)+arms+glow(241,252))
 # Opposite hand cups the lateral elbow; no detail badge.
 from clinic_character_master import torso
 elbow=skin('M121 221L143 229L149 252L206 253L217 247Q223 246 224 250L218 255L226 254Q232 255 228 259L218 268L157 280Q137 283 130 265Z')+p('M126 237L139 263Q145 275 159 274L218 264L218 268L157 280Q137 283 130 265Z','var(--skin_shadow)')
 support=skin('M259 226L277 222L275 248Q273 259 260 266L170 275L153 271Q145 269 146 264L153 258L160 256L157 262L170 263L249 248L257 237Z')+ink('M151 265L160 267M157 261L166 263')
 out['tennis-elbow']=scene(torso()+head()+elbow+support+glow(146,266))
 # Caregiving scene: an adult-sized woman cradles a swaddled infant.
 cradle=skin('M121 221L143 229L151 254L212 260L222 266Q226 270 220 272L207 272L150 278Q135 277 130 264Z')+skin('M259 226L276 220L279 253Q277 268 264 270L231 261L218 258Q212 254 218 251L231 252L259 251Z')
 blanket=p('M172 209Q187 194 211 201L247 224Q258 238 244 256Q234 268 218 260L169 234Z','#dfc79c')+p('M181 216Q207 218 242 251L232 259L183 235Z','#cab084')+p('M189 212L218 244M200 209L239 237',s='#bba278',w=1.3)
 baby=e(171,212,18,22,'var(--skin)')+p('M155 208Q153 187 172 189Q185 190 188 203Q169 197 155 208Z','var(--hair)')+ink('M162 215q3 2 6 0M175 215q3 2 6 0M169 224h5')
 out['de-quervain']=scene(torso()+head()+blanket+baby+cradle+glow(224,260))
 # Seated figure crosses one ankle over the opposite knee and cups the heel.
 chair=p('M112 242H247V258H112Z','var(--mustard)')+p('M122 258L115 322H122L132 258M232 258L238 322H245L242 258','var(--brown)')
 leg=pants('M139 222L203 221Q221 231 223 246L213 318H191L191 264L154 258Q135 252 139 222Z')+pants('M156 239Q161 227 177 235L224 260L268 268L265 283L219 282L164 261Z')
 foot=skin('M263 267L279 265L284 284L296 293Q303 300 293 303L271 296L260 285Z')
 top=shirt('M157 134Q139 140 132 159L123 205L140 229Q172 246 207 226L204 186L215 170Q211 148 191 138Z')
 hands=skin('M129 181L146 186L166 217L236 274L264 284Q270 289 265 292L250 288L230 280L155 232Q147 226 144 217Z')+skin('M202 174L217 179L218 220L259 271L273 280Q276 284 272 286L259 280L250 273L202 229Z')
 out['plantar-heel-pain']=scene(chair+leg+foot+top+head(174,80,8)+hands+glow(275,290))
 return out

def refine(source):
 art=dict(source)
 art.update(direct_poses())
 # For diarrhea, show cramping rather than the same organ stencil as constipation.
 root=etree.fromstring(art['diarrhea'].encode())
 for n in list(root.iter()):
  if isinstance(n.tag,str) and n.tag.endswith('path') and (n.get('fill')=='#f3ddc9' or n.get('stroke') in ('#ba937b','#bc9983') or n.get('d','').startswith('M201 237')):
   n.getparent().remove(n)
 g=root.find('.//{http://www.w3.org/2000/svg}g')
 g.append(etree.fromstring(('<g xmlns="http://www.w3.org/2000/svg">'+glow(208,251)+symptom('M226 226l-6 8 7 4 -6 8')+'</g>').encode()))
 art['diarrhea']=etree.tostring(root,encoding='unicode')
 # Reposition the neck hand toward the shoulder-neck junction, not the jaw.
 art['neck-shoulder-pain']=art['neck-shoulder-pain'].replace('L199 139Q198 133 202 133Q205 133 209 143L211 129Q214 125 217 130L218 145L224 135Q228 132 230 136L224 153','L211 154Q209 148 213 147Q216 146 220 155L225 144Q230 142 232 146L230 157L237 151Q242 150 242 154L231 166')
 for slug,svg in art.items():
  role,color=CAST[slug]
  root=etree.fromstring(svg.encode())
  # 17.6% optical enlargement, no CSS/layout changes. 14px extra lower clearance.
  root.set('viewBox','30 26 340 306')
  root.set('data-character',role)
  style=root.get('style','')
  a,b=COLORS[color]
  import re
  style=re.sub(r'--sage:[^;]+', '--sage:'+a,style)
  style=re.sub(r'--sage_shadow:[^;]+','--sage_shadow:'+b,style)
  root.set('style',style+';--lavender:#b3abc3;--beige:#c5b6a0')
  for node in list(root.iter()):
   if not isinstance(node.tag,str):continue
   d=node.get('d','')
   # Shared mild-discomfort face across all four adults; use action for emphasis.
   if d=='M184 87Q190 87 196 83M211 83Q216 87 221 87':
    node.set('d','M185 86Q190 84 195 85M211 85Q216 84 220 86')
   if d=='M186 94Q191 96 196 93M211 93Q216 96 220 94':
    node.set('d','M187 94Q191 92 195 94M212 94Q216 92 220 94')
    if slug not in ('fatigue','insomnia'):
     eyes=etree.fromstring(('<g xmlns="http://www.w3.org/2000/svg">'+e(191,94,1.25,1.65,'var(--brown)')+e(216,94,1.25,1.65,'var(--brown)')+'</g>').encode())
     node.getparent().insert(list(node.getparent()).index(node)+1,eyes)
   if 'M197 117Q203 111 211 116' in d:
    node.set('d',d.replace('M197 117Q203 111 211 116','M198 115Q204 114 210 115'))
   # Four controlled hairstyles; identical face proportions and skin tokens.
   if node.get('fill')=='var(--hair)' and d.startswith('M166 88'):
    if role=='woman':node.set('d','M166 88Q151 71 160 55Q172 38 195 41Q222 38 232 59Q239 77 229 94L220 86L217 65Q198 72 185 57Q180 79 173 88L171 100L164 99Z')
    elif role=='young':node.set('d','M166 88Q153 77 162 58L160 48L174 48Q184 34 205 42Q225 39 232 58L229 87L220 84L217 63Q195 77 181 64Q179 82 172 91L172 99L167 97Z')
    elif role=='middle':node.set('d','M166 88Q155 72 166 55Q177 43 191 44Q219 40 231 59L229 87L221 85L218 65Q202 62 191 56Q179 63 173 87L171 99L167 97Z')
   if role=='middle' and node.get('fill')=='var(--hair_light)':node.set('fill','#a08f80')
  # Add a ponytail behind the same female face, except existing tied-back heroine.
  if role=='woman' and slug!='menstrual-pain':
   for node in list(root.iter()):
    if not isinstance(node.tag,str):continue
    if node.get('d','').startswith('M181 111'):
     parent=node.getparent();parent.insert(list(parent).index(node),etree.fromstring(('<ellipse xmlns="http://www.w3.org/2000/svg" cx="155" cy="104" rx="13" ry="26" fill="var(--hair)"/>').encode()));break
  # Bedding uses the same dusty-blue family; keep moon soft mustard.
  if slug=='insomnia':
   root.set('style',root.get('style').replace('--sage:'+a,'--sage:#99aeba').replace('--sage_shadow:'+b,'--sage_shadow:#7f97a5'))
  art[slug]=etree.tostring(root,encoding='unicode')
 return art
