# 🔐 Google API 憑證取得與 `token.json` 生成圖文指南

本指南專為初學者與教師同仁設計，一步步引導您在 Google Cloud Console 建立 OAuth 憑證，並順利生成 `token.json` 與連接試算表。

---

## ⚡ 最推薦：使用「一鍵引導精靈」

在專案目錄下執行以下指令，系統會自動在瀏覽器依序開啟對應頁面，並引導您完成：

```bash
python setup_google_auth.py
```

---

## 📖 手動設定逐步圖文流程（5 步驟）

### 步驟 1：前往 Google Cloud Console 建立專案
1. 進入 [Google Cloud Console 建立專案頁面](https://console.cloud.google.com/projectcreate)。
2. 使用您的個人 Gmail 或 Google Workspace 帳號登入。
3. **專案名稱**：輸入好辨識的名稱（例如：`碧華國小行政秘書`）。
4. 點擊 **【建立】**，等待系統建立完成（約 10 秒）。

---

### 步驟 2：啟用 Sheets API 與 Drive API
1. 點擊頂端專案選單，確認切換至剛剛建立的專案。
2. 進入 [API 程式庫 (API Library)](https://console.cloud.google.com/apis/library)。
3. 搜尋 **`Google Sheets API`** ➔ 點擊進入 ➔ 點擊藍色按鈕 **【啟用】**。
4. 搜尋 **`Google Drive API`** ➔ 點擊進入 ➔ 點擊藍色按鈕 **【啟用】**。

---

### 步驟 3：設定 OAuth 同意畫面與測試使用者
1. 進入 [OAuth 同意畫面 (Consent Screen)](https://console.cloud.google.com/apis/credentials/consent)。
2. **User Type（使用者類型）**：選擇 **【外部 (External)】** ➔ 點擊 **【建立】**。
3. **應用程式資訊**：
   - 應用程式名稱：填寫 `行政秘書`
   - 使用者支援電子郵件：選擇您自己的 Email
   - 開發人員聯絡資訊：填寫您自己的 Email
   - 點擊 **【儲存並繼續】**。
4. **範圍 (Scopes)**：直接點擊 **【儲存並繼續】**。
5. **⚠️ 關鍵步驟：測試使用者 (Test Users)**：
   - 點擊 **【+ ADD USERS】**（新增使用者）。
   - 輸入您要登入使用的 **Gmail 帳號**。
   - 點擊 **【儲存並繼續】**。

---

### 步驟 4：建立並下載 OAuth 用戶端憑證
1. 進入 [憑證管理 (Credentials)](https://console.cloud.google.com/apis/credentials)。
2. 點擊頂端 **【+ 建立憑證】** ➔ 選擇 **【OAuth 用戶端 ID】**。
3. **應用程式類型**：選擇 **【桌面應用程式 (Desktop App)】**。
4. **名稱**：填寫 `Desktop Client` ➔ 點擊 **【建立】**。
5. 建立成功後會跳出下載視窗，點擊 **【下載 JSON】**。
6. 將下載的檔案改名為 **`credentials.json`**，並放到您的專案根目錄中。

---

### 步驟 5：執行授權並生成 `token.json`
在專案根目錄終端機執行：

```bash
python setup_google_auth.py
```

1. 瀏覽器會自動開啟 Google 登入視窗，請選擇您在步驟 3 加入的測試 Gmail 帳號。
2. **若出現「Google 尚未驗證此應用程式」警告**：
   - 點擊左下角的 **【進階 (Advanced)】**。
   - 點擊 **【前往「行政秘書」(不安全)】**。
   - 勾選所有權限並點擊 **【繼續】**。
3. 授權完成後，終端機將會顯示 `✅ token.json 授權憑證生成成功！`。
4. 輸入您的 Google 試算表網址，系統會自動驗證連線並將設定存入 `config.json`！

---

## 🛠️ 常見問題與疑難排解 (FAQ)

### Q1：授權時出現「存取遭到封鎖：此應用程式未經過驗證」或錯誤 403？
- **原因**：尚未將您的 Gmail 帳號加入「測試使用者 (Test Users)」。
- **解法**：回到步驟 3 的「OAuth 同意畫面」，在「測試使用者」清單中點擊 `+ ADD USERS` 加入您的 Gmail 即可。

### Q2：`token.json` 過期或失效報 `invalid_grant` 怎麼辦？
- **解法**：直接刪除當前目錄下的 `token.json`，重新執行 `python setup_google_auth.py` 即可自動重新授權產生新 Token。

### Q3：如何確認 Google 試算表 ID 是否正確？
- Google 試算表網址格式為：
  `https://docs.google.com/spreadsheets/d/` **`17vdUkxEz1-jD0CuNzufsWRSaG05GKWX75y2iFlCIglU`** `/edit`
- 中間粗體部分即為 `SPREADSHEET_ID`。

---
授權：MIT License | 歡迎各校行政團隊自由參考使用！
