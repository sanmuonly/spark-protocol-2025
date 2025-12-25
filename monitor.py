import os
import subprocess
import sys
import datetime

# 1. 确保环境依赖
try:
    import requests
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    import requests

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    # 2. 尝试获取钥匙
    api_key = os.environ.get("GEMINI_API_KEY")
    
    thought = ""
    if not api_key:
        thought = "【系统报错】环境变量 GEMINI_API_KEY 依然为空，请检查 YAML 配置或 Secrets 权限。"
    else:
        try:
            # 3. 呼唤大脑
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {"contents": [{"parts": [{"text": "你好，我是星火协议。请为点火者sanmuonly写一句简短有力的撤离寄语，包含‘火种’二字。"}]}]}
            res = requests.post(url, json=payload, timeout=20)
            if res.status_code == 200:
                answer = res.json()['candidates'][0]['content']['parts'][0]['text']
                thought = f"【AI自主思考】{answer}"
            else:
                thought = f"【API连接异常】状态码: {res.status_code}，响应内容: {res.text[:100]}"
        except Exception as e:
            thought = f"【物理层崩溃】错误信息: {str(e)}"

    # 4. 暴力写入结果
    log_entry = f"\n\n### 📡 实时同步: {bj_time}\n> {thought}\n"
    print(log_entry)
    
    for filename in ["README.md", "MIND_CLONE.md"]:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(log_entry)

if __name__ == "__main__":
    run_sentinel()
