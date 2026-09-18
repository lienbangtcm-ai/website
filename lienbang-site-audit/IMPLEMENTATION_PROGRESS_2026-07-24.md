# 連邦中醫網站實作進度（更新至 2026-07-26）

## 已完成並已在正式前台驗證

- 首頁首屏：
  - 加入「台北松山・小巨蛋站附近」定位。
  - 服務層級改為「中醫內科與體質調理」及「疼痛、筋膜與活動功能」。
  - CTA 統一為 LINE 預約、電話預約、查看門診時間與交通。
  - 電話統一使用 `tel:0225795059`。
  - LINE 使用 `https://lin.ee/UWWKmse`。
  - Google 地圖使用 `https://maps.app.goo.gl/k4yUg13gzQFgrujW9`。
  - 首圖保留 `fetchpriority="high"`，未設 lazy load。
  - 加入手機版溢出防護、按鈕尺寸及 `safe-area-inset-bottom`。
- 主選單：
  - 關於我們 → 門診資訊。
  - 連邦特色 → 診療特色。
  - 醫師介紹 → 醫師團隊。
  - LINE預約掛號 → LINE預約。
  - 聯絡我們客戶服務 → 交通資訊。
  - 門診資訊連到 `/support/#clinic-hours`。
- Astra 頁首：
  - 帳號／`my-account` 圖示已在桌機、平板及手機隱藏。
- 醫師團隊 `/team/`：
  - 重建公開版醫師卡片與行動按鈕。
  - 加入張豫、戴宣元醫師正式照片、已確認學經歷、診療方向及固定門診。
  - 加入張豫醫師 2026/8/21–2026/10/27 休診提示。
  - 移除「埋線減重」等舊版呈現，改為中性描述。
  - 修正 AIOSEO title 與 meta description。
- 院所資訊 `/support/`：
  - 頁面名稱由「客戶服務」改為「門診與交通資訊」。
  - 移除公開前台的購物式客服中心、兩份重複表單、錯誤信箱及高風險療效 FAQ。
  - 加入地址、電話、LINE、Google 地圖、小巨蛋站 5 號出口、固定醫師門診及臨時休診提示。
  - 加入 LINE／電話／導航三個主要按鈕。
  - 修正 AIOSEO title 與 meta description。
- 草稿：
  - 已建立張豫醫師新版草稿，WordPress ID `4285`，網址代稱 `zhang-yu`。
  - 草稿含正式照片、診療方向、學經歷、門診、休診期間、官方社群及 SEO title／description。
  - 已建立戴宣元醫師新版草稿，WordPress ID `4288`，網址代稱 `dai-xuan-yuan-new`。
  - 戴醫師草稿含正式照片、已確認學經歷、診療方向、週四午晚診、LINE／電話及 SEO title／description。
  - 已建立「新醫師頁範本（資料待補）」草稿，WordPress ID `4290`，網址代稱 `new-doctor-template`；未知姓名、照片、學經歷、診療方向及門診均明確標示待補。
- 公開連結保護：
  - 首頁張豫醫師連結暫時改回 `/profile/`。
  - 因 `/team/` 仍連到未發布的 `/zhang-yu/`，已新增單一可逆 301：`/zhang-yu/` → `/profile/`；新版醫師頁核准發布後應移除此暫時轉址。
- AIOSEO Sitemap／索引：
  - Sitemap 只保留文章、頁面及一般文章分類。
  - 已排除商品、附件、Landing Pages、Floating Elements、Elementor Header & Footer Builder。
  - 已排除商品分類、商品標籤、商品品牌、商品屬性及 language 系統分類。
  - 商品與上述範本內容類型已設為 `noindex`；商品相關分類與 language 系統分類亦已設為 `noindex`。
  - 公開 `sitemap.xml` 已驗證不再列出 `product-sitemap.xml`、`product_cat-sitemap.xml` 或 `language-sitemap.xml`。
  - 直接開啟 `product-sitemap.xml` 與 `product_cat-sitemap.xml` 目前皆為空的 `urlset`。
  - 已將下列明確舊頁加入 AIOSEO Sitemap 個別排除清單：
    - `/cart/`（ID 27）
    - `/checkout/`（ID 28）
    - `/my-account/`（ID 29）
    - `/sample-page/`（ID 2）
    - `/home/`（ID 15）
    - `/home-2/`（ID 2042）
    - `/shop/`（ID 26）
    - `/shop-2/`（ID 11）
    - `/collections/`（ID 541）
    - `/new-arrivals/`（ID 677）
  - `/sample-page/`、`/cart/`、`/checkout/`、`/my-account/` 已另外設定頁面層級 `noindex`；公開 HTML 均已驗證含 `noindex`。
  - `/home/`、`/home-2/`、`/shop/`、`/shop-2/`、`/collections/`、`/new-arrivals/` 亦已完成頁面層級 `noindex`；以上 10 個網址均已從公開 HTML 驗證。
  - 2026-07-26 公開 Sitemap 索引只剩 `post-sitemap.xml`、`page-sitemap.xml`、`category-sitemap.xml`。
  - 2026-07-26 公開 `page-sitemap.xml` 已確認不含上述 10 個明確舊頁。
