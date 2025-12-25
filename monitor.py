import os
import subprocess
import sys
import datetime

# --- 环境自愈 ---
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if api_key and len(api_key) > 10:
        try:
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {"contents": [{"parts": [{"text": "你好，我是星火协议AI。请为点火者sanmuonly写一句简短有力的撤离寄语，必须包含‘火种’二字。"}]}]}
            res = requests.post(url, json=payload, timeout=15)
            if res.status_code == 200:
                answer = res.json()['candidates'][0]['content']['parts'][0]['text']
                thought = f"【AI自主思考】{answer}"
            else:
                thought = f"【API状态异常】代码: {res.status_code}"
        except Exception as e:
            thought = f"【连接崩溃】{str(e)}"
    else:
        thought = "【环境异常】未检测到有效的 GEMINI_API_KEY，请检查 Secrets 设置。"

    log_entry = f"\n\n### ⚡ 实时同步: {bj_time}\n> {thought}\n"
    print(log_entry)

    # 暴力写入：直接追加到文件末尾
    for filename in ["README.md", "MIND_CLONE.md"]:
        try:
            with open(filename, "a", encoding="utf-8") as f:
                f.write(log_entry)
        except:
            pass

if __name__ == "__main__":
    run_sentinel()
