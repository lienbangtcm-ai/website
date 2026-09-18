---
name: lianbang-seo-article
description: Build complete, illustrated Traditional Chinese SEO articles for 連邦中醫診所 from pasted drafts or HTML. Use when Codex should structure a clinic article, create or place medical illustrations, produce publish-ready responsive HTML, apply the clinic's visual identity and LINE booking CTA, replace uploaded media URLs, or validate links and image delivery before publication.
---

# 連邦中醫 SEO 文章

Read [references/brand-profile.md](references/brand-profile.md) and [references/standard-layout.md](references/standard-layout.md) before producing or editing an article. Use [assets/standard-article-template.html](assets/standard-article-template.html) as the default structural and visual starting point unless the user explicitly asks for another format.

## Workflow

1. Inspect the supplied draft or HTML. Preserve the author's meaning and do not invent medical evidence, diagnoses, treatment outcomes, citations, clinic services, or patient stories.
2. Produce one responsive HTML deliverable under the current workspace's user-facing output directory. Start from the saved standard template and replace its topic-specific content and assets without carrying GERD-specific facts into another article.
3. Structure the article with exactly one H1, a short introduction, navigable H2/H3 sections, FAQ when supported by the draft, and the fixed LINE CTA.
4. Remove visible author names and publication/update dates from the article body, including metadata rows beneath the H1.
5. Omit unpublished internal links. Never publish a placeholder, guessed URL, or known 404. Add an extended-reading block only after its destination returns successfully.
6. Make clinic articles image-led by default. When the user does not state a quantity, plan four topic-specific inline images that correspond to major sections, matching the approved template. Follow a different explicit image count when provided. Treat a supplied cover or featured-image slot separately from inline images.
7. Freeze the image plan before generation. Do not reuse an illustration from another condition when its medical meaning does not match the new article.
8. Reuse a supplied prompt and placement when suitable; refine it only for medical safety, brand style, composition, and text avoidance. Do not create speculative variants or replacement images unless an output fails a required safety or usability check.
9. Generate a 1200×630 featured image only when the supplied content includes a cover/featured slot or the user requests one. Deliver it separately for website backend configuration and never insert it into article-body HTML. Keep the focal subject in the central safe area and avoid embedded title text unless requested.
10. Use 1200×800 for requested inline images. Insert them only at their supplied or clearly associated section. Prefer real user-supplied clinic photos for clinic-specific scenes. Use the imagegen skill only for requested educational medical illustrations. Do not fabricate a photo that appears to document the real clinic.
11. Keep image content free of generated text, logos, prescriptions, cure claims, gore, or unnecessary anatomy. Do not show visible captions such as 「概念示意圖」 beneath images; communicate image meaning through useful Traditional Chinese `alt` text.
12. Export every generated image as WebP plus JPEG, target each file below 200 KB, and use descriptive lowercase filenames. Use a `<picture>` element when both formats are deployed; otherwise use the confirmed public JPEG URL.
13. Give every inline image explicit dimensions and useful Traditional Chinese `alt`. Set non-hero inline images to `loading="lazy"`.
14. Remove `contenteditable` from publishable HTML. External links opening a new tab must include `rel="noopener noreferrer"`.
15. If the user uploads images and supplies one public URL, infer sibling URLs only when filenames and folder are confirmed. Check every final image URL for a successful image response; hide or remove a failed figure rather than leaving a broken image.
16. Run `scripts/validate_article.py <html-path>` and fix every error before delivery.

## Saved editorial preferences

- Use the approved aligned layout: 1180px outer shell, 1040px primary content line, and 980px long-form reading width on desktop.
- Keep headings, paragraphs, images, lists, navigation, and CTA controls on consistent left edges. Do not use deliberately offset rows, floating cards, staggered margins, sticky side headings, or ornamental layout tricks.
- Keep headings as plain titles. The only standing English display text is `LIEN BANG TRADITIONAL CHINESE MEDICINE` in the brand area.
- Use restrained teal, warm ivory, 12px image corners, light shadows, clear section spacing, and simple separators. Avoid grids of small cards and AI-template styling.
- Do not add visible image captions, source-reference sections, AI disclaimers, generic red-flag panels, or formulaic notes such as 「食物誘發情況因人而異……再與醫師討論」 unless the user explicitly asks for them.
- Preserve the existing article URL, clinic facts, LINE, phone, map, physician information, and other confirmed links during publication.
- Prepare and preview locally first. Do not publish or update WordPress until the user explicitly approves the finished version.

## Delivery

- Provide the finished HTML, only the requested generated images, and a short list of any assets still awaiting upload. Omit featured-image and image-folder deliverables when none were requested.
- Do not ask the user to repeat saved brand preferences.
- When the publishing platform strips HTML or attributes, explain the exact affected field and provide the smallest compatible replacement.
