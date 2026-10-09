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
