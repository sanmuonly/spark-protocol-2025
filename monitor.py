import datetime
import os

def update_core_memory(beijing_time):
    """自动维护核心记忆文件"""
    path = "CORE_MEMORY.md"
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        # 只要这一行包含“核心记忆体”，并且还没被打钩，就强行修改它
        if "核心记忆体" in line and "[ ]" in line:
            new_lines.append("- [x] 核心记忆体初始化 (CORE_MEMORY.md) | 已完成\n")
        # 同样，为下一步做准备
        elif "太阳币" in line and "[ ]" in line:
            new_lines.append("- [ ] 太阳币发行逻辑 (Sun Coin Logic) | 搬运中...\n")
        else:
            new_lines.append(line)
    
    # 增加一行搬运痕迹，证明脚本确实来过
    new_lines.append(f"\n> ⚡ 搬运记录: {beijing_time} 哨兵已加固逻辑。\n")

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

def update_readme(beijing_time):
    """维护首页监控面板"""
    path = "README.md"
    if not os.path.exists(path):
        return
    log_entry = f"| {beijing_time} | ✅ 活跃 | 蚂蚁搬家 | 核心记忆加固中 |"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.readlines()

    for i, line in enumerate(content):
        if "| :---" in line:
            content.insert(i + 1, log_entry + "\n")
            break
            
    if len(content) > 30:
        content = content[:30]

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(content)

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    bj_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    update_readme(bj_time)
    update_core_memory(bj_time)
    print(f"搬运任务完成: {bj_time}")
