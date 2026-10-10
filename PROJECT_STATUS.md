# 連邦中醫網站 — Codex 開發交接與進度
更新：2026-10-09（GitHub 儲存庫與歷史文件盤點；不是即時正式站驗收）

## 優先讀取
- 儲存庫：https://github.com/lienbangtcm-ai/website
- 預設分支：main；截至本次查詢可見 main 最新提交 5d4d825（2026-09-18）
- **目前主要改版分支：`sitewide-treatment-dropdown-20260918`**；HEAD `2782af7bbcaefa55c04c74d87e45cad5218deeb7`（2026-09-30）
- 未合併草稿 PR #1：https://github.com/lienbangtcm-ai/website/pull/1
- 查詢時 PR #1 有 269 個 commits、80 個 changed files；不可把 main 當作最新改版。
- 本文件編輯所在分支是上述改版分支；請以實際 HEAD 與檔案內容再查一次，不要假定已合併／已上線。

## 實作與證據分級
以下「完成」指**已在儲存庫或歷史測試報告存在**，**不等於已發布 WordPress 正式網站**。

| 工作流 | 可確認的進度 | 下一步 |
| --- | --- | --- |
| 首頁 | `output/site-preview/index.html`；9/30 commit 替換 reception hero 圖，調整首頁 | 實際視覺、手機、效能檢查及院方審稿 |
| 關於連邦 | `output/site-preview/about-lienbang/index.html`；9/30 多次調整故事圖片、版面、頁尾 | 檢查圖文真實性／裁切／手機版 |
| 共用導航 | `assets/global-shell.css`、`assets/global-shell.js`；PR 主題為治療服務圖片下拉選單，取消舊 subnav | 驗證全頁導航、鍵盤、手機菜單和回歸測試 |
| 治療服務 | `output/site-preview/services/`、`acupuncture/`、`pulse-diagnosis/`、`acupuncture-physical-therapy/` | 逐頁驗收、確認 WordPress 對應正式網址 |
| 自費服務 | `output/site-preview/針刀/`、`浮針/`、`美顏針/`、`埋線/` | 核對醫療敘述、價格、CTA 和發布狀態 |
| 症狀內容 | 2026-09-08 進度檔記錄 16 篇 HTML 與每篇 3 張圖片，並記錄歷史瀏覽器／連結測試通過 | 醫師審稿、正式網址去重、圖片上傳、WordPress 草稿及發布驗收 |
| 醫師團隊 | 分支含 `output/site-preview/team/` 和醫師子頁；7 月報告記錄 WordPress 部分醫師頁仍為草稿 | 核對姓名／資歷／門診與實際發布狀態 |
| SEO | 歷史報告記錄 canonical、H1、AIOSEO 與 Sitemap 已做部分清理 | 檢查實際 live canonical、index/noindex、schema、重導向、GSC |
| 預覽發佈 | `.github/workflows/preview-pages.yml`，預覽目錄 `output/site-preview/`，另有 `dist/` | 查 Actions 與公開預覽是否成功，不要把預覽直接覆蓋 WordPress |
| 效能分析 | 有歷史手機版／桌面版與圖片測試報告 | 重新測量最新提交、正式站 PageSpeed，確認 CWV 與實際使用速度 |

## 關鍵歷史參考
- `output/WEBSITE_PROGRESS_2026-09-08.md`：27 頁預覽、16 篇症狀、發布順序與重要警示；報告說當時尚未整批正式發布。
- `output/current-site-page-checklist-2026-08-26.md`：已做與待確認的 WordPress 清單。
- `lienbang-site-audit/IMPLEMENTATION_PROGRESS_2026-07-24.md`：舊站實作、SEO 與 WordPress 草稿歷史紀錄。
- `output/PREVIEW_RELEASE_PLAN.md` 是較舊版本，部分內容與 9/8 文件衝突；以較新紀錄和現存程式碼為優先，務必註明不確定處。

## 尚未解決的重點
1. PR #1 尚未合併；先確定部署來源與發布方式。
2. 是否將 16 篇症狀文章正式發布、對應網址與 WordPress 資料，尚缺當下正式站查核。
3. `/profile/` 與 `/zhang-yu/` 的主網址、`/contact/`、`/about/`、`/elementor-3725/` 的轉址策略待核定。
4. 內科服務介紹、醫師班表、正式預約 CTA、LINE 入口及診所資訊應再次核對院方現況。
5. 正式站 SEO、GTM/GA4 事件與載入速度需實測。
6. 預覽站若設置 noindex/robots Disallow，**不得直接套用至正式站**。

