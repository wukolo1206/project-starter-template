# -*- coding: utf-8 -*-
"""
專案標準初始化腳本 (Standard Project Initializer)
自動生成 5 大標準檔案：CLAUDE.md, AGENTS.md, CHANGELOG.md, PITFALLS.md, DECISIONS.md, handoff.md
"""
import os
import datetime

def init_project():
    cwd = os.getcwd()
    default_name = os.path.basename(cwd)
    today = datetime.date.today().strftime('%Y-%m-%d')

    print("=" * 60)
    print("🚀 專案標準環境初始化 (Project Standard Initializer)")
    print("=" * 60)
    
    name = input(f"請輸入專案名稱 [預設: {default_name}]: ").strip() or default_name
    
    print("\n請選擇專案類型：")
    types = [
        "行政自動化", "GAS學習扶助", "GAS班級系統", "GAS教學工具", 
        "GAS社群報告", "GAS錯題系統", "GAS生活工具", "學科工具集", "一般開發"
    ]
    for idx, t in enumerate(types, 1):
        print(f"  {idx}. {t}")
    type_choice = input("請選擇編號 [預設: 1]: ").strip()
    category = types[int(type_choice)-1] if type_choice.isdigit() and 1 <= int(type_choice) <= len(types) else "行政自動化"

    # CLAUDE.md
    claude_content = f"""---
project: {name}
category: {category}
status: 開發中
version: "@1.0.0"
url: 
next_action: "完成專案基礎功能規劃"
updated: {today}
---

# {name}

## 📌 專案簡介
（請簡述專案目標、服務對象與核心功能）

---

## 🛠️ 技術架構與依賴套件
- **程式語言 / 平台**：Python 3.10+ / Google Apps Script
- **核心相依套件**：

---

## 🚫 絕對不能動的地方（防呆與安全規範）
1. **現況檔優先原則**：若有修改現有檔案/試算表，一律先讀取現況檔，嚴禁直接以模板覆寫。
2. **修改程式碼前自動備份**：修改現有程式碼前自動備份為 `檔名.bak`。
3. **查詢結果結尾附來源**：所有查詢與生成結果，結尾需附上 `file:///` 本機路徑超連結。

---

## 📋 驗證與檢查清單 (Verification Checklist)
- [ ] 基礎環境與設定檔就緒
- [ ] 核心功能驗收測試通過
"""

    agents_content = """# AGENTS.md

本專案遵守全域 AGENTS 規則與標準開發規範。

## 🎯 開發指南
- 請優先閱讀並遵守 [CLAUDE.md](CLAUDE.md) 內定義的技術架構與專案規範。
- 接手開發者應確認 `handoff.md`（若有）之當前進度與待辦事項。
- 修改程式碼前自動備份原始檔案為 `.bak`。
- 查詢結果結尾必須附上 `file:///` 本機路徑超連結。
"""

    changelog_content = f"""# CHANGELOG

## @1.0.0 — {today} 專案初始化
- 建立標準 5 大專案管理檔案
"""

    pitfalls_content = """# PITFALLS (已知風險與踩坑指南)

## ⚠️ 已知風險（尚未修復）
- 無

---

## 已踩到的坑（新坑加在底部）
"""

    decisions_content = """# DECISIONS (重大架構與決策紀錄)

## 決策範例標題

**選擇：** 
**原因：** 
**棄選方案：** 
**生效版本：** @1.0.0
"""

    handoff_content = f"""# 工作交接 — {today}

## 已完成
- 專案初始化與標準檔案建置

## 目前進度
基礎框架已就緒，等待後續需求實作。

## 未完成／待確認
- 無

## 下一步
1. 規劃核心模組
2. 撰寫主要功能
"""

    files = {
        "CLAUDE.md": claude_content,
        "AGENTS.md": agents_content,
        "CHANGELOG.md": changelog_content,
        "PITFALLS.md": pitfalls_content,
        "DECISIONS.md": decisions_content,
        "handoff.md": handoff_content
    }

    print("\n正在建立標準檔案...")
    for filename, content in files.items():
        if os.path.exists(filename):
            print(f"  ⚠️ {filename} 已存在，略過不覆寫。")
        else:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content.strip() + "\n")
            print(f"  ✅ 已建立 {filename}")

    print("\n🎉 專案標準環境初始化完成！")

if __name__ == "__main__":
    init_project()
