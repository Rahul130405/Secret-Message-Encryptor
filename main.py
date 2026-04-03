import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image

from crypto_engine import swap_letters, obfuscate, deobfuscate
from ai_key_generator import generate_ai_key
from key_storage import save_key, load_key

from ai_engine import ai_guess_decryption

encrypted_text = ""

def ai_guess_decrypt_message():
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message for the AI to guess.")
        return
    
    try:
        result = ai_guess_decryption(message)
        messagebox.showinfo("AI Guess", result)
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "AI Guessing failed. Please check your OpenAI API key and internet connection.")

# --- Button Functions ---
def encrypt_message():
    global encrypted_text
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message to encrypt.")
        return
    
    casing_info = [char.isupper() for char in message]
    shift, char_map = generate_ai_key()
    save_key(shift, char_map, casing_info) # Pass casing_info
    
    swapped = swap_letters(message)
    encrypted_text = obfuscate(swapped, shift, char_map)
    result_label.config(text="🔐 Encrypted: " + encrypted_text)

def decrypt_message():
    message = entry.get()
    if not message:
        messagebox.showwarning("Input Error", "Please enter a message to decrypt.")
        return
    try:
        shift, char_map, casing_info = load_key() # Receive casing_info
        reverse_map = {v: k for k, v in char_map.items()}
        
        deob = deobfuscate(message, shift, reverse_map)
        decrypted = swap_letters(deob)
        
        # Apply original casing
        final_decrypted = []
        for i, char in enumerate(decrypted):
            if i < len(casing_info) and casing_info[i]:
                final_decrypted.append(char.upper())
            else:
                final_decrypted.append(char)
        decrypted = "".join(final_decrypted)

        result_label.config(text="🔓 Decrypted: " + decrypted.rstrip('x'))
    except Exception as e:
        print(e)
        messagebox.showerror("Error", "Decryption failed. Input might be incorrect. Have you encrypted a message first?")

def clear_text():
    entry.delete(0, tk.END)
    result_label.config(text="")

def save_to_file():
    if not encrypted_text:
        messagebox.showwarning("No Data", "Please encrypt a message first.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, 'w') as f:
            f.write(encrypted_text)
        messagebox.showinfo("Saved", f"Encrypted message saved to {file_path}")

def export_qr():
    if not encrypted_text:
        messagebox.showwarning("No Data", "Please encrypt a message first.")
        return
    qr = qrcode.make(encrypted_text)
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Image", "*.png")])
    if file_path:
        qr.save(file_path)
        messagebox.showinfo("QR Code", f"QR code saved to {file_path}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🔏 Secret Message Encryptor/Decryptor")
root.geometry("1280x720")
root.configure(bg="#1e1e2f")
root.resizable(False, False)

frame = tk.Frame(root, bg="#1e1e2f")
frame.place(relx=0.5, rely=0.5, anchor='center')

title_label = tk.Label(frame, text="🕵️ Secret Message Tool", font=("Helvetica", 44, "bold"), fg="#ffffff", bg="#1e1e2f")
title_label.pack(pady=40)

entry = tk.Entry(frame, font=("Helvetica", 28), width=40, justify='center', bg="#f0f0f0", fg="#000")
entry.pack(pady=30)

# Buttons (Encrypt / Decrypt / Clear)
btn_frame = tk.Frame(frame, bg="#1e1e2f")
btn_frame.pack(pady=20)

encrypt_btn = tk.Button(btn_frame, text="Encrypt 🔐", command=encrypt_message, width=15, font=("Helvetica", 20), bg="#4caf50", fg="white")
encrypt_btn.grid(row=0, column=0, padx=25)

decrypt_btn = tk.Button(btn_frame, text="Decrypt 🔓", command=decrypt_message, width=15, font=("Helvetica", 20), bg="#2196f3", fg="white")
decrypt_btn.grid(row=0, column=1, padx=25)

clear_btn = tk.Button(btn_frame, text="Clear ❌", command=clear_text, width=15, font=("Helvetica", 20), bg="#f44336", fg="white")
clear_btn.grid(row=0, column=2, padx=25)

# Export Options (Save to file / QR)
export_frame = tk.Frame(frame, bg="#1e1e2f")
export_frame.pack(pady=30)

save_btn = tk.Button(export_frame, text="💾 Save to File", command=save_to_file, width=18, font=("Helvetica", 18), bg="#9c27b0", fg="white")
save_btn.grid(row=0, column=0, padx=20)

qr_btn = tk.Button(export_frame, text="📷 Export QR", command=export_qr, width=18, font=("Helvetica", 18), bg="#ff9800", fg="white")
qr_btn.grid(row=0, column=1, padx=20)

ai_guess_btn = tk.Button(export_frame, text="🤖 AI Guess Decryption", command=ai_guess_decrypt_message, width=25, font=("Helvetica", 18), bg="#673ab7", fg="white")
ai_guess_btn.grid(row=1, column=0, columnspan=2, pady=20)


# Output label
result_label = tk.Label(frame, text="", font=("Helvetica", 26, "italic"), fg="#ffcc00", bg="#1e1e2f", wraplength=1200, justify="center")
result_label.pack(pady=40)

root.mainloop()
