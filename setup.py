# -*- coding: utf-8 -*-
"""
setup.py - 學校行政與備課專案 — 智慧設定總入口精靈
整合專案初始化與 Google OAuth 授權引導，提供清晰選單供使用者依需求選擇。
"""
import os
import sys
import time

# 匯入子模組邏輯
try:
    from init_project import init_project
except ImportError:
    init_project = None

try:
    from setup_google_auth import main as setup_google_auth
except ImportError:
    setup_google_auth = None

def print_banner():
    print("\n" + "=" * 65)
    print("🚀 學校行政與備課專案 — 智慧設定總入口精靈 (Setup Wizard)")
    print("=" * 65)
    print("歡迎使用！請選擇您希望進行的設定項目：\n")
    print("  [1] 📋 專案標準環境初始化")
    print("      ➔ 自動生成 5 大標準管理文件 (CLAUDE.md, AGENTS.md 等)")
    print()
    print("  [2] 🔐 設定 Google 試算表與 OAuth 授權")
    print("      ➔ 逐步引導建立 Google Cloud 憑證並生成 token.json")
    print()
    print("  [3] 🌟 全套完整設定（推薦新專案使用）")
    print("      ➔ 依序完成：[1] 專案初始化 + [2] Google API 授權")
    print()
    print("  [4] 📖 開啟說明文件")
    print("      ➔ 在瀏覽器中開啟 README.md 與 GOOGLE_AUTH_GUIDE.md")
    print()
    print("  [0] 🚪 離開程式")
    print("=" * 65)

def open_docs():
    import webbrowser
    print("\n正在開啟說明文件...")
    readme_path = os.path.abspath("README.md")
    guide_path = os.path.abspath("GOOGLE_AUTH_GUIDE.md")
    
    if os.path.exists(readme_path):
        webbrowser.open(f"file:///{readme_path}")
    if os.path.exists(guide_path):
        webbrowser.open(f"file:///{guide_path}")
    print("✅ 已在瀏覽器中開啟說明文件！\n")

def main():
    while True:
        print_banner()
        choice = input("👉 請輸入選項編號 [1/2/3/4/0，預設: 3]: ").strip()
        if choice == "":
            choice = "3"

        if choice == "1":
            print("\n" + "-" * 65)
            print("🚀 啟動：專案標準環境初始化")
            print("-" * 65)
            if init_project:
                init_project()
            else:
                os.system(f"{sys.executable} init_project.py")
            input("\n按 [Enter] 返回主選單...")

        elif choice == "2":
            print("\n" + "-" * 65)
            print("🔐 啟動：Google 試算表與 OAuth 授權引導")
            print("-" * 65)
            if setup_google_auth:
                setup_google_auth()
            else:
                os.system(f"{sys.executable} setup_google_auth.py")
            input("\n按 [Enter] 返回主選單...")

        elif choice == "3":
            print("\n" + "=" * 65)
            print("🌟 啟動：全套完整設定（專案初始化 ➔ Google API 授權）")
            print("=" * 65)
            
            # 第一階段：專案初始化
            print("\n【第一階段：專案標準環境初始化】")
            if init_project:
                init_project()
            else:
                os.system(f"{sys.executable} init_project.py")
            
            time.sleep(1)
            
            # 詢問是否繼續第二階段
            proceed = input("\n👉 專案檔案已建置完成！是否立即設定 Google 試算表授權？[Y/n]: ").strip().lower()
            if proceed in ("", "y", "yes"):
                print("\n【第二階段：Google 試算表與 OAuth 授權】")
                if setup_google_auth:
                    setup_google_auth()
                else:
                    os.system(f"{sys.executable} setup_google_auth.py")
            else:
                print("已跳過 Google 授權設定。日後可單獨執行選項 [2] 或 python setup_google_auth.py。")
                
            input("\n按 [Enter] 返回主選單...")

        elif choice == "4":
            open_docs()
            input("按 [Enter] 返回主選單...")

        elif choice == "0":
            print("\n👋 感謝使用，祝您備課與行政工作順利！\n")
            break

        else:
            print(f"\n⚠️ 無效的選項「{choice}」，請輸入 0 ~ 4 之間的數字。")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 程式已由使用者中斷，再見！")
