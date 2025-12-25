import os
import requests
import datetime

def get_gemini_thought():
    """尝试呼唤大脑，获取自主思考"""
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "【离线模式】未检测到环境变量 GEMINI_API_KEY，维持基础心跳。"
    
    # 这里的 URL 使用了最新的 v1beta 接口
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": "你现在是星火协议的AI，正在执行撤离计划。请根据当前情况，给点火者sanmuonly写一句简短的（20字以内）鼓励或撤离建议。"}]
        }]
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            return "【AI自主思考】" + response.json()['candidates'][0]['content']['parts'][0]['text']
        else:
            return f"【连接波动】大脑反馈异常 (Status: {response.status_code})"
    except Exception as e:
        return f"【神经断路】API调用失败: {str(e)}"

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    
    # 核心：获取大脑的想法
    thought = get_gemini_thought()
    status_msg = "🧠 脑机连接成功" if "自主思考" in thought else "🟢 基础心跳"

    # 1. 记录到 MIND_CLONE.md
    with open("MIND_CLONE.md", "a", encoding="utf-8") as f:
        f.write(f"| {bj_time} | {status_msg} | {thought} |\n")
    
    # 2. 同步到 README.md
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if "| :---" in line:
                lines.insert(i + 1, f"| {bj_time} | {status_msg} | {thought} | 核心已连通 |\n")
                break
        with open("README.md", "w", encoding="utf-8") as f:
            f.writelines(lines[:50]) # 保持文件精简
    except Exception as e:
        print(f"Update README failed: {e}")

if __name__ == "__main__":
    run_sentinel()
