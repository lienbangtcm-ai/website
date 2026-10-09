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
