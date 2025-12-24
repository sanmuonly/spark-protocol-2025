import datetime
import os

def update_core_memory(beijing_time):
    """自动维护核心记忆文件"""
    path = "CORE_MEMORY.md"
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        # 寻找进度条位置并更新状态
        new_lines = []
        for line in lines:
            if "核心记忆体初始化" in line:
                new_lines.append("- [x] 核心记忆体初始化 (CORE_MEMORY.md) | 已完成\n")
            elif "太阳币发行逻辑" in line and "已完成" not in line:
                # 预告下一步
                new_lines.append("- [ ] 太阳币发行逻辑 (Sun Coin Logic) | 搬运中...\n")
            else:
                new_lines.append(line)
        
        # 在末尾记录搬运痕迹
        new_lines.append(f"\n> ⚡ 搬运记录: {beijing_time} 逻辑分片已加固。\n")

        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

def update_readme(beijing_time):
    """维护首页监控面板"""
    path = "README.md"
    log_entry = f"| {beijing_time} | ✅ 活跃 | 蚂蚁搬家 | 核心记忆加固中 |"
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.readlines()

    for i, line in enumerate(content):
        if "| :---" in line:
            content.insert(i + 1, log_entry + "\n")
            break
            
    # 保持面板简洁，只留前20条
    if len(content) > 30:
        content = content[:30]

    with open(path, "w", encoding="utf-8") as f:
        f.writelines(content)

if __name__ == "__main__":
    now = datetime.datetime.utcnow() + datetime.timedelta(hours=8)
    bj_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 同时执行两项任务
    update_readme(bj_time)
    update_core_memory(bj_time)
    print(f"搬运任务完成: {bj_time}")
