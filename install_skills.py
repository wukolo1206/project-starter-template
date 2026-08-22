# -*- coding: utf-8 -*-
"""
install_skills.py - 常用 Skills 全域與專案安裝器
支援一鍵將 using-superpowers、Office 文件處理、視覺設計等 Skills 安裝至 Antigravity、Gemini CLI、Claude Code 與當前專案。
"""
import os
import shutil
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# 技能定義清單
SKILL_DEFINITIONS = {
    # 核心大腦
    "using-superpowers": {
        "cat": "👑 核心總控",
        "desc": "強制 AI 先檢查並精準調用專屬 Skill，提升執行嚴謹度",
        "tags": ["core", "office_design", "teaching_admin"]
    },
    # Office 文件處理類
    "docx": {
        "cat": "📑 Office辦公",
        "desc": "Word 文件（.docx）深度排版、表格處理、目錄與列印級生成",
        "tags": ["office_design", "teaching_admin"]
    },
    "xlsx": {
        "cat": "📑 Office辦公",
        "desc": "Excel 試算表（.xlsx）資料分析、統計、公式與格式化",
        "tags": ["office_design", "teaching_admin"]
    },
    "pdf": {
        "cat": "📑 Office辦公",
        "desc": "PDF 公文與教冊深度文字抽取、表格解析與合併分割",
        "tags": ["office_design", "teaching_admin"]
    },
    "pptx": {
        "cat": "📑 Office辦公",
        "desc": "PowerPoint 簡報生成、教學投影片編排與大綱摘要",
        "tags": ["office_design"]
    },
    # 視覺設計與互動工具類
    "canvas-design": {
        "cat": "🎨 視覺互動",
        "desc": "宣傳海報、班級公約、活動傳單美編設計（產出高解析 PNG/PDF）",
        "tags": ["office_design"]
    },
    "frontend-design": {
        "cat": "🎨 視覺互動",
        "desc": "互動式教學網頁、計時器、班級抽籤輪盤、HTML 遊戲設計",
        "tags": ["office_design"]
    },
    "algorithmic-art": {
        "cat": "🎨 視覺互動",
        "desc": "p5.js 數學圖形、碎形幾何與程式美學互動生成",
        "tags": ["office_design"]
    },
    "theme-factory": {
        "cat": "🎨 視覺互動",
        "desc": "文件與網頁設計主題樣式庫（10組專業配色與字型主題）",
        "tags": ["office_design"]
    },
    "web-artifacts-builder": {
        "cat": "🎨 視覺互動",
        "desc": "複雜多元件 React / Tailwind / shadcn 教學工具與儀表板",
        "tags": ["office_design"]
    },
    # 教學與行政類
    "chinese-quiz-generator": {
        "cat": "🎒 教學行政",
        "desc": "國語科標準考題產生器（南一/康軒/翰林 1~6 年級命題規範）",
        "tags": ["teaching_admin"]
    },
    "teacher-meeting-organizer": {
        "cat": "🎒 教學行政",
        "desc": "教師會議深度整理、方案 A 累加至 Google 試算表總檢核表",
        "tags": ["teaching_admin"]
    },
    "teacher-meeting-auditor": {
        "cat": "🎒 教學行政",
        "desc": "會議時程防呆審核（場地撞期、同日負擔、法定義務漏列檢查）",
        "tags": ["teaching_admin"]
    },
    # AI 代理人與開發工具類
    "skill-creator": {
        "cat": "🛠️ AI開發",
        "desc": "讓 AI 自行建立、優化、評估與客製化新的專屬 Skill",
        "tags": ["dev_tools", "office_design"]
    },
    "webapp-testing": {
        "cat": "🛠️ AI開發",
        "desc": "使用 Playwright 進行網頁前端自動化測試與截圖驗證",
        "tags": ["dev_tools", "office_design"]
    }
}

def detect_ai_agent_and_targets():
    """
    智慧偵測當前運行的 AI Agent 或本機已配置的 AI 環境，
    自動決定最佳的全域與專案安裝目標路徑。
    """
    user_home = os.path.expanduser("~")
    gemini_path = os.path.join(user_home, ".gemini", "config", "skills")
    claude_path = os.path.join(user_home, ".claude", "skills")
    project_path = os.path.abspath(os.path.join(".agents", "skills"))

    target_dirs = {}
    detected_agents = []

    # 1. 執行時期環境變數偵測 (Runtime Detection - 優先度最高)
    is_antigravity = any(k.startswith("ANTIGRAVITY_") for k in os.environ)
    is_claude = "CLAUDE_CODE" in os.environ or "CLAUDE_PROJECT_DIR" in os.environ
    is_gemini = "GEMINI_CLI" in os.environ or "GEMINI_PROJECT_DIR" in os.environ

    if is_antigravity:
        detected_agents.append("🌐 Google Antigravity (當前運行中)")
        target_dirs["Antigravity 全域技能目錄"] = gemini_path
    elif is_claude:
        detected_agents.append("🤖 Claude Code (當前運行中)")
        target_dirs["Claude Code 全域技能目錄"] = claude_path
    elif is_gemini:
        detected_agents.append("✨ Gemini CLI (當前運行中)")
        target_dirs["Gemini CLI 全域技能目錄"] = gemini_path

    # 2. 若無特定執行環境變數（例如在獨立終端機執行），根據本機已安裝的 AI 目錄動態加入
    if not detected_agents:
        if os.path.exists(os.path.join(user_home, ".gemini")):
            detected_agents.append("🌐 Antigravity / Gemini CLI (本機已安裝)")
            target_dirs["Antigravity / Gemini CLI 全域"] = gemini_path
        if os.path.exists(os.path.join(user_home, ".claude")):
            detected_agents.append("🤖 Claude Code (本機已安裝)")
            target_dirs["Claude Code 全域"] = claude_path

    # 3. 預設始終包含當前專案工作區 (.agents/skills)
    target_dirs["當前專案工作區 (.agents/skills)"] = project_path

    return detected_agents, target_dirs

