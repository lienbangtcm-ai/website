# 治療服務完整重構

## 最新插畫確認版 v4

- 以已確認的把脈、單味藥、美顏針三款樣稿為基準，更新全部 10 款服務插畫；生活照護、活動評估、一般針灸、整合物理治療、針刀、浮針、穴位埋線均已重畫。
- 已同步 output/services-page.html 與 output/site-preview/services/index.html。就診流程與初診準備仍保留既有小型功能圖示。
- 完整放大對照頁：/services/illustration-collection.html；個別向量檔：icons-v4/；插畫來源：tmp/clinic_illustrations_v4.py。
- 1440、1280、768、390px 版面檢查通過；10 張服務插畫、16 個症狀連結、單一 H1，無水平溢出。
- 僅本機確認稿，未上傳正式站；既有 ZIP 尚未重新打包，請以目前預覽為準。

僅本機預覽，正式站未更新。預覽路徑 /services/。

- 舊頁備份：services-before.html。移除舊 lbsv-*、sv-card、sv-grid、重複 media rules、漸層、陰影、浮動 CTA 與頁尾重複症狀索引。
- 新頁採 lb-services 命名空間，services.css 為唯一頁面樣式來源；頁首沿用共用品牌樣式。
- 依 2026-09-11 審閱意見改為無 AI 圖片版本：暖白 Hero、細線導覽、低彩度編輯插畫服務選項、症狀文字索引、整合物理治療段落、初診清單與單一主要 CTA。
- Design tokens：--lb-bg、--lb-bg-soft、--lb-text、--lb-muted、--lb-brand、--lb-accent、--lb-line、--lb-container、--lb-section-space、--lb-radius。
- 桌面容器 1240px、主要段落留白 140px；平板 100px，手機 76px。手機重排流程數字與文字、單行症狀連結、圖片優先、全寬 CTA。
- 原有內部目的連結保留，16 個症狀連結改為文字索引；保留單一 H1 與 ItemList schema。
- 中醫內科、針灸傷科與自費診療共 10 個選項，全部改用手工彩色向量插畫；插畫保留人物、手部、脈枕、藥材、生活照護、關節活動、針具、皮膚層次與身體部位等辨識細節，不使用 AI 圖片。
- 1440、1280、768、390px 檢查：無橫向溢出、1 個 H1、主內容 0 張圖片、10 個服務 SVG、16 個症狀連結。結果見 line-art-browser-check.json。
- 生成入口 tmp/build_services_editorial.py；圖片安裝 tmp/install_services_images.py。output/services-page.html 已同步為新版本。
- 目前僅供使用者確認，未上傳或變更正式站；ZIP 為預覽包，不能直接覆蓋 WordPress。
