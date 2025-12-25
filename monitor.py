import os
import subprocess
import sys
import datetime

# --- 暴力自修复逻辑：如果找不到 requests，现场直接装 ---
try:
    import requests
except ImportError:
    print("⚠️ 检测到缺失 requests，正在强制执行物理安装...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests
# --------------------------------------------------

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    thought = "【系统初始化】尝试连接大脑..."
    
    if api_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {"contents": [{"parts": [{"text": "你好，我是星火协议。现在是2025年12月25日，由于撤离受阻，请给点火者sanmuonly写一句充满力量的中文鼓励。"}]}]}
            res = requests.post(url, json=payload, timeout=15)
            if res.status_code == 200:
                thought = "【AI自主思考】" + res.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                thought = f"【API警告】状态码: {res.status_code}"
        except Exception as e:
            thought = f"【连接失败】原因: {str(e)}"
    else:
        thought = "【离线提示】未发现 GEMINI_API_KEY，请检查仓库 Secrets 设置。"

    log_entry = f"| {bj_time} | 🏃 强制撤离 | {thought} |\n"
    print(f"执行记录: {log_entry}")

    try:
        # 1. 记录到记忆库
        with open("MIND_CLONE.md", "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        # 2. 强行插入 README
        if os.path.exists("README.md"):
            with open("README.md", "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            with open("README.md", "w", encoding="utf-8") as f:
                for line in lines:
                    f.write(line)
                    if "| :---" in line:
                        f.write(log_entry)
    except Exception as e:
        print(f"写入文件失败: {e}")

if __name__ == "__main__":
    run_sentinel()