def copy_skill(skill_name, src_base, target_dir):
    src_path = os.path.join(src_base, skill_name)
    if not os.path.exists(src_path):
        return False, f"來源不存在: {src_path}"
    
    dst_path = os.path.join(target_dir, skill_name)
    os.makedirs(dst_path, exist_ok=True)
    shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    return True, dst_path

def run_installation(selected_skills):
    if not selected_skills:
        print("\n⚠️ 未選取任何 Skill，已取消安裝。")
        return

    script_dir = os.path.dirname(os.path.abspath(__file__))
    src_base = os.path.join(script_dir, "skills_pack")
    
    if not os.path.exists(src_base):
        print(f"\n❌ 找不到 skills_pack 資料夾！路徑: {src_base}")
        return

    print("\n" + "=" * 65)
    print(f"📦 開始安裝選定的 {len(selected_skills)} 個 Skills...")
    print("=" * 65)

    detected_agents, target_dirs = detect_ai_agent_and_targets()

    print("🔍 智慧 AI Agent 環境偵測：")
    if detected_agents:
        for ag in detected_agents:
            print(f"  🎯 偵測到 AI Agent: {ag}")
    else:
        print("  🎯 偵測到通用終端環境 (自動配置專案與通用全域目錄)")

    print("\n📂 自動判斷的最佳安裝目標路徑：")
    for label, path in target_dirs.items():
        print(f"  📁 [{label}] ➔ {path}")
    print("-" * 65)

    success_count = 0
    for skill in selected_skills:
        info = SKILL_DEFINITIONS.get(skill, {})
        cat = info.get("cat", "自訂")
        print(f"\n🚀 正在安裝: [{cat}] {skill} ...")
        
        for label, tdir in target_dirs.items():
            ok, msg = copy_skill(skill, src_base, tdir)
            if ok:
                print(f"   ✅ 已安裝至 {label}")
            else:
                print(f"   ❌ 安裝失敗 ({label}): {msg}")
        success_count += 1

    print("\n" + "=" * 65)
    print(f"🎉 全部安裝完成！共成功安裝 {success_count} 個 Skills！")
    print("💡 提示：Antigravity、Claude Code 與 Gemini CLI 均已全域支援上述技能！")
    print("=" * 65 + "\n")

def main():
    while True:
        print("\n" + "=" * 65)
        print("📦 常用 Skills 安裝管理器 (Skill Pack Installer)")
        print("=" * 65)
        print("請選擇您要安裝的技能組合：\n")
        print("  [1] 🌟 全套精選大滿貫（全部 15 個 Skills 一鍵全裝）")
        print("      ➔ using-superpowers + Office + 視覺設計 + 教學行政 + AI開發(skill-creator/webapp-testing)")
        print()
        print("  [2] 📑 Office 辦公文件、視覺設計與開發工具包（共 11 個）")
        print("      ➔ using-superpowers + docx + xlsx + pdf + pptx")
        print("      ➔ canvas-design + frontend-design + algorithmic-art + theme-factory")
        print("      ➔ skill-creator + webapp-testing")
        print()
        print("  [3] 🎒 教師教學出題與學校行政包（共 6 個）")
        print("      ➔ using-superpowers + 國語出題 + 會議整理 + 防呆審核 + docx + pdf")
        print()
        print("  [4] 🎯 自訂清單（自由勾選想要安裝的 Skill）")
        print()
        print("  [0] 🚪 返回上一層")
        print("=" * 65)

        choice = input("👉 請輸入選項編號 [1/2/3/4/0，預設: 2]: ").strip()
        if choice == "":
            choice = "2"

        if choice == "1":
            selected = list(SKILL_DEFINITIONS.keys())
            run_installation(selected)
            break

        elif choice == "2":
            selected = [k for k, v in SKILL_DEFINITIONS.items() if "office_design" in v["tags"] or k == "using-superpowers"]
            run_installation(selected)
            break

        elif choice == "3":
            selected = [k for k, v in SKILL_DEFINITIONS.items() if "teaching_admin" in v["tags"] or k == "using-superpowers"]
            run_installation(selected)
            break

        elif choice == "4":
            print("\n請勾選您想安裝的 Skill（輸入編號，以逗號或空白分隔，例如: 1 2 5 7）：")
            skill_keys = list(SKILL_DEFINITIONS.keys())
            for idx, key in enumerate(skill_keys, 1):
                item = SKILL_DEFINITIONS[key]
                print(f"  [{idx:2d}] [{item['cat']}] {key:<26} : {item['desc']}")
            
            raw_input = input("\n請輸入編號 (輸入 all 全選): ").strip()
            if raw_input.lower() == "all":
                run_installation(skill_keys)
                break
            else:
                selected = []
                import re
                nums = re.findall(r'\d+', raw_input)
                for n in nums:
                    num_idx = int(n) - 1
                    if 0 <= num_idx < len(skill_keys):
                        selected.append(skill_keys[num_idx])
                if selected:
                    # 去重保留順序
                    selected = list(dict.fromkeys(selected))
                    run_installation(selected)
                    break
                else:
                    print("⚠️ 未選擇有效編號。")

        elif choice == "0":
            break

        else:
            print("⚠️ 無效的選項，請重新輸入。")

if __name__ == "__main__":
    main()
