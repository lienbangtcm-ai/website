from lxml import html

ICONS=[
 '<path d="M8 34h10l4-12 7 23 6-17 4 6h17M18 12v6m28-6v6M18 48v5m28-5v5"/>',
 '<path d="M16 25h32l-3 27H19zM22 25v-9h20v9M27 16v-5h10v5M25 38h14M32 31v14"/>',
 '<path d="M12 30 32 13l20 17M18 26v26h28V26M27 52V38h10v14M9 13h8m-4-4v8"/>',
 '<circle cx="33" cy="13" r="5"/><path d="m29 22-9 12-10 2m21-14 8 12 14-5M30 23l-4 18-10 12m11-12 12 1 6 11M43 15a18 18 0 0 1 12 9"/>',
 '<path d="m15 49 27-30m-7-2 9 8m-4-14 11 10M12 52l3-3M9 39c4-2 8-2 12 0m14 7h17"/>',
 '<path d="M10 43h44M16 43v11m32-11v11M19 34h14l9-12 10 4M33 34l9 9M10 18l8 8m-4-12 8 8"/><circle cx="17" cy="33" r="4"/>',
 '<path d="m17 50 24-28m-5-7 12 10m-9-16 14 12M13 54l4-4M11 40l8-2"/>',
 '<path d="M9 40c11-6 35-6 46 0M9 49c12-5 34-5 46 0M17 24l25 7m-2-5 7 7M14 23l3 1"/>',
 '<path d="M22 12c-6 6-8 16-5 26s8 16 15 16 12-6 15-16 1-20-5-26M23 29h4m10 0h4M29 40h6M8 17h8m-4-4v8M49 11h7m-3-3v6"/>',
 '<path d="M23 10c3 10 1 15-4 22-4 7-4 15-1 22m23-44c-3 10-1 15 4 22 4 7 4 15 1 22M24 32c5 3 11 3 16 0M28 45h8"/><circle cx="32" cy="26" r="2"/>',
]
GROUPS={
 'internal':[('把脈評估','/pulse-diagnosis/#assessment'),('單味藥組方','/pulse-diagnosis/#why'),('生活照護','/pulse-diagnosis/#assessment')],
 'orthopedics':[('疼痛與活動評估','/acupuncture/#process'),('一般針灸／不留針','/acupuncture/'),('針灸整合物理治療','/acupuncture-physical-therapy/')],
 'self-pay':[('針刀','/針刀/'),('浮針','/浮針/'),('美顏針','/美顏針/'),('穴位埋線','/埋線/')],
}
def simplify(doc):
 n=0
 for id,items in GROUPS.items():
  section=doc.get_element_by_id(id)
  grid=section.xpath('.//*[@class="ls-services" or @class="ls-treatment-grid"]')[0]
  new=html.Element('div',{'class':'ls-entry-grid'})
  for title,url in items:
   a=html.fragment_fromstring(f'<a class="ls-entry" href="{url}"><svg viewBox="0 0 64 64" width="56" height="56" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[n]}</svg><span>{title}</span></a>')
   new.append(a);n+=1
  grid.getparent().replace(grid,new)
  for p in section.xpath('.//p'):p.getparent().remove(p)
  for h in section.xpath('.//h3'):
   if h.text_content()=='我們會做什麼':h.getparent().remove(h)
 for p in doc.xpath('.//*[@id="approach"]//p'):p.getparent().remove(p)
