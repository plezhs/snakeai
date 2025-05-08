def log(m, location, time):                             #m = 메세지, location = py파일 이름, time = 로그 시간
    with open(f"./data/logs/{time}.log", "a") as f:
        f.write(f"[{time}] {location} - {m}\n")

def log_error(m, location, time):                       #m = 메세지, location = py파일 이름, time = 로그 시간
    with open(f"./data/logs/errors/{time}.log", "a") as f:
        f.write(f"[{time}] {location} - {m}\n")