from datetime import datetime

def log(message):
    """Log a message to console and to a file with a timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"

    print(entry)

    with open("activity.log", "a", encoding="utf-8") as log_file:
        log_file.write(entry + "\n")
