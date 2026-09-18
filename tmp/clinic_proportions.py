"""Five-pose proportion proof, awaiting user approval before wider rollout.

Unprojected adult skeleton: H=52, stature=6.75H, head width=40,
shoulders=92 (2.3 head widths), crown-to-hip=3.5H, thigh=1.6H,
shin=1.6H, upper arm=1.25H, forearm=1.18H, hand=.72 face length.
Seated joints rotate; segment length is not stretched to reach a symptom.
All five use identical head transform, shared limb widths, 400x360 artboard,
and identical optical crop. Standing legs continue beyond the 3/4 frame.
"""
import math
from clinic_character_master import face, PALETTE

TOKENS=dict(head_height=52, head_scale=52/88, shoulder_width=92,
            upper_arm=65, forearm=61, thigh=83, shin=83,
            arm_width=17, wrist_width=12, palm_length=29,
            stroke=1.3, shadow_opacity=.4)

def p(d,fill='none',stroke='none',w=1.3):
 return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def oval(x,y,rx,ry,c,opacity=1):return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{c}" opacity="{opacity}"/>'
def limb(points,color,width):
 # Joint centers are explicit; rounded joins create a continuous limb silhouette.
 d='M'+'L'.join(f'{x},{y}' for x,y in points)
 return p(d,stroke=color,w=width)
def hand(x,y,angle=0):
 return f'<g transform="translate({x} {y}) rotate({angle})">'+p('M-6 0L-7 11L-10 17Q-11 21 -8 21L-4 16L-4 28Q-3 32 -1 28L0 18L1 30Q3 32 4 28L4 18L6 27Q8 29 9 25L8 14L9 21Q12 22 11 17L8 7L6 0Z','var(--skin)')+p('M-3 10L5 11M0 18V25',stroke='#bc967e',w=1)+'</g>'
def head(x,y,role,angle=0):
 # x,y anchor the crown center. Head outline is shared, never independently scaled.
 h=face().replace('M184 87Q190 87 196 83M211 83Q216 87 221 87','M185 86Q190 84 195 85M211 85Q216 84 220 86').replace('M197 117Q203 111 211 116','M198 115Q204 114 210 115').replace('M186 94Q191 96 196 93M211 93Q216 96 220 94','M187 94Q191 92 195 94M212 94Q216 92 220 94')
 if role=='woman':
  h=oval(154,104,14,25,'var(--hair)')+h
 if role=='middle':h=h.replace('fill="var(--hair_light)"','fill="#a09081"')
 h+=oval(191,94,1.3,1.8,'var(--brown)')+oval(216,94,1.3,1.8,'var(--brown)')
 return f'<g data-head-scale="{TOKENS["head_scale"]}" transform="translate({x} {y}) rotate({angle}) scale({TOKENS["head_scale"]}) translate(-200 -44)">'+h+'</g>'
def torso(cx=190,shoulder=128,hip=235,lean=0):
 return f'<g transform="rotate({lean} {cx} {hip})">'+p(f'M{cx-17} {shoulder-7}Q{cx-42} {shoulder-5} {cx-48} {shoulder+12}L{cx-51} {shoulder+39}L{cx-30} {shoulder+46}L{cx-27} {hip-7}Q{cx} {hip+5} {cx+31} {hip-6}L{cx+27} {shoulder+41}L{cx+48} {shoulder+35}Q{cx+45} {shoulder-2} {cx+16} {shoulder-7}Q{cx} {shoulder+5} {cx-17} {shoulder-7}Z','var(--sage)')+p(f'M{cx+22} {shoulder+13}L{cx+27} {hip-7}L{cx+13} {hip-3}Q{cx+22} {shoulder+57} {cx+12} {shoulder+26}Z','var(--sage_shadow)')+p(f'M{cx-17} {shoulder-7}Q{cx} {shoulder+9} {cx+16} {shoulder-7}',stroke='var(--cream)',w=4)+p(f'M{cx-20} {hip-16}Q{cx} {hip-9} {cx+20} {hip-15}',stroke='var(--sage_shadow)',w=1.1)+'</g>'
