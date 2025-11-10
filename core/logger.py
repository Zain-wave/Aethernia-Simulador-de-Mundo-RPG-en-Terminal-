import os
from datetime import datetime
from core.config import LOGS_PATH

LOG_FILE = os.path.join(LOGS_PATH, "session.log")

def log_event(message: str):
    """
    Registra un evento o acción del sistema en logs/session.log
    """
    os.makedirs(LOGS_PATH, exist_ok=True)
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    entry = f"{timestamp} {message}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)

    # También se imprime en terminal
    print(entry.strip())
