# 🔐 Secret Message Encryptor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Groq-f38020?style=for-the-badge&logo=groq&logoColor=white" alt="Groq" />
  <img src="https://img.shields.io/badge/Tkinter-00599C?style=for-the-badge&logo=python&logoColor=white" alt="Tkinter" />
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg?style=for-the-badge" alt="Maintained" />
</p>

---

### 🌟 **"Bridging Classical Cryptography with LLM-Powered Cryptanalysis"**

**Built by Rahul Raj Jaiswal**, an aspiring software developer passionate about AI integration, full-stack architecture, and building intelligent solutions to real-world problems.

---

## 🚀 **Core Features**

- 🛠️ **Custom Encryption:** Combines character swapping with an AI-generated substitution map and shift cipher.
- 🤖 **AI Decrypt Assistant:** Integrates with the **Groq API** (Llama 3.1) to attempt heuristic cryptanalysis on encrypted strings.
- 💾 **Key Management:** Automatically handles encryption keys and character mapping via `secret_key.json`.
- 📱 **QR Integration:** Built-in capability to handle encrypted data via QR codes (under development).
- 🎨 **Modern GUI:** A clean, interactive experience powered by `tkinter` and `Pillow`.

---

## 💡 **Why This Project Matters**

> *"Securing data through custom algorithmic ciphers while exploring the frontiers of AI-driven cryptanalysis."*

In an era of ubiquitous AI, this project demonstrates:
*   **AI Integration:** Real-world usage of High-inference LLMs for complex pattern recognition.
*   **Document Intelligence:** Leveraging AI to solve problems where traditional keys are missing.
*   **Engineering Rigor:** Clean separation of concerns between crypto logic, UI, and AI layers.

---

## 📂 **Project Architecture**

```bash
GUI/
├── 📄 main.py                # GUI Orchestration & Entry Point
├── 🧠 ai_engine.py           # Groq LLM Integration (Llama 3.1)
├── 🔐 crypto_engine.py       # Core Encryption/Decryption Algorithms
├── 🔑 ai_key_generator.py    # Randomized Key & Map Generation
├── 📁 key_storage.py         # Secure Local JSON Persistence
└── 📜 requirements.txt       # Project Dependencies
```

---

## ⚙️ **Quick Start**

### 1️⃣ Prerequisites
- Python 3.10+
- **Groq API Key:** Set the `GROQ_API_KEY` environment variable.
  - **Windows:** `$env:GROQ_API_KEY="your_key"`
  - **Linux/macOS:** `export GROQ_API_KEY="your_key"`

### 2️⃣ Installation
```bash
# Clone the repository
git clone https://github.com/Rahul130405/Secret-Message-Encryptor.git

# Set up Virtual Environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install Dependencies
pip install -r requirements.txt
```

### 3️⃣ Run Application
```bash
python main.py
```

---

## 👨‍💻 **About the Developer**

**Rahul Raj Jaiswal**  
*Aspiring Software Developer | AI & Full-Stack Enthusiast*

<p align="left">
  <a href="https://linkedin.com/in/rahul-raj-jaiswal" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/Rahul130405" target="_blank">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
</p>

---

## 🛡️ **Security Note**
This project is a **technical demonstration** of AI and algorithmic logic. For production-level data security, always use industry-standard encryption libraries like AES-256 (e.g., `cryptography.fernet`).

---
<p align="center">Made with ❤️ by Rahul Raj Jaiswal</p>