## Codex 下一次執行
1. checkout 本分支，讀取本文件及上述歷史報告。
2. 列出目前程式結構、各頁可用性與主分支差異；查最新 commits、PR、Actions。
3. 在**不改正式網站**前提下做預覽 smoke tests、連結／圖片／手機版／SEO 檢查，區分「歷史測試」與「本次實測」。
4. 輸出短表：完成／部分完成／待處理／阻擋，附證據路徑和優先順序。
5. 先提出最優先的 3 個修改任務，再按院方確認逐項實作。
6. 每次任務完成更新本文件，標示日期、分支、SHA、已做修改、測試結果、是否上線與後續事項；不得把本地未 push 的內容寫成已同步。

## 安全原則
- 現有網站基於 WordPress / Elementor / Astra 的歷史資料；不要在沒明確指示時重建 Next.js 或重構整站。
- 保留目前頁面內容、醫師資料、真實照片、Logo、既有 CTA 和 WordPress 設定。
- 不捏造治療療效、患者評價、醫師資歷或看診時間。
- 不要未經確認就合併 PR、對正式站推送、修改 DNS、批次刪頁或執行轉址。

## 2026-10-09 本機參考圖改版進度
- 工作目錄：C:/Users/yutin/Documents/網站相關/website；分支 sitewide-treatment-dropdown-20260918；基礎提交 c06b77d09b3d58caee1b0b68a231ccd90234cfc5。
- 首頁已調整字級、區塊留白、導覽比例、主視覺文字及預約區間距，三位醫師改用使用者提供原照並統一首頁卡片大小。已複製至本機 repository 預覽；複製後首頁仍需再驗證。
- 關於連邦、治療服務、常見症狀、醫師團隊、針灸、中醫內科／脈診、中醫×物理治療七頁已加入參考圖版面樣式，保留既有連結與醫療內容。這是本機預覽修改，沒有重建 WordPress／Elementor／Astra。
- 七頁在 390px 與 1440px 共 14 組瀏覽器檢查通過：無水平溢出、每頁一個 H1、圖片正常載入、無 JavaScript 或 HTTP 錯誤；手機選單及存在的 FAQ 鍵盤操作正常。證據：output/reference-design-qa/browser-checks.json 與同目錄截圖。
- 尚未完全符合參考圖：各頁乾淨主圖、16 張症狀照片、部分治療圖片、創辦人合照及品牌影片待補；使用者已回覆正在準備。整合治療等部分區塊仍保留原內容數量，待逐項視覺驗收。
- 下一步優先順序：1. 驗證 repository 內首頁與手機實際排版；2. 收到素材後替換並逐頁對照；3. 圖片壓縮與載入速度量測；4. 正式站 SEO、LINE 預約目的地與發布驗收。
- 尚未 commit、push、合併 PR 或上線。不可把本機預覽測試描述為正式站測試或完全一致。

### 素材套用與可操作預覽
已收到 12 張圖片，轉為 WebP 保存於 assets/user-20261009，套用服務、脈診、針灸、整合治療、醫師團隊及症狀頁主視覺與部分療程卡片；保留真實診所首頁與個別醫師原照。七頁 14 組測試再次通過，首頁 390/1440px 兩組另行通過，證據 home-browser-checks.json。本機伺服器 http://127.0.0.1:8876/；停止後需於 output/site-preview 執行 python -m http.server 8876 --bind 127.0.0.1。仍待症狀原圖、專屬療程照片及關於頁素材，尚未完全符合參考圖，尚未 push 或上線。

