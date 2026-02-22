# 🎙️ Gemini Voice Assistant (VoiceChat-Bot)

A low-latency, multimodal AI voice assistant optimized for macOS (Apple Silicon). Built on your MacBook Air M4 using Google's Gemini 1.5 Flash and ElevenLabs synthesis.

## 🚀 Key Features
* **Stateful Memory**: Tracks conversation history for contextual dialogue.
* **Modern SDK**: Built with the 2026 `google-genai` SDK and stable v1 endpoints.
* **Low Latency**: Uses streaming audio for real-time vocal responses.

## 🛠️ Installation
1. Clone the repo.
2. Setup environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Add your API keys to a `.env` file.

## 🖥️ Usage
```bash
python main.py
```
