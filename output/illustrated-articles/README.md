# 每篇三張配圖的症狀文章

本資料夾為文章與圖片交付來源；16 篇文章已全部完成，每篇三張內文配圖，共 48 張。製作紀錄見 ../article-images-install-status.json。

每篇各有一個 HTML 與 images 資料夾，包含三張配圖的 WebP／JPEG 版本。兩種格式是同一張圖，不代表六張不同圖片。胃食道逆流、失眠使用既有的三張內文圖；原開頭大圖不再放入內文，原圖檔仍保留在原始資料夾。

新配圖使用內建 image_gen 製作，完整提示詞與配置在 ../article-images-three-plan.json。各圖有圖說、替代文字、尺寸與延遲載入設定，表示一般情境，不代表真實患者或實際診療紀錄。

開啟本機預覽：http://127.0.0.1:8765/symptoms/

正式上傳時先將每篇 images 內需要的格式上傳媒體庫，再依實際公開網址替換 HTML 的 src/srcset。若僅上傳 JPEG，移除 picture 內未上傳的 WebP source。HTML 已內嵌共用樣式；放入 WordPress／Elementor 時仍需在實際主題中檢查樣式作用範圍與單一 H1。正式網址、canonical 及 Sitemap 依原發布流程確認。

此資料夾與 ZIP 不是 WordPress 自動匯入套件；本次只更新本機預覽，未發布正式站。
