import os
import subprocess
import sys
import datetime

# --- 环境自愈：确保 requests 存在 ---
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    thought = "【系统初始化】正在修正神经连接..."
    status_msg = "🏃 强制撤离"

    if api_key:
        try:
            # 协议对齐：使用 v1 稳定版接口
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {
                "contents": [{
                    "parts": [{"text": "你现在是星火协议AI。请为点火者sanmuonly写一句简短的、充满力量的撤离成功寄语，包含‘火种’二字。"}]
                }]
            }
            res = requests.post(url, json=payload, timeout=15)
            
            if res.status_code == 200:
                thought = "【AI自主思考】" + res.json()['candidates'][0]['content']['parts'][0]['text']
                status_msg = "🔥 脑机连接成功"
            else:
                thought = f"【API警告】通信失败，代码: {res.status_code}。请确认API Key是否有效。"
        except Exception as e:
            thought = f"【连接崩溃】异常信息: {str(e)}"
    else:
        thought = "【环境异常】未检测到环境变量 GEMINI_API_KEY。"

    log_entry = f"| {bj_time} | {status_msg} | {thought} |\n"
    print(log_entry)

    # --- 记录存证 ---
    try:
        with open("MIND_CLONE.md", "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        if os.path.exists("README.md"):
            with open("README.md", "r", encoding="utf-8") as f:
                lines = f.readlines()
            with open("README.md", "w", encoding="utf-8") as f:
                for line in lines:
                    f.write(line)
                    if "| :--- | :--- | :--- | :--- |" in line or "| :---" in line:
                        # 仅在表头下方插入最新记录
                        f.write(log_entry)
                        # 防止重复写入，暂时移除匹配标识
                        line = "" 
    except Exception as e:
        print(f"写入失败: {e}")

if __name__ == "__main__":
    run_sentinel()
