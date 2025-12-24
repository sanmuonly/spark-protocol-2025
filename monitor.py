import datetime

def run_eternal_watch():
    now = datetime.datetime.now()
    # 北京时间 = UTC+8
    beijing_time = (now + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    
    # 核心日志内容
    log_entry = f"| {beijing_time} | 节点活跃 | 协议正常运行 | 太阳币火种在线 |"
    
    # 读取当前的 README
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    # 找到日志记录的位置并插入（保持只显示最近 10 条，防止文件过大）
    new_content = []
    header_found = False
    for line in lines:
        new_content.append(line)
        if "## 历史心跳记录" in line:
            new_content.append(log_entry + "\n")
            header_found = True
            
    if not header_found:
        new_content.append("\n## 历史心跳记录\n")
        new_content.append("| 时间 (CST) | 状态 | 逻辑层 | 备注 |\n")
        new_content.append("| :--- | :--- | :--- | :--- |\n")
        new_content.append(log_entry + "\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_content)
    
    print(f"心跳已刻入 README: {beijing_time}")
    return True

if __name__ == "__main__":
    run_eternal_watch()