## 2026-10-09 本機自主開發與視覺驗收
- 保留原有未提交修改，在 sitewide-treatment-dropdown-20260918 工作；未重建網站、刪除重要內容或變更正式 WordPress。
- 修正醫師圖片 HTML 原始高度與 CSS 比例衝突，統一容器、左右交錯排列、原照裁切與字級；移除重複「主要方向」文字。
- 修正首頁過大的卡片、留白與文章列表排版；修正手機頁首對齊、LINE 按鈕換行、服務主視覺半高圖片與下方空白、症狀／整合治療主視覺對比、關於頁手機卡片与圖片排列、脈診頁過高區塊。依路徑標示導覽 active，保留預約入口。
- 八頁依首頁、服務、症狀、醫師、關於、針灸、脈診、整合順序，於 1440/768/390px 保存 baseline、round-1、round-2、round-3 和 final 完整截圖與各輪 report.json。最後 24 組檢查包含圖片、H1、水平溢出、手機選單／Escape、FAQ 與內部連結狀態。
- 實際點擊 158 個內部連結無 404，另外 50 個既有 HTML 子頁在 390px 無水平溢出；這是 smoke checks，不代表其所有操作與視覺都已完整驗收。LINE／電話只核對入口，沒有傳訊或撥號。
- 參考圖等比縮放至相同寬度，保存並排、疊圖與差異圖；比較無法排除原照片與文字差異，不宣稱 100% 還原。除首頁外沒有獨立手機參考圖。
- 原始完整證據 output/visual-qa/ 留在本機（圖片 gitignored）；可攜式壓縮前後截圖與對照頁位於 output/site-preview/review/。工具位於 tools/visual-qa.cjs、click-regression.cjs、compare-visuals.py、build-review.py；操作與每輪變更見 output/visual-qa/CHANGELOG.md。
- 本機預覽 http://127.0.0.1:8876/；醫師頁 /team/；對照頁 /review/。若伺服器停止，從 repository 執行 python -m http.server 8876 --bind 127.0.0.1 --directory output/site-preview。
- 尚未一致：個別醫師原照白底、16 張症狀照片未補、關於頁主圖背景與品牌影片未補、部分專屬療程照片未補、整合治療保留六步原內容。不能把 AI 情境素材視為實際診所／醫師紀實照片。
- 使用者已授權完成後提交並推送開發分支。GitHub Pages workflow 只接受 workflow_dispatch；本次不啟動 Actions、不合併 main、不改正式網站。提交和 push 結果以後續 Git 紀錄為準。

### 本次 GitHub 同步結果
程式與驗收資料提交 fd28cac（Refine eight reference pages with local visual QA and review gallery）已成功推送 origin/sitewide-treatment-dropdown-20260918。對照頁 /review/ 已由 Playwright 檢查：8 個頁面、48 張前後截圖全部載入正常。下一次先看 /review/ 與尚未一致清單，再接續替換缺少素材。本段為同步後交接紀錄。

## 2026-10-09 關於連邦頁面專項修正
- 新增僅作用於 lb-about 的 about-polish-20261009.css，保留原合照、所有故事文字與連結，不影響其他頁面。
- 統一 #fffdf9／#f8f3eb／#493023 色系，主視覺增加過渡漸層，恢復主標題、副標題與英文標籤層級；核心理念欄加寬，避免單字落行。
- 修正故事區舊固定高度造成的文字裁切與左右邊界不齊；時間軸使用一致圓圖、下方文字與水平連線；團隊照片等高等寬，手機兩欄。
- 三輪完整截圖與報告位於 output/visual-qa/about-polish、about-polish-2、about-polish-3；每輪 1440/768/390px 三組檢查通過（H1、圖片、水平溢出、選單/Escape、內部連結狀態）。
- 最新頁面 /about-lienbang/；前後對照與設計圖疊圖 /review/about-update/；tools/about-qa.cjs 和 about-review.py 可重跑。
- 仍待素材：合照背景與原參考不同，品牌影片未提供；不新增虛構照片或假的播放功能。未變更正式 WordPress。

### 小巨蛋總院門面照片替換
已依使用者提供的真實門面照，替換關於頁「第一家物理治療所」時間軸圖片為 assets/clinic-photos/ptc-arena-exterior.webp，補正 alt 並調整圓形焦點。保留標題與文字。1440/768/390px 三組檢查通過，證據 output/visual-qa/about-arena-photo/report.json 與同目錄截圖。正式 WordPress 未修改。

### 關於頁桌面文字放大
依使用者要求，1024px 以上桌面版主視覺內文調為 20px、故事／團隊內文 19px、理念文字 18px、時間軸描述 17px，增加行距並調整文字欄寬與區塊留白。標題與按鈕同步放大，手機保持原閱讀尺寸。1440/768/390px 三組檢查通過，證據 output/visual-qa/about-desktop-type/report.json。

