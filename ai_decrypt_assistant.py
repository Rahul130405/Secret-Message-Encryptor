from key_storage import load_key
from crypto_engine import deobfuscate

def ai_decryption_assistant(text):
    try:
        shift, char_map = load_key()
        reverse_map = {v: k for k, v in char_map.items()}
        decrypted_text = deobfuscate(text, shift, reverse_map)
        return f"Decrypted message: {decrypted_text}"
    except Exception as e:
        print(e)
        return "Could not decrypt the message. Is the key file present?"