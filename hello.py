#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
我的第一个Python程序
作者：[您的名字]
日期：2024-01-01
"""

def main():
    """主函数"""
    print("="*50)
    print("Hello, AI World!")
    print("欢迎来到人工智能的世界！")
    print("="*50)
    
    # 显示Python版本
    import sys
    print(f"Python版本：{sys.version}")
    
    # 显示当前时间
    from datetime import datetime
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"当前时间：{current_time}")
    
    # 个人信息
    student_info = {
        "姓名": "学员姓名",
        "目标": "掌握AI编程",
        "周次": "第1周"
    }
    
    print("\n学员信息：")
    for key, value in student_info.items():
        print(f"  {key}: {value}")
    
    print("="*50)

if __name__ == "__main__":
    main()

# 1. 查看当前状态（应显示hello.py为未跟踪文件）
git status

# 2. 添加文件到暂存区
git add hello.py

# 或添加所有文件
git add .

# 3. 查看暂存区状态（文件变绿）
git status

# 4. 提交到本地仓库
git commit -m "添加第一个Python程序hello.py"

# 5. 推送到GitHub
git push origin main

# 如果是master分支
git push origin master
