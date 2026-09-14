# global-population-dashboard
# Global Population & Geopolitical Risk Dashboard

## 📌 專案簡介!
本專案為 Department of FinTech / AI Applications 進階作業，旨在結合 Python 數據統計處理與前端網頁開發，呈現全球人口趨勢與伊朗地緣政治風險評估。


---

## 🤖 AI 使用聲明 (AI Usage Declaration)
本專案在開發過程中輔助使用了大型語言模型 (ChatGPT / Claude / Gemini)：
* **程式碼生成**：輔助撰寫 `clean.py` 中的 CAGR 統計邏輯與響應式 CSS 網頁佈局。
* **文獻彙整**：協助整理中東地緣政治風險因子與事實資料分類。

### Prompt 範例
> "請提供一個 Python 函式，讀取字典格式的人口數據，並計算出 2024 至 2100 年的平均值、總成長率與 CAGR（複合年均成長率），最後將結果輸出為 cleaned.json。"

---

## 🔍 資料驗證與防幻覺流程

### 1. 人口數據驗證
* **數據來源**：引用 **UN World Population Prospects (2024 Revision)** 中位數預測。
* **AI 數字差異處理**：當不同 AI 給出微幅不同的預估值時，統一以聯合國 (UN) 官方報告的標準數據為準，排除 AI 自行推算的變異。

### 2. 地緣政治防幻覺（事實與推論分離）
在中東地緣政治風險矩陣 (Iran Risk Matrix) 中，嚴格區分數據屬性：
* **事實資料**：必須附帶權威機構（如 EIA 海峽運量數據、IAEA 核監測報告）之數據背書[cite: 1]。
* **推論分析**：對於未發生的區域局勢與供應鏈衝擊，一律標示為「推論」，避免將 LLM 的預測當作確定事實[cite: 1]。

---

## 📁 專案檔案結構
* `index.html` - 網站首頁與 Dashbaord 內容[cite: 1]
* `style.css` - 網站樣式表 (具備 RWD 響應式設計)[cite: 1]
* `scripts/clean.py` - Python 資料處理腳本[cite: 1]
* `data/raw.txt` - 原始人口數據[cite: 1]
* `data/cleaned.json` - Python 計算後輸出的 JSON 分析檔[cite: 1]
* `report.pdf` - 一頁式 PDF 分析報告[cite: 1]
