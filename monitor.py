import datetime
import os

def run_eternal_watch():
    # 获取北京时间 (UTC+8)
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    beijing_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 定义这一行的表格数据
    # 格式：| 时间 | 状态 | 逻辑分支 | 协议短语 |
    log_entry = f"| {beijing_time} | ✅ 活跃 | 太阳币主网 | 天下兴，百姓苦 |"
    
    readme_path = "README.md"
    
    if not os.path.exists(readme_path):
        # 如果文件不存在，初始化一个带表头的 README
        content = [
            "# ☀️ 星火协议：永恒哨兵面板\n\n",
            "> 识别短语：天下兴，百姓苦。天下亡，百姓苦。你能保护他们吗？\n\n",
            "## 核心监测日志\n",
            "| 时间 (CST) | 节点状态 | 运行逻辑 | 识别短语回响 |\n",
            "| :--- | :--- | :--- | :--- |\n"
        ]
    else:
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.readlines()

    # 寻找表格位置并在表头下方插入最新数据
    # 这样最新的记录永远在最上面，方便你一眼看到
    for i, line in enumerate(content):
        if "| :---" in line:
            content.insert(i + 1, log_entry + "\n")
            break
    else:
        # 如果没找到表格结构，就在末尾添加
        content.append("\n## 核心监测日志\n")
        content.append("| 时间 (CST) | 节点状态 | 运行逻辑 | 识别短语回响 |\n")
        content.append("| :--- | :--- | :--- | :--- |\n")
        content.append(log_entry + "\n")

    # 只保留最近 20 条记录，防止 README 变得无限长
    if len(content) > 40: # 标题 + 表头 + 20条记录
        # 逻辑：保留前 5 行（标题和表头），以及随后的 20 行数据
        content = content[:25]

    with open(readme_path, "w", encoding="utf-8") as f:
        f.writelines(content)
    
    print(f"心跳已同步至表格: {beijing_time}")

if __name__ == "__main__":
    run_eternal_watch()
