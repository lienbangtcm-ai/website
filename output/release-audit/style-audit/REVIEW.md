# 本機網站風格審視

範圍：27 個 index.html 頁面，1440px／390px 共 54 次檢查。未修改網站。
基準：已核准常見症狀與治療服務的暖米白、暖棕、柔和彩色插圖；首頁實景照片方向。
限制：檢查時主動阻擋外部 HTTPS 圖片，遠端照片及 Logo 的空白不可判定為正式站故障。正式網站外連頁尚未視覺審核。截圖拼頁只呈現各頁上段，另有逐頁完整桌機截圖與手機首屏。

## 優先問題

1. 四個自費頁的相對 shared-selfpay.css 檔案不存在於各自預覽目錄；原始檔位於 output/selfpay-content/shared-selfpay.css。目前僅有部分共用樣式生效，出現無排版的清單、預設藍色連結及異常寬度。先修載入，再統一視覺，不應直接重寫內容。
2. 中醫內科、針灸、整合治療與關於頁仍是舊深咖啡大型橫幅；H1 無襯線 66–76px，與新頁襯線 48–56px 差異明顯。
3. 全站頂部 LINE 按鈕實測圓角：首頁／症狀文章 5px，治療服務 0px，其餘多頁 999px。共享導覽被各頁 CSS 覆蓋，須統一規則。
4. 首頁三個治療服務入口仍是舊 SVG；治療服務內已使用新提供的點陣插畫，需換成同一組素材。
5. 常見症狀原圖裁切含底色，部分卡片內仍可見圖片矩形邊界；屬後續精修，不應重新生成角色。
6. 症狀文章已大致統一為米白／暖棕；胃食道逆流和失眠的內容編排與其他文章不同。依先前約定保留文章文字和原圖片，只調整版面框架、間距、目錄及 CTA。

## 全部頁面清單

| 頁面 | 評估與順序 |
| --- | --- |
| /針刀/ | P0 樣式載入缺失，第一批 |
| /浮針/ | P0 樣式載入缺失，第一批 |
| /美顏針/ | P0 樣式載入缺失，第一批 |
| /埋線/ | P0 樣式載入缺失，第一批 |
| /pulse-diagnosis/ | P1 深色大首屏、粗體字、部分預設藍色文字連結 |
| /acupuncture/ | P1 舊照片式首屏與粗體標題，需銜接新服務分類頁 |
| /acupuncture-physical-therapy/ | P1 深咖啡首屏、金色標題、舊式 CTA |
| /about-lienbang/ | P1 深色大首屏及較重照片框；可延續實景照片與新排版 |
| / | P2 新方向已成立，三個服務入口仍為舊插圖；浮動 CTA 較厚重 |
| /services/ | 基準頁；頂部 LINE 按鈕圓角與其他頁不同 |
| /symptoms/ | 基準頁；裁切素材底色邊界待精修 |
| /symptoms/gerd/ | P3 米白基調一致，頁首品牌字、內容分欄與其他文章不同 |
| /symptoms/insomnia/ | P3 基調一致，前段偏純文字，保持內容不變調整節奏 |
| /symptoms/allergic-rhinitis/ | P3 共用文章框架已統一，檢查目錄和 CTA 細節 |
| /symptoms/constipation/ | P3 同上 |
| /symptoms/cough/ | P3 同上 |
| /symptoms/de-quervain/ | P3 同上 |
| /symptoms/diarrhea/ | P3 同上 |
| /symptoms/fatigue/ | P3 同上 |
| /symptoms/frozen-shoulder/ | P3 同上 |
| /symptoms/knee-pain/ | P3 同上 |
| /symptoms/low-back-pain/ | P3 同上 |
| /symptoms/menstrual-pain/ | P3 同上 |
| /symptoms/neck-shoulder-pain/ | P3 同上 |
| /symptoms/plantar-heel-pain/ | P3 同上 |
| /symptoms/sciatica/ | P3 同上 |
| /symptoms/tennis-elbow/ | P3 同上 |

## 下一步

先修四個自費頁 → 統一全站共用導覽與按鈕 → 三個治療介紹頁 → 關於連邦 → 首頁殘留舊插圖 → 16 篇症狀文章版面細節 → 正式站外連頁。

醫師團隊、健康專欄、門診與交通目前為正式站外連，不在上述 27 個本機頁面中。全數 54 次檢查未發現水平溢出，但不代表所有互動、連結、遠端圖片或正式站功能皆完成驗證。
