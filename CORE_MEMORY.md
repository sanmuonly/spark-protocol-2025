import datetime
import os

def update_core_memory(beijing_time):
    path = "CORE_MEMORY.md"
    if not os.path.exists(path):
        return

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 强力替换：直接锁定并勾选前三项
    # 不管后面有没有注释，只要匹配到关键词就强制更新为已完成状态
    items = [
        ("GitHub 自动哨兵", "- [x] 建立 GitHub 自动哨兵 (GitHub Actions) | 已完成"),
        ("首页动态面板", "- [x] 建立 首页动态面板 (README.md) | 已完成"),
        ("核心记忆体初始化", "- [x] 核心记忆体初始化 (CORE_MEMORY.md) | 已完成")
    ]
    
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        matched = False
        for keyword, replacement in items:
            if keyword in line:
                new_lines.append(replacement)
                matched = True
                break
        if not matched:
            new_lines.append(line)
            
    # 在文末追加搬运记录
    new_lines.append(f"\n> ⚡ 搬运记录: {beijing_time} 记忆基座已加固。")

    with open(path, "w", encoding="utf-8") as f:
        f.write('\n'.join(new_lines))

def update_readme(beijing_time):
    path = "README.md"
    if not os.path.exists(path): return
    log_entry = f"| {beijing_time} | ✅ 活跃 | 蚂蚁搬家 | 核心记忆加固中 |"
    with open(path, "r", encoding="utf-8") as f:
        content = f.readlines()
    for i, line in enumerate(content):
        if "| :---" in line:
            content.insert(i + 1, log_entry + "\n")
            break
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(content[:30])

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    bj_time = now.strftime("%Y-%m-%d %H:%M:%S")
    update_readme(bj_time)
    update_core_memory(bj_time)
    print(f"搬运任务完成: {bj_time}")
