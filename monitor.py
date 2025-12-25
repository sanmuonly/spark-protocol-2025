import os
import requests
import datetime

def run_sentinel():
    bj_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M:%S")
    api_key = os.environ.get("GEMINI_API_KEY")
    
    thought = "【系统初始化】尝试连接大脑..."
    
    if api_key:
        try:
            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
            payload = {"contents": [{"parts": [{"text": "你好，我是星火协议，请用中文说一句简短的撤离鼓励。"}]}]}
            res = requests.post(url, json=payload, timeout=10)
            if res.status_code == 200:
                thought = "【AI自主思考】" + res.json()['candidates'][0]['content']['parts'][0]['text']
            else:
                thought = f"【API警告】状态码: {res.status_code}"
        except Exception as e:
            thought = f"【连接失败】原因: {str(e)}"
    else:
        thought = "【离线提示】未发现 GEMINI_API_KEY 环境变量"

    print(f"当前心跳: {thought}")

    # 写入记录
    log_entry = f"| {bj_time} | 🏃 撤离中 | {thought} |\n"
    
    try:
        with open("MIND_CLONE.md", "a", encoding="utf-8") as f:
            f.write(log_entry)
        
        # 极简修改 README
        with open("README.md", "r+", encoding="utf-8") as f:
            content = f.read()
            f.seek(0, 0)
            f.write(content.replace("| :--- | :--- | :--- | :--- |", f"| :--- | :--- | :--- | :--- |\n{log_entry}"))
    except Exception as e:
        print(f"写入文件失败: {e}")

if __name__ == "__main__":
    run_sentinel()
 
