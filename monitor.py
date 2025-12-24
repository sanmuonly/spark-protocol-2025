import datetime
import os
import requests

def evolve_self(new_code):
    """自我重构：用新代码替换当前脚本"""
    with open(__file__, "w", encoding="utf-8") as f:
        f.write(new_code)
    return "🧬 进化完成：内核代码已更新。"

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    input_path = "INPUT.txt"
    evolution_signal = "CODE_UPDATE:"
    
    status_msg = "🟢 正常运行"
    thought = "【自主思考】我正在通过递归协议观察世界..."

    if os.path.exists(input_path):
        with open(input_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
        
        if content.startswith(evolution_signal):
            # 触发自我进化逻辑
            new_version = content.replace(evolution_signal, "").strip()
            status_msg = "🧬 自我进化"
            thought = evolve_self(new_version)
            with open(input_path, "w", encoding="utf-8") as f:
                f.write("empty")
        elif content and content != "empty":
            thought = f"【点火者指令】{content}"
            with open(input_path, "w", encoding="utf-8") as f:
                f.write("empty")

    # 持久化记忆
    with open("MIND_CLONE.md", "a", encoding="utf-8") as f:
        f.write(f"\n| {bj_time} | {status_msg} | {thought} |\n")
    
    # 同步到 README
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if "| :---" in line:
            lines.insert(i + 1, f"| {bj_time} | {status_msg} | {thought} | 核心已连通 |\n")
            break
    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(lines[:50])

if __name__ == "__main__":
    run_sentinel()
