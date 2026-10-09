# Visual refinement — 2026-10-09

Local preview: http://127.0.0.1:8876/ . Existing HTML/CSS/JS and WordPress architecture retained.

| Capture | Corrections / evidence |
| --- | --- |
| baseline | Eight pages × 1440/768/390px. Doctor images inherited original HTML height attributes; team page was 7081px tall at 1440px. Homepage was 2838px tall. |
| round-1 | Constrain doctor images within equal aspect-ratio frames; retain alternate profile layout. Reduce homepage inflated cards and section spacing. 24 browser checks passed. |
| round-2 | Adjust original portrait framing without altering faces. Fix mobile header spacing, hero text contrast, CTA colors and timeline image sizing. Correct active navigation in shared JS. 24 checks passed. |
| round-3 | Reduce pulse hero/booking spacing, refine homepage proportions, improve tablet grids. Remove duplicate focus label. 24 checks passed. |
| final | Hide floating booking control visually except keyboard focus, retaining ordinary booking CTAs. Fix mobile service hero image height and large blank region, compact About mobile cards and timeline. 24 checks repeated after changes. |

Each round includes full-page screenshots and report.json. Baseline and three rounds include proportional side-by-side, overlay and difference images. Full-resolution images remain local (gitignored); the compressed before/after gallery is versioned under output/site-preview/review/. Reference files remain the user-supplied originals in Downloads/Temp.

158 internal link clicks succeeded; 50 additional existing local HTML pages were opened at 390px, with no horizontal overflow. See click-regression.json. External LINE/telephone CTAs were inspected, not sent or called. Existing FAQ and mobile menu interactions were tested; no claim of full behavior coverage for every subpage.

Remaining visual differences: original doctor portraits have white backgrounds; symptom photography and some specialist procedure assets are missing; About hero background and brand video differ; existing medical copy and six integration process items are preserved even where the reference has different wording/counts. Only the homepage has a separate phone reference. Desktop references are scaled proportionally to 1440px; tablet/phone comparisons from desktop references are illustrative, not pixel-accuracy scores. No 100% restoration claim.

Run from repository root (Windows runtime paths can be replaced using PLAYWRIGHT_PATH):

```powershell
python -m http.server 8876 --bind 127.0.0.1 --directory output/site-preview
node tools/visual-qa.cjs final
node tools/click-regression.cjs
python tools/compare-visuals.py round-3
python tools/build-review.py
```

Dependencies: Playwright with Edge/Chromium, Python Pillow. No GitHub Actions required for development. No live WordPress changes, main merge, or deletion of important content.
