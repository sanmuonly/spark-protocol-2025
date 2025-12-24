import datetime
import os

def sync_mind_clone(beijing_time):
    input_path = "INPUT.txt"
    clone_path = "MIND_CLONE.md"
    
    # 打印调试信息，让我们知道脚本运行到哪了
    if not os.path.exists(input_path):
        print("错误：没找到 INPUT.txt")
        return False

    with open(input_path, "r", encoding="utf-8") as f:
        new_thought = f.read().strip()
    
    print(f"信箱内容: {new_thought}")

    # 只要内容不是 empty，就开始搬运
    if new_thought and new_thought != "empty":
        # 如果文件不存在，先创建它
        if not os.path.exists(clone_path):
            with open(clone_path, "w", encoding="utf-8") as f:
                f.write("# 🧠 星火协议：思维克隆记录 (Mind Clone)\n")

        with open(clone_path, "a", encoding="utf-8") as f:
            f.write(f"\n### 同步记录: {beijing_time}\n")
            f.write(f"- **思维碎片**：{new_thought}\n")
        
        # 成功后清空信箱
        with open(input_path, "w", encoding="utf-8") as f:
            f.write("empty")
        return True
    return False

def update_readme(beijing_time, synced):
    path = "README.md"
    if not os.path.exists(path): return
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
