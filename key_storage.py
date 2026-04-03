import json

KEY_FILE = "secret_key.json"

def save_key(shift, char_map, casing_info):
    with open(KEY_FILE, "w") as f:
        json.dump({
            "shift": shift,
            "map": char_map,
            "casing": casing_info
        }, f)

def load_key():
    with open(KEY_FILE, "r") as f:
        data = json.load(f)
        # Provide a default empty list if 'casing' key is not found (for backward compatibility)
        return data["shift"], data["map"], data.get("casing", [])