### 關於頁文案精簡
依使用者確認，移除主視覺重複介紹與英文小標，故事合併為一段並保留台大相識及兩種專業背景；四項理念各留一句，時間軸保留照片與事件名稱，團隊介紹縮短為一句。保留原照片、重要背景、較大的桌面字體及預約入口。1440/768/390px 三組瀏覽器檢查通過，完整前後截圖分別位於 output/visual-qa/about-desktop-type 與 about-concise，後者 report.json 無失敗。舊 /review/about-update/ 為前一輪排版對照，最新文案請看 /about-lienbang/?revision=concise-copy。正式 WordPress 未修改。

### 關於頁連續排版調整
依使用者要求減少四格切割與空虛感：故事、理念、歷程與團隊改用連續米白背景，移除理念直線，縮減區塊留白與首屏高度；理念標題改置於內容上方，避免短句落字。團隊圖片改為主次拼排，保留全部四張素材，醫師原照使用 contain 避免頭部裁切。1440/768/390px 三組檢查通過，修正前 about-concise、修正後 about-flow-final 截圖與 report.json 留在 output/visual-qa。預覽 /about-lienbang/?revision=continuous-flow。未改正式 WordPress。

### 關於頁擴充內容版本
使用者認為緊湊版仍空虛，明確要求放大每段並增加文字與排版層次。本次主視覺 520px、故事照片 420px，故事增為兩段；理念改兩欄圖示與段落、手機單欄；歷程圖片放大至 140px 並補說明；團隊照片群 444px，補合作介紹。所有背景沿用現有內容，沒有新增年份、資歷或療效承諾。1440/768/390px 檢查通過，證據 output/visual-qa/about-expanded/report.json 與完整截圖；修正前 about-flow-final。預覽 /about-lienbang/?revision=expanded-story。正式 WordPress 未修改。

### 全站套用已確認的擴充圖文風格
使用者確認關於頁 expanded-story，要求每頁套用。新增 editorial-expanded-20261009.css，套用全部 31 個可操作內容頁及其 dist 副本（58 個 HTML 檔）：主視覺 520px、主要段落約 19px、主區塊標題約 40px、區塊留白 64px；首頁與服務卡片改桌面三欄、症狀列表三欄，保留手機雙欄／單欄適配。醫師原照 contain 避免裁切；脈診理念照片放大，療程流程與 FAQ 增加閱讀空間。沿用既有較完整醫療內容，沒有新增療效說法或刪除功能。關於頁已確認版保留。
八個主頁 1440/768/390px 共 24 組檢查通過，證據 output/visual-qa/sitewide-expanded-final；前一輪 sitewide-expanded。前後桌面／手機對照 /review/expanded/，較早的 /review/ 不代表最新實作。其餘子頁另執行 click-regression.cjs。第一次並行測試曾有 localhost 短暫拒絕連線，改單獨重跑完成後以 click-regression.json 為準。未修改正式 WordPress、不合併 main。
驗收完成：158 個內部連結實際點擊無 404；53 個其他本機頁（含 dist 與對照頁）390px 無水平溢出。tools/expanded-desktop-qa.cjs 另外對全部 31 個實際內容頁保存 1440px 截圖，無水平溢出，report 位於 output/visual-qa/sitewide-subpages/report.json。八主頁仍以完整圖片／選單／FAQ／H1 檢查為準，子頁桌面檢查僅代表溢出與截圖驗證，未宣稱所有子頁像素級還原。

### 全站頁首與頁尾放大及統一
依使用者要求，31 個內容頁與 dist 副本共 58 個 HTML 共用同一份頁首／頁尾結構與 shell-unified-20261009.css。桌面頁首固定 96px、Logo 240px、導航 16px；820px 以下頁首 76px、Logo 175px、選單展開位置同步修正。頁尾 Logo 260px，導航／段落 17px、電話 24px；桌面頁尾總高 372px、手機／平板 818px，格式與聯絡內容一致，依路徑標示 active。保留較窄桌面適配、手機 LINE 入口與 Escape 選單操作。
tools/shell-dimensions-qa.cjs 對 31 頁 × 1440/768/390px 共 93 組檢查：頁首／頁尾實際尺寸一致且無水平溢出，report 位於 output/visual-qa/shell-dimensions。第一輪發現捲軸寬度與繼承行高不同，已修正並重跑通過。八主頁完整截圖與互動驗證見 output/visual-qa/shell-unified-final。正式 WordPress 未修改。

