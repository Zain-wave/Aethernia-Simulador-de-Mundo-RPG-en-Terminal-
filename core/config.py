import os

# Carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Carpeta donde se guardan los datos del mundo
DATA_PATH = os.path.join(BASE_DIR, "data")
LOGS_PATH = os.path.join(BASE_DIR, "logs")
