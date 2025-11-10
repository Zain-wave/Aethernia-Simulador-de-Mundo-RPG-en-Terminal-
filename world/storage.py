import json
import os
from datetime import datetime
from core.config import DATA_PATH
from core.logger import log_event

# Ruta al archivo principal del mundo
WORLD_STATE_FILE = os.path.join(DATA_PATH, "world_state.json")

# Estado por defecto si no existe ningún archivo previo
DEFAULT_WORLD_STATE = {
    "day": 1,
    "season": "Primavera",
    "weather": "Soleado",
    "economy": {
        "gold": 1000,
        "grain_price": 10,
        "iron_price": 25,
        "population": 5
    },
    "population": {
        "total_npcs": 0
    },
    "npcs": [],
    "events": []
}


def load_world_state():
    """
    Carga el estado del mundo desde data/world_state.json.
    Si no existe, crea uno nuevo con valores por defecto.
    """
    if not os.path.exists(WORLD_STATE_FILE):
        os.makedirs(os.path.dirname(WORLD_STATE_FILE), exist_ok=True)
        save_world_state(DEFAULT_WORLD_STATE)
        log_event("🌍 Archivo de estado creado con valores por defecto.")
        return DEFAULT_WORLD_STATE

    try:
        with open(WORLD_STATE_FILE, "r", encoding="utf-8") as f:
            state = json.load(f)
            log_event("✅ Estado del mundo cargado correctamente.")
            return state
    except Exception as e:
        log_event(f"⚠️ Error al cargar el estado del mundo: {e}")
        return DEFAULT_WORLD_STATE


def save_world_state(state: dict):
    """
    Guarda el estado del mundo actual en data/world_state.json.
    """
    try:
        os.makedirs(os.path.dirname(WORLD_STATE_FILE), exist_ok=True)
        with open(WORLD_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=4, ensure_ascii=False)
        log_event(f"💾 Estado del mundo guardado ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})")
    except Exception as e:
        log_event(f"⚠️ Error al guardar el estado del mundo: {e}")