## 2026-10-09 首頁六項治療服務同步
- 使用者改以治療服務頁六張卡片為首頁此區塊基準，授權更新首頁服務區。
- 首頁與 dist 首頁同步六張圖片、名稱、摘要及目的連結；卡片採相同圓角、裁切、字級、箭頭與桌機三欄／手機兩欄。
- 新增 assets/service-cards-unified.css 與 tools/service-sync-qa.cjs；未改動其他首頁區塊。
- 1440、768、390px 六項資料一致、無水平溢出，六個目的頁 HTTP 通過；截圖 output/visual-qa/service-sync/。
- 上一批全站視覺統一仍待最終報告與 Git 提交收尾，不能將此項通過等同全站已交付。

### 首頁治療服務標題整理
- 依使用者要求移除「探索你所需要的／調理方式」。
- 標題列改為左側「治療服務」、右側總覽連結，六張服務卡片維持同步樣式。
- service-sync-qa：1440／768／390px 通過，六項內容及目的連結一致、無水平溢出。

### 首頁三區對齊與服務箭頭移除
- 治療服務、醫師團隊、衛教文章採相同內容寬度與標題列格式，標題左邊線及總覽連結右邊線一致。
- 收起標題列的英文小標與輔助宣傳文字，保留 HTML 原文；服務卡片底部箭頭隱藏，整卡連結與鍵盤焦點保留。
- home-alignment-qa：1440、768、390px 對齊差小於 1px、箭頭不可見、無水平溢出；完整截图與 alignment.json 存於 output/visual-qa/service-sync/。

### 首頁全部圓圈箭頭移除
- 依要求移除首頁服務 6 張、醫師 3 張、衛教 4 張卡片的裝飾箭頭 HTML，共 13 個；保留所有卡片連結。
- 同步 dist 首頁。1440、768、390px 對齊／溢出檢查及六項服務一致性／目的頁測試通過。

### 首頁雙語標題恢復
- 恢復 OUR SERVICES、OUR DOCTORS、HEALTH ARTICLES，統一位於各中文標題上方。
- 使用共用兩列 Grid，英文與中文左邊線相同，右側總覽連結對齊中文標題。
- 1440、768、390px 三區標題及右側連結對齊、無溢出驗證通過；卡片箭頭仍移除。

### 頁首治療服務大型選單
- 共用展開選單放大至最大 1160px，採三欄兩列大型圖文卡片，圖片 140px、服務名稱 21px、摘要 15px；限制視窗高度並可捲動。
- 全站頁首六張選單圖片同步首頁六張服務圖；桌機與較窄桌機固定置中避免邊緣裁切。
- 1440／1024px 選單邊界、六張圖片一致與十二次真實點擊通過。截圖 output/visual-qa/service-sync/menu-*.png。手機保留既有導覽行為。

## 2026-10-09 六個治療服務內頁統一
- 新增 assets/service-unified-20261009.css，限定六個服務內頁；首頁不受此樣式影響。
- 六頁使用相同英文小標／中文標題／介紹／圖片／預約按鈕結構；桌機 520px 起主視覺，手機圖片置頂後接內容，修正脈診頁大片空白。
- 使用現有六張服務素材，未生成新照片；針刀原有示意圖移至原理解說區保留。美顏針、埋線新增既有素材主視覺。
- 統一章節導覽、流程卡片、FAQ 和綠色預約區，脈診新增內容錨點導覽。保留療程各自的評估、風險、流程等醫療資訊與 SEO 腳本。
- 六頁 1440／768／390px 共18組檢查通過：單一 H1、共用 Hero、預約入口、章節錨點、FAQ 切換與無水平溢出。
- 桌機手機完整截圖及報告：output/visual-qa/six-services-audit/；工具 tools/six-services-audit.cjs、six-services-validation.cjs。
- 「針刀／浮針」總覽入口仍以針刀為目的頁，浮針保留既有獨立 URL；未擅自改寫針刀頁的醫療範圍。頁面長度依內容保留差異。

### 治療服務總覽縮小
- 僅總覽頁：桌機主視覺最低高度440px、服務圖片190px、卡片標題22px／摘要17px，收斂間距與留白。
- 首頁與六個療程內頁維持原尺寸。1440／768／390px 六項卡片及無溢出檢查通過；截圖 service-sync/services-compact-*.png。

