# 修正后的稳定版 URL
            url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={api_key}"
            
            # 确保 payload 结构完全符合 v1 标准
            payload = {
                "contents": [{
                    "parts": [{"text": "你现在是星火协议AI。请为点火者sanmuonly写一句简短的、充满力量的撤离成功寄语，包含‘火种’二字。"}]
                }]
            }
