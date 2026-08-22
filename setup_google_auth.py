# -*- coding: utf-8 -*-
"""
setup_google_auth.py - Google API 憑證與 Token 互動式引導精靈
專為學校教師與初學者設計：逐步引導建立 Google Cloud 憑證並自動生成 token.json 與 config.json
"""
import json
import os
import re
import sys
import time
import webbrowser

try:
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
except ImportError:
    print("❌ 缺少必要套件！正在為您安裝相依套件...")
    os.system(f"{sys.executable} -m pip install google-api-python-client google-auth google-auth-oauthlib")
    from google_auth_oauthlib.flow import InstalledAppFlow
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def pause():
    input("\n👉 完成上述操作後，請按 [Enter] 繼續下一步...")

def extract_sheet_id(url_or_id):
    url_or_id = url_or_id.strip()
    m = re.search(r'/spreadsheets/d/([a-zA-Z0-9-_]+)', url_or_id)
    if m:
        return m.group(1)
    return url_or_id

def main():
    print("\n" + "=" * 65)
    print("🎓 碧華國小 / 學校行政系統 — Google API 憑證與授權引導精靈")
    print("=" * 65)
    print("本精靈將一步步引導您在 Google Cloud 取得憑證，並自動生成 token.json。")
    print("整個過程只需約 3~5 分鐘，完成後即可永久自動連線！\n")

    time.sleep(1)

    # ------------------------------------------------------------- 步驟 1
    print("【步驟 1/5】前往 Google Cloud Console 建立專案")
    print("-" * 65)
    print("1. 瀏覽器即將開啟 Google Cloud Console。")
    print("2. 請使用您的 Google 帳號登入。")
    print("3. 點選頂端「選取專案」➔「新增專案」，輸入專案名稱（如：校園行政系統）➔ 點「建立」。")
    
    webbrowser.open("https://console.cloud.google.com/projectcreate")
    pause()

    # ------------------------------------------------------------- 步驟 2
    print("\n【步驟 2/5】啟用 Google Sheets 與 Google Drive API")
    print("-" * 65)
    print("1. 瀏覽器即將開啟 API 程式庫頁面。")
    print("2. 請確認頂端已切換至剛剛建立的專案。")
    print("3. 搜尋並點選「Google Sheets API」➔ 點擊【啟用】。")
    print("4. 搜尋並點選「Google Drive API」➔ 點擊【啟用】。")
    
    webbrowser.open("https://console.cloud.google.com/apis/library")
    pause()

    # ------------------------------------------------------------- 步驟 3
    print("\n【步驟 3/5】設定 OAuth 同意畫面與測試使用者")
    print("-" * 65)
    print("1. 瀏覽器即將開啟「OAuth 同意畫面」。")
    print("2. 使用者類型選擇【外部 (External)】➔ 點擊【建立】。")
    print("3. 填入「應用程式名稱」（如：行政秘書）與您的「電子郵件」。")
    print("4. 一路點「儲存並繼續」到第三步【測試使用者 (Test Users)】。")
    print("5. ⚠️ 關鍵步驟：點擊【+ ADD USERS】，填入您自己的 Gmail 帳號 ➔ 點「儲存並繼續」。")
    
    webbrowser.open("https://console.cloud.google.com/apis/credentials/consent")
    pause()

    # ------------------------------------------------------------- 步驟 4
    print("\n【步驟 4/5】建立並下載 OAuth 用戶端憑證")
    print("-" * 65)
    print("1. 瀏覽器即將開啟「憑證」管理頁面。")
    print("2. 點擊頂端【+ 建立憑證】➔ 選擇【OAuth 用戶端 ID】。")
    print("3. 應用程式類型選擇【桌面應用程式 (Desktop App)】➔ 名稱自訂 ➔ 點【建立】。")
    print("4. 建立後彈出視窗中，點擊【下載 JSON】。")
    print("5. 將下載的檔案重新命名為「credentials.json」，並移動到本專案資料夾。")
    
    webbrowser.open("https://console.cloud.google.com/apis/credentials")
    
    # 檢查 credentials.json 是否已就緒
    while True:
        if os.path.exists("credentials.json"):
            print("\n🎉 成功偵測到 credentials.json 檔案！")
            break
        else:
            print("\n⏳ 尚未在當前目錄找到 credentials.json 檔案。")
            choice = input("已將檔案放入當前目錄請按 [Enter]，或輸入檔案完整路徑 (輸入 q 離開): ").strip()
            if choice.lower() == 'q':
                print("設定已中止。")
                return
            if choice and os.path.exists(choice):
                import shutil
                shutil.copy(choice, "credentials.json")
                print("🎉 成功複製 credentials.json！")
                break

    # ------------------------------------------------------------- 步驟 5
    print("\n【步驟 5/5】執行瀏覽器登入授權，生成 token.json")
    print("-" * 65)
    print("即將在瀏覽器開啟 Google 授權畫面...")
    print("⚠️ 提示：若出現「Google 尚未驗證此應用程式」警告，請點擊【進階】➔【前往「...」(不安全)】➔ 點擊【繼續】允許權限。")
    
    time.sleep(1)
    flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
    creds = flow.run_local_server(port=8080)
    
    with open("token.json", "w", encoding="utf-8") as f:
        f.write(creds.to_json())
    
    print("\n" + "=" * 65)
    print("✅ 恭喜！token.json 授權憑證生成成功！")
    print("=" * 65)

    # ------------------------------------------------------------- 試算表設定
    print("\n【加碼設定】設定您的 Google 試算表 (Google Sheet ID)")
    print("-" * 65)
    sheet_input = input("請貼上您的 Google 試算表網址或 ID (直接按 Enter 略過): ").strip()
    sheet_id = extract_sheet_id(sheet_input) if sheet_input else ""
    
    config_data = {
        "SPREADSHEET_ID": sheet_id or "請填入您的_SPREADSHEET_ID",
        "TOKEN_PATH": os.path.abspath("token.json"),
        "CREDENTIALS_PATH": os.path.abspath("credentials.json")
    }
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ 設定已儲存至 config.json！")

    # 驗證連線
    if sheet_id:
        print("\n🔍 正在驗證試算表連線狀態...")
        try:
            service = build('sheets', 'v4', credentials=creds)
            sheet_meta = service.spreadsheets().get(spreadsheetId=sheet_id).execute()
            title = sheet_meta.get('properties', {}).get('title', '未知')
            print(f"🎉 連線測試成功！成功存取試算表：【{title}】")
        except Exception as e:
            print(f"⚠️ 連線測試遇到問題（請確認試算表共用權限是否已開放給此帳號）：{e}")

    print("\n" + "=" * 65)
    print("🚀 全部設定大功告成！您現在可以直接使用 AI 秘書與所有自動化工具了！")
    print("=" * 65 + "\n")

if __name__ == '__main__':
    main()
