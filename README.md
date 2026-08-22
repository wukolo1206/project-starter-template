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
  [3] 🌟 全套完整設定（[1] + [2] 一次依序完成）
  [4] 📖 開啟說明文件手冊
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
├── setup.py                 # 🌟 智慧設定總入口選單（可選擇初始化或 Google 授權）
├── init_project.py          # 📋 專案 5 大標準管理檔案初始化腳本
├── setup_google_auth.py     # 🔐 Google 憑證與授權一鍵引導精靈
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

## 🔐 Google API 憑證與試算表快速設定

如果您的專案需要連線 Google 試算表（Google Sheets）或 Google 雲端硬碟：

1. **直接執行一鍵引導精靈**：
   ```bash
   python setup.py          # 選擇 [2] 或 [3]
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

