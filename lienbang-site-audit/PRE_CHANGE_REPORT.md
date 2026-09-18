# 連邦中醫網站變更前報告（公開層初檢）

- 網站：<https://lienbangtcm.tw/>
- 初檢日期：2026-07-24（Asia/Taipei）
- 狀態：**尚未修改網站**
- 安全閘門：**尚未取得主機、資料庫、WordPress、GSC、GA4、GTM 權限；尚未完成完整備份與還原演練**

## 1. 目前可確認的技術狀態

以下版本與元件來自公開頁面產生器標記或實際載入資源，仍須在後台核對：

| 項目 | 公開層觀察 |
|---|---|
| WordPress | 6.7.1 |
| 主題 | Astra 4.8.11、Astra Addon 4.8.12 |
| 頁面編輯器 | Elementor 3.27.6、Elementor Pro 3.27.4 |
| SEO | All in One SEO Pro 4.7.9 |
| 電商 | WooCommerce 9.6.1 |
| 其他已見資源 | YayPricing Pro、WPForms、Amelia、Ultimate Addons for Elementor、Header Footer Elementor |
| 分析 | 直接載入 GA4 `G-ZY5FT1B8DC`，並載入 `GTM-WVSPRVNK` |
| CDN／監測 | Cloudflare Insights |

後台尚待確認：

- 已確認目前只有 Astra（後台顯示名稱：Metabiz THEME）為啟用主題，未安裝 Astra 子主題。
- 是否有 MU plugins、主機注入程式或自訂 `functions.php`；Code Snippets 已安裝但目前停用。
- PHP、資料庫、Web Server、CDN、快取與圖片最佳化設定。
- 現有備份、staging、排程與主機層還原方式。
- GA4 是否由 GTM 再次送出相同 `page_view`。

### 後台確認的主要啟用外掛

- All in One SEO Pro、Local Business、Redirects
- All-in-One WP Migration
- Amelia
- Elementor、Elementor Pro
- Polylang、Connect Polylang for Elementor
- WooCommerce、ECPay Ecommerce、MYPay、Metabiz ECPay Logistic
- YayMail、YayPricing Pro
- WPForms、WP Mail SMTP
- Ultimate Addons for Elementor、Header Footer Elementor
- Redis Object Cache、Metabiz Cache Flush
- WP All Import Pro、WP All Export Pro
- All In One Login、Activity Log、Disable XML-RPC-API

完整外掛清單非常龐大，包含大量停用的購物、金流、聯盟、表單與範本外掛；正式清理前須由完整檔案備份與還原演練保護。

### 2026-07-24 備份嘗試紀錄

- All-in-One WP Migration 的 Backups 頁面原先顯示 `0` 份備份。
- 已成功執行一次完整匯出封裝；外掛完成資料庫、內容、1,627個媒體檔與147,213個外掛檔案的封裝，完成畫面顯示備份大小約6GB。
- 外掛產生的下載網址使用 `twyuting10210314859.admin.metabiz.tw` 管理別名，下載時被導向404。
- 改以正式網域存取同一路徑也回傳404；返回Backups頁後仍顯示「No backups found」。
- 因伺服器備份未保留、站外副本未下載且沒有校驗碼，這次匯出**不算有效備份**。
- 已進行第二次完整匯出，並保持匯出完成視窗開啟；同樣成功產生約6GB的 `.wpress` 檔案。
- 第二次分別測試管理網域連結、正式網域相同檔案路徑、瀏覽器下載事件及受控媒體下載；管理網域與正式網域均回傳404，Downloads及瀏覽器暫存區均未產生 `.wpress` 副本。
- 第二次測試證實問題位於主機對 `wp-content/ai1wm-backups` 的檔案公開／保存機制，而非外掛封裝程序。
- 下一步必須使用主機控制面板的檔案／資料庫快照或由主機商修正All-in-One WP Migration下載路徑，再完成站外副本與還原演練。

## 2. 首頁與全站共用介面

### 已確認

- 首頁只有一個 H1：「連邦中醫診所」。
- canonical 為 `https://lienbangtcm.tw/`。
- 頁首仍有 `/my-account/` 帳號入口。
- 主選單仍使用「關於我們」「連邦特色」「醫師介紹」「聯絡我們客戶服務」等舊命名。
- LINE、電話及Google地圖目的網址目前分別為：
  - `https://lin.ee/UWWKmse`
  - `tel:0225795059`
  - `https://maps.app.goo.gl/k4yUg13gzQFgrujW9`
- 首屏按鈕仍顯示「查看院所資訊」，尚未改為「查看門診時間與交通」。
- 首圖為 1672×941 PNG，已設 `fetchpriority="high"` 且未 lazy load，但沒有 `srcset`。
- 多張內容圖仍為PNG且沒有響應式 `srcset`。
- 公開首頁仍載入 WooCommerce、YayPricing、商店樣式及多個電商腳本。
- OG圖片目前使用白色Logo，需確認社群分享時的可讀性與尺寸。

### 結構化資料問題

- 首頁輸出 `LocalBusiness`，不是更明確的 `MedicalClinic`。
- 名稱目前為「連邦中醫」，應與正式名稱「連邦中醫診所」核對一致。
- `openingHoursSpecification` 目前錯誤輸出週一至週日皆為 09:00–17:00。
- 正確門診時間確認前，不能沿用或推測營業時間。

## 3. 醫師頁

### `/team/`

- title：「醫師團隊 - 連邦中醫」。
- meta description 為頁面文字的機械截斷，內容不完整。
- 有單一H1「醫師團隊」。
- 張豫與戴宣元醫師卡片欄位不一致。
- 張豫醫師連到 `/profile/`；戴宣元醫師連到 `/dai-xuan-yuan/`。
- 沒有 `Person` 醫師結構化資料。

