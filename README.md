# 🚀 學校備課與行政自動化專案標準範本 (Project Starter Template)

本倉庫為新北市國小教師備課、學校行政自動化、GAS 系統與各類專案的**通用標準起手架構**。
內建 Antigravity、Claude Code、Gemini CLI 等 AI 助手的全域規範、防呆機制與 5 大標準管理文件。

---

## 🌟 如何開始使用？（三種超簡易方式）

### 方式 A（最神速！在 Antigravity 直接貼上網址）
在電腦建立任意空白資料夾，用 **Antigravity** 開啟該資料夾，並在對話框直接貼上：
> 💬 **「請參考此 GitHub 範本初始化我的專案：https://github.com/wukolo1206/project-starter-template」**

Antigravity 會自動讀取規範、詢問專案名稱與類型，1 秒鐘為您自動建置好專屬的 5 大標準檔案！

---

### 方式 B（執行一鍵智慧設定總選單：setup.py）🌟 最推薦！
在專案根目錄下執行：
```bash
python setup.py
```
系統會自動跳出互動選單，讓您自由選擇：
```text
  [1] 📋 專案標準環境初始化（自動生成 5 大標準管理文件）
  [2] 🔐 設定 Google 試算表與 OAuth 授權（引導生成 token.json）
  [3] 📦 安裝全域常用 Skills（using-superpowers + Office + 視覺設計）
  [4] 🌟 全套一鍵大滿貫（[1] + [2] + [3] 一次全自動完成）
  [5] 📖 開啟說明文件手冊
  [0] 🚪 離開
```

---

### 方式 C（標準 GitHub 範本法：Use this template）
1. 點擊本頁右上角綠色的 **「Use this template」➔「Create a new repository」**。
2. 輸入您的新專案名稱並建立倉庫。
3. Clone 至本機並以 **Antigravity** 開啟資料夾即可直接開工！

---

## 📁 專案標準文件結構

```text
專案根目錄/
├── .agents/                 # Antigravity 專屬工作區技能與客製化配置
├── skills_pack/             # 📦 內建常用 Skills 離線安裝包（含 13 個精選技能）
├── setup.py                 # 🌟 智慧設定總入口選單（初始化 / Google 授權 / Skills 安裝）
├── init_project.py          # 📋 專案 5 大標準管理檔案初始化腳本
├── setup_google_auth.py     # 🔐 Google 憑證與授權一鍵引導精靈
├── install_skills.py        # 📦 常用 Skills 全域與專案安裝器
├── GOOGLE_AUTH_GUIDE.md     # 📖 Google OAuth 圖文逐步設定指南
├── AGENTS.md                # 全域 AI 規範（現況檔優先、自動備份、來源追溯）
├── CLAUDE.md                # 專案憲法（YAML 元資料、技術架構、不能動的地方、驗收清單）
├── CHANGELOG.md             # 版本歷程記錄
├── PITFALLS.md              # 避坑指南（已知風險與踩坑解法庫）
├── DECISIONS.md             # 重大架構決策紀錄
├── handoff.md               # Session 結束工作交接紀錄
└── .gitignore               # 預設忽略暫存與憑證檔案
```

---

## 📦 內建常用 Skills 清單（智慧偵測 AI Agent 目標路徑）

執行 `python setup.py` 選擇 `[3]` 或直接執行 `python install_skills.py`，系統會**自動智慧偵測當前運行的 AI Agent**（Antigravity / Claude Code / Gemini CLI），並自動鎖定最佳的全域路徑與專案路徑進行部署，無需手動選擇：

| 類別 | 技能名稱 | 核心功能與說明 |
| :--- | :--- | :--- |
| 👑 **核心大腦** | **`using-superpowers`** | 強制 AI 先檢查並精準調用專屬 Skill，提升執行嚴謹度 |
| 📑 **Office 辦公** | **`docx`** | Word 文件（.docx）深度排版、表格處理與列印級生成 |
| 📑 **Office 辦公** | **`xlsx`** | Excel 試算表（.xlsx）資料分析、統計、公式與格式化 |
| 📑 **Office 辦公** | **`pdf`** | PDF 公文與教冊深度文字抽取、表格解析與合併分割 |
| 📑 **Office 辦公** | **`pptx`** | PowerPoint 簡報生成、教學投影片編排與重點摘要 |
| 🎨 **視覺互動** | **`canvas-design`** | 宣傳海報、班級公約、活動傳單美編設計（PNG/PDF） |
| 🎨 **視覺互動** | **`frontend-design`** | 互動式教學網頁、計時器、班級抽籤輪盤、HTML 元件 |
| 🎨 **視覺互動** | **`algorithmic-art`** | p5.js 數學圖形、碎形幾何與程式美學互動生成 |
| 🎨 **視覺互動** | **`theme-factory`** | 文件與網頁設計主題樣式庫（10 組配色與字型主題） |
| 🎒 **教學行政** | **`chinese-quiz-generator`** | 國語科標準考題產生器（南一/康軒/翰林 1~6 年級命題規範） |
| 🎒 **教學行政** | **`teacher-meeting-organizer`** | 教師會議深度整理、方案 A 累加至 Google 試算表總表 |
| 🎒 **教學行政** | **`teacher-meeting-auditor`** | 會議時程防呆審核（場地撞期、同日負擔、法定義務檢查） |
| 🛠️ **AI 開發** | **`skill-creator`** | 讓 AI 自行建立、優化、評估與客製化新的專屬 Skill |
| 🛠️ **AI 開發** | **`webapp-testing`** | 使用 Playwright 進行網頁前端自動化測試與截圖驗證 |

---

## 🔐 Google API 憑證與試算表快速設定

如果您的專案需要連線 Google 試算表（Google Sheets）或 Google 雲端硬碟：

1. **直接執行一鍵引導精靈**：
   ```bash
   python setup.py          # 選擇 [2] 或 [4]
   # 或直接執行：
   python setup_google_auth.py
   ```
   系統會自動開啟瀏覽器頁面，引導您建立專案、啟用 API、下載 `credentials.json` 並自動生成 `token.json` 與 `config.json`！
2. 亦可參考完整的逐步圖文指南：[👉 GOOGLE_AUTH_GUIDE.md](GOOGLE_AUTH_GUIDE.md)

---

## 🛡️ 核心全域三大鐵律

1. **現況檔優先 (Live State First)**：
   在任何修改前一律先讀取現況檔，以使用者當下修改後的內容為準，絕不盲目以模板覆寫。
2. **修改前自動備份**：
   修改任何程式碼或重要文件前，自動將原檔案備份為 `檔名.bak`。
3. **資料來源透明追溯**：
   所有查詢與整理結果，結尾一律附上 `file:///` 本機路徑超連結以供追溯驗證。

---
授權：MIT License | 歡迎各校教師自由 Fork 與複製使用！