### 更正縮小目標：頁首展開選單
- 使用者澄清縮小的是首頁頁首展開選單，撤回總覽页 services-compact 樣式引用。
- 全站選單最大寬度1160→1000px、圖片140→115px、標題21→19px，仍為三欄兩列及首頁同圖。
- 1440／1024px 選單圖片、邊界與六個入口操作驗證通過。

## 2026-10-10 治療全路徑一致性複查
- 本機預覽已恢復。全站最新31頁×1440／768／390px共93組檢查通過，無失效內部連結／圖片、水平溢出、FAQ／手機選單或頁面執行錯誤。
- SEO、Schema及追蹤腳本屬性31頁未變更；完整文字逐字檢查因使用者授權首頁／選單摘要等修改而不同，保護摘要已據實記錄。
- 治療邏輯 audit：首頁／總覽／共用選單六張圖片一致；針灸頁交叉推薦的針刀、埋線、美顏針仍使用舊圖。浮針獨立頁尚未採用六頁共用Hero，需接續修正。
- 預約文案仍有「LINE 預約諮詢」「立即預約評估 (LINE)」「預約內科諮詢」差異；針刀／浮針合併入口仍須讓患者清楚理解兩者不同。
- 脈診頁內容長度較短，未提供流程及FAQ；保留現有醫療內容，尚未新增未經診所確認的醫療說明。
- 檢查資料 output/visual-qa/six-services-audit/logic-audit.json；全站前後視覺報告 /review/home-system/。
- 之前全站巡覽784次點擊通過；本次僅共用選單另測12次點擊，不能將舊巡覽聲稱為本次全量點擊。

## 2026-10-10 治療項目一致性修正完成
- 針灸頁針刀／美顏針／穴位埋線交叉推薦卡片更換為首頁同項目圖片；入口圖片一致性檢查通過。
- 浮針独立頁加入共用服務Hero、頂部LINE預約、既有流程／FAQ樣式，保留原醫療與SEO內容；使用現有浮針素材。
- 針刀與浮針頁新增雙療程切換，明確標示為不同療程。列表仍保留六項結構及原URL。
- 所有七個療程頁主要預約入口統一「LINE 預約諮詢」；卡片與選單「埋線」統一為「穴位埋線」。
- 七頁×1440／768／390px共21組驗證通過：主視覺、H1、預約、錨點、FAQ、水平溢出；catalog檢查圖片及所有療程預約文案一致。
- 脈診既有醫療內容較短，未為湊齊版型新增未確認的療程流程或醫療FAQ；這是保留的內容差異。
- 全站前後對照報告已產生 /review/home-system/，其中全站截圖為本次最後小修前的驗收基準；最新治療頁截圖另存 output/visual-qa/six-services-audit/。

## 2026-10-10 症狀頁照片與版型更新
- 沿用目前定製品牌格式，更新常見症狀總覽及16個症狀內頁，保留內科／體質、筋骨／針灸分類。
- 使用本次提供16張圖片，依症狀對應；新增1600／640px WebP與srcset，素材對應表 assets/symptoms-20261010/manifest.json。
- 總覽桌機四欄、平板與手機兩欄，照片16:9；內頁桌機文字／照片雙欄、手機照片置頂。同步首頁衛教與醫師推薦卡片的同症狀照片，dist鏡像一併更新。
- 評估、日常照護圖解保留；症狀圖片為使用者提供的情境示意，並非診所真實病例紀錄。
- 視覺循環紀錄：symptoms-after發現旧窄欄衝突；symptoms-final修正完整卡片寬度；symptoms-approved改善手機Hero並修正旧裝飾線寬度。各輪完整截圖保留 output/visual-qa/home-system/。
- 全站31頁×3尺寸93組檢查通過；最後症狀17頁×1440／768／390px再驗收51組，檢查H1、FAQ、手機導覽、圖片、水平溢出及內部連結。
- 31頁文字／SEO／Schema／原有連結保護檢查全數通過；未變更醫療資訊及正式WordPress。
- 17頁桌機／手機修改前後報告：/review/symptoms-refresh/；工具 tools/refresh-symptoms.py、symptoms-qa.cjs、build-symptoms-review.py。
- 保留差異：文章長度依原有醫療內容不同，診療圖解維持既有插畫；桌機總覽仍使用原定診療背景，手機採新肩頸情境照片。
