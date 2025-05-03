def log(m, location, time):
    with open(f"./data/logs/{time}.log", "a") as f:
        f.write(f"[{time}] {location} - {m}\n")

def log_error(m, location, time):
    with open(f"./data/logs/errors/{time}.log", "a") as f:
        f.write(f"[{time}] {location} - {m}\n")