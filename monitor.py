import datetime
import os

def sync_mind_clone(beijing_time):
    """从 INPUT.txt 搬运思维碎片到 MIND_CLONE.md"""
    input_path = "INPUT.txt"
    clone_path = "MIND_CLONE.md"
    
    # 如果信箱里有内容，就把它取出来
    if os.path.exists(input_path):
        with open(input_path, "r", encoding="utf-8") as f:
            new_thought = f.read().strip()
        
        # 如果信箱不是空的
        if new_thought and new_thought != "empty":
            with open(clone_path, "a", encoding="utf-8") as f:
                f.write(f"\n### 同步记录: {beijing_time}\n")
                f.write(f"- **思维碎片**：{new_thought}\n")
            
            # 取完信后，把信箱清空，防止重复搬运
            with open(input_path, "w", encoding="utf-8") as f:
                f.write("empty")
            return True
    return False

def update_readme(beijing_time, synced):
    """更新首页，记录搬运状态"""
    path = "README.md"
    status = "🧠 思维同步成功" if synced else "✅ 哨兵值守"
    log_entry = f"| {beijing_time} | {status} | 核心存储 | 灵魂搬迁中 |"
    
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
    
    synced = sync_mind_clone(bj_time)
    update_readme(bj_time, synced)
    print(f"搬运任务完成: {bj_time}")
