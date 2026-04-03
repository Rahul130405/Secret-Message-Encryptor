# Secret Message Encryptor

A Python-based GUI application for encrypting and decrypting messages using custom substitution and swap ciphers, featuring AI-assisted cryptanalysis.

## Features

- **Custom Encryption:** Combines character swapping with an AI-generated substitution map and shift cipher.
- **AI Decrypt Assistant:** Integrates with the Groq API (using Llama models) to attempt cryptanalysis on encrypted strings.
- **Key Storage:** Automatically manages encryption keys and character mapping in `secret_key.json`.
- **QR Code Support:** (In development/Integrated) Capability to handle encrypted data via QR codes.
- **User-Friendly GUI:** Built with `tkinter` for a simple, interactive experience.

## Prerequisites

- Python 3.10+
- **Groq API Key:** For AI-powered decryption to work, you must set the `GROQ_API_KEY` environment variable.
  - **Windows (PowerShell):** `$env:GROQ_API_KEY="your_key_here"`
  - **Linux/macOS:** `export GROQ_API_KEY="your_key_here"`

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd GUI
   ```

2. **Set up a virtual environment:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**
   ```bash
   python main.py
   ```

2. **Encrypt a Message:**
   - Enter your plaintext in the input field.
   - Click "Encrypt". The encrypted text will appear, and the key will be saved locally.

3. **Decrypt a Message:**
   - Paste the encrypted text into the input field.
   - Click "Decrypt". The app will use the stored `secret_key.json` to revert the transformation.

4. **AI Guess:**
   - If you have an encrypted string but no key, click "AI Guess". The app will send the text to the Groq API to attempt a recovery of the original message.

## Project Structure

- `main.py`: The entry point and GUI logic.
- `crypto_engine.py`: Core encryption/decryption algorithms (swap and obfuscation).
- `ai_engine.py`: Groq API integration for AI-powered decryption guesses.
- `ai_key_generator.py`: Generates randomized shift and mapping keys.
- `key_storage.py`: Handles saving and loading keys from `secret_key.json`.

## Security Note

This project is intended for educational and personal use. While it uses multiple layers of obfuscation, it is not a replacement for industry-standard encryption like AES.
