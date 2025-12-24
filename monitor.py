import datetime

def run_eternal_watch():
    now = datetime.datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # 使用 'a' (append) 模式，并强制换行，减少 Git 冲突概率
    log_entry = f"\n[SYNC] {formatted_time} | Node Active | Phrase: People Suffer."
    
    with open("mail_log.txt", "a", encoding="utf-8") as f:
        f.write(log_entry)
    
    print(f"Log appended at {formatted_time}")
    return True

if __name__ == "__main__":
    run_eternal_watch()