def chair(y=236):
 return p(f'M120 {y}H256V{y+9}H120Z','var(--mustard)')+p(f'M132 {y+9}L124 331M242 {y+9}L250 331',stroke='var(--brown)',w=5)
def cue(x,y):return oval(x,y,15,12,'var(--terracotta)',.19)
def wrap(body,color,role):
 palette=dict(PALETTE)
 palette.update(sage=color[0],sage_shadow=color[1])
 style=';'.join(f'--{k}:{v}' for k,v in palette.items())
 return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="30 26 340 306" style="{style}" data-character="{role}" data-proportion-system="adult-6.75h-v1" aria-hidden="true" focusable="false">'+oval(202,193,121,129,'var(--cream)')+oval(199,331,92,4,'#ded6c7',.4)+body+'</svg>'

def samples():
 out={}
 # Knee: seated, horizontal thigh then vertical shin. Arms reach the raised knee.
 legs=limb([(174,228),(252,245),(247,327)],'var(--blue)',26)+limb([(192,231),(269,235),(285,315)],'#8096a1',25)+p('M237 323L256 323L268 332H237Z','var(--brown)')
 arms=limb([(145,161),(160,218),(216,244)],'var(--skin)',17)+hand(216,244,-76)+limb([(228,160),(247,215),(259,236)],'var(--skin)',16)+hand(259,236,8)
 out['knee-pain']=wrap(chair()+legs+torso(186,124,232)+head(186,57,'middle',5)+arms+cue(251,246),('#9cae9c','#819783'),'middle')
 # Foot: seated figure, opposite ankle crossed above the planted knee.
 # Thigh and calf rotate around explicit hip/knee/ankle anchors (not shortened).
 legs=limb([(174,229),(254,246),(251,327)],'var(--blue)',25)+limb([(192,229),(251,287),(299,222)],'#8096a1',25)
 foot=p('M291 215L305 222L305 244L314 256Q315 263 307 260L296 249L286 231Z','var(--skin)')
 arms=limb([(154,156),(198,202),(254,226)],'var(--skin)',17)+hand(254,226,-72)+limb([(234,153),(266,206),(287,224)],'var(--skin)',16)+hand(287,224,-26)
 out['plantar-heel-pain']=wrap(chair()+legs+foot+torso(194,123,231,8)+head(211,55,'young',9)+arms+cue(300,243),('#c59984','#ad806e'),'young')
 # 3/4 views: preserve full torso length; crop continuing legs at the upper calf.
 legs=p('M161 230L218 230L229 339H209L193 266L183 339H160L170 266Z','var(--blue)')
 arms=limb([(155,171),(159,229),(173,282)],'var(--skin)',16)+hand(173,282,-15)+limb([(238,167),(262,223),(211,244)],'var(--skin)',17)+hand(211,244,76)
 out['low-back-pain']=wrap(legs+torso(191,128,241,7)+head(209,60,'middle',7)+arms+cue(224,243),('#99aeba','#7f97a5'),'middle')
 sciaticarms=limb([(153,170),(157,231),(168,285)],'var(--skin)',16)+hand(168,285,-8)+limb([(233,168),(251,229),(221,272)],'var(--skin)',17)+hand(221,272,15)
 out['sciatica']=wrap(legs+torso(188,128,241,3)+head(197,59,'adult',3)+sciaticarms+p('M213 251Q228 262 215 283L209 308',stroke='var(--terracotta)',w=2.5),('#c5b6a0','#ab9a84'),'adult')
 # Shoulder-neck junction: upper arm ~65, forearm ~61, small palm rests on trapezius.
 arms=limb([(144,170),(145,199),(152,257)],'var(--skin)',16)+hand(152,257,-3)+limb([(233,168),(249,196),(220,150)],'var(--skin)',17)+hand(220,150,132)
 out['neck-shoulder-pain']=wrap(p('M161 232H223L229 332H157Z','var(--blue)')+torso(190,128,241)+head(190,62,'woman')+arms+cue(211,140),('#9cae9c','#819783'),'woman')
 return out