### `/profile/`

- title：「個人醫師詳細頁 - 連邦中醫」。
- H1只有「中醫師/院長」，沒有以醫師姓名作為主標題。
- canonical為 `/profile/`。
- 沒有 `Person` 結構化資料。
- 規劃建立 `/zhang-yu/`，待正式資料完成後將 `/profile/` 301至新頁。

### `/dai-xuan-yuan/`

- title為「戴宣元醫師 - 連邦中醫」。
- H1只有「中醫師」，沒有姓名。
- description為截斷頁面文字。
- 沒有 `Person` 結構化資料。

### 待診所提供

- 正式姓名與職稱寫法。
- 正式醫師照片及使用授權。
- 經確認的診療方向、學經歷及門診時段。
- 是否有醫師個人官方社群／專業頁可列為 `sameAs`。

使用者已於2026-07-24指示：醫師頁優先使用現有網站公開資料。現有資料的逐欄盤點見 `DOCTOR_CONTENT_INVENTORY.md`；現站缺少的學經歷及戴宣元醫師門診時段不得自行補寫。

使用者另確認：網站可顯示最新提供的固定醫師時段，但實際排班仍以官方LINE每月公告為準。張豫醫師為週一至週三下午／晚上、週四上午、週日上午；戴宣元醫師為週四下午／晚上。張豫醫師於2026-08-21至2026-10-27休診。新版頁面保留「查看本月門診表（LINE）」按鈕；未取得可長期維護的診所整體營業時間前，不輸出診所層級的 `openingHoursSpecification`。

張豫醫師的學歷、現任／曾任經歷、「臨床脈學學會創辦人」身分及Instagram、Threads、Facebook官方社群已由使用者提供，列入可用內容。公開搜尋未找到能可靠核對的獨立個人網站，因此暫不新增個人網站連結。

戴宣元醫師的履歷PDF已完成視覺核對。可公開使用的資料包括長庚大學中醫學系、長庚醫院中醫部實習醫師、龜山及青溪風澤中醫診所主治醫師、五股大順中醫診所院長等學經歷。私人聯絡方式、出生日期、身高體重不納入網站；履歷中的效果保證文字亦不沿用。

## 4. 聯絡與院所資訊頁

### `/support/`

- title仍為「客戶服務 - 連邦中醫」。
- description為頁面文字截斷。
- 存在重複「客服中心／回饋表單／聯絡表單／常見問題」區塊。
- 有兩份重複表單。
- 內文出現錯誤信箱 `lienbang.tcm@gamil.com`。
- 未見完整地址、Google地圖、捷運小巨蛋站5號出口與結構化門診資訊的整合呈現。
- 下列文字具有醫療廣告或正確性風險，應移除或改寫：
  - 「急性病療程大約7-14天可以解決」
  - 「用自費才能讓患者用到最好的藥物」
  - 「在中醫師正確的診斷下一定會讓身體邁向正軌」
  - 「停藥停針後馬上緩解，不會殘留」

## 5. 舊購物與範本頁

下列頁面目前仍可公開開啟，具有自我canonical，robots只顯示 `max-image-preview:large`，未退出索引：

| URL | 目前標題／H1 | 初步問題 |
|---|---|---|
| `/shop/` | 商店 | 舊商店頁仍公開 |
| `/shop-2/` | Shop／大事即將發生 | 商品封存頁仍公開 |
| `/cart/` | 購物車 | 交易頁可索引 |
| `/checkout/` | 結帳 | 交易頁可索引 |
| `/my-account/` | 我的帳號 | 會員登入頁可索引 |
| `/collections/` | Collections | 舊購物範本 |
| `/new-arrivals/` | New Arrivals | 舊購物範本 |
| `/sample-page/` | 範例頁面 | WordPress範例頁 |
| `/home/` | Home／Party Wears | 服飾商店範本 |
| `/home-2/` | 首頁／調理體質，從根本改善身體循環 | 舊版首頁及高風險文字 |
| `/about/` | About | 舊英文範本 |
| `/contact/` | Contact | 舊英文範本 |

隨機不存在網址目前顯示正確404版面、沒有canonical，並輸出 `noindex`；實際HTTP狀態碼仍須用爬蟲或命令列驗證。

## 6. 預定修改面

在備份與還原驗證完成、且診所確認本報告後，staging預計修改：

- Astra頁首／主選單／手機選單及帳號圖示設定。
- 首頁、`/team/`、`/support/`、`/dai-xuan-yuan/`，並新增 `/zhang-yu/`。
- AIOSEO的title、description、canonical、OG、Schema、索引與Sitemap設定。
- WooCommerce前台入口、商品索引、商品Sitemap及非商店頁資源載入。
- 重新導向／410規則。
- 首圖與主要圖片衍生檔、`srcset`、preload及lazy-load策略。
- GTM點擊觸發條件；保留容器ID與既有事件名稱。
- 子主題或Code Snippets中的全站CSS／PHP／JS；實際檔案需在後台盤點後列明。

## 7. 目前阻擋條件

執行下一階段前必須取得：

1. 主機面板或SSH/SFTP、資料庫及WordPress管理員登入。
2. staging子網域／DNS／SSL及密碼保護建立權限。
3. GSC、GA4、GTM存取權。
4. 正確門診時間。
5. 醫師照片、學經歷、診療方向及門診時段。

在以上條件到位前，不得修改正式站，也不能宣稱已完成備份、還原演練、GTM DebugView或Search Console判讀。