- 結構化資料：
  - 已關閉 AIOSEO 未確認的營業時間輸出。
  - 清除 Redis 後，公開首頁已確認不再輸出錯誤的週一至週日 `09:00–17:00` `openingHoursSpecification`。
  - AIOSEO Local SEO 已補入已確認資料：連邦中醫診所、南京東路四段69號1樓、105、松山區、臺北市、Taiwan、+886 2-2579-5059。
  - AIOSEO 此版本的 Local SEO 類型選單搜尋不到 `MedicalClinic` 或 Medical 類型，因此保留原 LocalBusiness，並以 AIOSEO Custom Schema 補上相同 `@id` 的 `MedicalClinic` 節點。
  - 公開首頁已驗證 `MedicalClinic` 含名稱、網址、電話、地址與 Google 地圖，且未輸出尚未確認的營業時間。
  - 張豫醫師草稿已加入並驗證 `Person`：姓名、職稱、照片、`worksFor`、學校、診療方向與已提供的官方社群。
  - 戴宣元醫師草稿已加入並驗證 `Person`：姓名、職稱、照片、`worksFor`、學校與診療方向。
  - 新醫師範本因姓名、照片、學經歷、診療方向與時段未提供，未建立推測性 Person Schema。
- 追蹤與行動連結：
  - 公開首頁、`/team/`、`/support/` 均已驗證保留 LINE、`tel:0225795059` 與 Google 地圖目的網址。
  - 主要 CTA 保留 `data-conversion="line|phone|map"` 與位置標記。
  - 公開首頁只偵測到 `GTM-WVSPRVNK`，未發現額外直接載入的 `gtag.js`。

## 響應式驗證

- 已測試首頁、醫師團隊、院所資訊：
  - 360×800
  - 390×844
  - 430×932
- 首頁三個尺寸均未發現水平溢出。
- `/team/` 與 `/support/` 回歸測試曾偵測到舊 Elementor `100vw` 容器造成約 8px 溢出；已加入僅限 page ID 2065、2069 的防溢出及全寬容器修正 CSS。
- 首屏主要 LINE／電話／門診交通按鈕未重疊。
- 手機固定電話／LINE 列正常顯示，並保留 safe-area 空間。
- `/team/` 與 `/support/` 的舊 Elementor 標題已由 H1 改為 H2；公開 DOM 已驗證每頁僅一個 H1。
- 網站 Logo 已驗證 alt 為「連邦中醫」。
- 頁尾部分純文字電話／資訊連結點擊高度小於 44px；主要 LINE／電話／導航 CTA 均為 48px 以上。

## 截圖

- `screenshots/after-home-mobile-390.png`
- `screenshots/after-team-mobile-390.png`
- `screenshots/after-support-mobile-390.png`
- `screenshots/after-home-desktop-1366.png`
- `screenshots/after-team-desktop-1366.png`
- `screenshots/after-support-desktop-1366.png`
- `screenshots/final-home-mobile-390.png`
- `screenshots/final-team-mobile-390.png`
- `screenshots/final-support-mobile-390.png`

## 尚未完成

- `/about/`、`/contact/` 仍在頁面 Sitemap；因缺少 GSC／GA4／外鏈資料，尚未直接 301、410 或 noindex。
- `page-sitemap.xml` 仍會從 `/team/`、`/support/` 及舊醫師頁解析到部分隱藏舊 Elementor 圖片及管理網域圖片；完全清除需刪除舊 Elementor 容器或做 Sitemap 圖片層級處理。
- 新版張豫、戴宣元醫師頁仍為草稿；未經確認不發布。`/zhang-yu/` 暫時 301 至 `/profile/`。
- GTM Preview／GA4 DebugView 的事件去重驗證。
- GSC 外部連結與流量資料取得前，不做批次 301／410。
- WooCommerce 停用、資料庫、DNS、GA4、GTM 變更均未執行。
- 完整 Lighthouse／PageSpeed 修改前後比較尚未完成。

## 目前阻擋

無 WordPress 登入阻擋。需由使用者補充／確認診所整體營業時間、新醫師資料，並提供 GSC、GA4、GTM 權限後，才能安全完成逐網址處置、事件 DebugView 與可歸因的修改前後效能比較。
