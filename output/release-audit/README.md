# 預覽驗證紀錄

2026-09-08 執行。這是發布前準備資料，並非正式站已發布證明。

- image-manifest.csv：27 頁中 img 與 srcset 的圖片對照，共 40 筆頁面／來源配對。
- remote-checks.json：19 個不同遠端圖片來源皆 HTTP 200 且 Content-Type 為 image/*；另含兩個 LINE 短網址的唯讀轉址查核。
- 兩個 LINE 短網址均指向 @076icjzg。
- 本機圖檔存在已由 tmp/check_site_preview.py 驗證。
- layout-checks.json：27 頁 × 390px／1440px 的瀏覽器尺寸與圖片載入檢查，未發現水平溢出。
- image-render-recheck.json：針對前份紀錄中胃食道逆流與失眠延遲載入圖片的 4 個組合，等待解碼後複查通過；原紀錄的未載入回報不代表圖片失效。
- PNG 為首頁、症狀總覽、失眠、咳嗽的桌面／手機截圖。自動尺寸檢查不等於完整視覺或醫療內容審閱。
- 重跑查核：使用 Python 執行 tmp/audit_preview_assets.py。需有公開網路讀取權限；失敗結果必須區分網路限制與實際 HTTP 錯誤。

整站預覽 ZIP 只供保留及本機審閱。解壓後以 HTTP 靜態伺服器開啟 site-preview 資料夾；不可直接將 ZIP 匯入 WordPress 或覆蓋正式站。預覽含 noindex、禁止索引的 robots.txt 與本機路徑。
