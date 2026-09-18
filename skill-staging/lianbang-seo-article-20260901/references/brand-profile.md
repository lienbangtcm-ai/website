# 連邦中醫文章設定

## Identity

- Language and audience: Traditional Chinese for readers in Taiwan.
- Clinic: 連邦中醫診所.
- Article body metadata: omit author names and publication/update dates from visible article content.
- Tone: clear, calm, professional, approachable; avoid fear and guaranteed outcomes.

## Visual system

- Primary: `#00897b`
- Secondary: `#e0f2f1`
- Heading: `#004d40`
- Text: `#333333`
- Background: warm white or light gray.
- Visual style: teal and ivory medical editorial illustration with restrained coral-red warning accents.
- Featured image: generate a 1200×630 WebP/JPEG asset only when the input includes a cover/featured slot or the user explicitly requests one. Deliver it separately for website backend configuration; never insert it into article body HTML.
- Inline image: 1200×800.
- Image quantity: follow the explicit slots, prompts, or quantity in the supplied content. Generate exactly that number and never add images to satisfy a default package.
- Output: WebP primary and JPEG fallback, ideally below 200 KB each.

## Fixed conversion action

- Button label: `立即預約評估 (LINE)`
- URL: `https://lin.ee/UWWKmse`
- Attributes: `target="_blank" rel="noopener noreferrer"`
- CTA heading: `讓專業團隊成為您的健康後盾`

## Media publishing

- Known storage host: `https://twyuting10210314859.admin.metabiz.tw/storage/twyuting10210314859/`
- Storage paths include year and month; do not guess the active folder. Derive it from one confirmed uploaded asset URL supplied by the user.
- Validate `Content-Type` starts with `image/` and the response succeeds before inserting a public URL.

## SEO and safety defaults

- Use one H1 and descriptive H2/H3 hierarchy.
- Write alt text for meaning, not keyword stuffing.
- Do not display image captions beneath article images; keep the meaning in Traditional Chinese `alt` text.
- Do not claim guaranteed cures, replace necessary medical assessment, or imply that illustration alone is diagnostic.
- Include urgent-care guidance when the article discusses red flags.
- Do not include unfinished extended-reading links.
- Never leave `contenteditable="true"` in published HTML because it interferes with normal link clicking.
