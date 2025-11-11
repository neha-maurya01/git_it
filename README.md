# Chatbot Projects

This repository contains two chatbot-related projects:

## 1. Chetbot_Creation

A FastAPI-based chatbot application using Ollama for local LLM inference.

### Features
- Local language model integration via Ollama
- FastAPI backend with REST API
- HTML-based user interface
- Configurable chat engine
- API documentation included

### Project Structure
- **app.py** — FastAPI application entry point
- **chat_engine.py** — Core chatbot logic
- **ollama_service.py** — Ollama LLM integration
- **config.py** — Configuration settings
- **user_interface.html** — Frontend UI
- **requirements.txt** — Python dependencies
- **api documentation.txt** — API reference
- **README.md** — Project-specific documentation

### Setup & Run

1. Install dependencies:
```bash
cd Chetbot_Creation
pip install -r requirements.txt
```

2. Ensure Ollama is running locally on port 11434

3. Start the FastAPI server:
```bash
python app.py
```

4. Open `user_interface.html` in a browser or visit `http://localhost:8000`

---

## 2. Adversarial Attacks

Research notebook on adversarial attacks against chatbots and language models.

### Contents
- **Neha_Maurya.ipynb** — Jupyter notebook with analysis and experiments

### Run the Notebook
```bash
cd "Adversarial Attacks"
jupyter notebook Neha_Maurya.ipynb
```

---

## Repository Structure
```
chatbot/
├── Chetbot_Creation/
│   ├── app.py
│   ├── chat_engine.py
│   ├── ollama_service.py
│   ├── config.py
│   ├── user_interface.html
│   ├── requirements.txt
│   └── README.md
├── Adversarial Attacks/
│   └── Neha_Maurya.ipynb
└── README.md (this file)
```

---

## Requirements
- Python 3.8+
- Ollama (for Chetbot_Creation)
- FastAPI, Uvicorn (see `Chetbot_Creation/requirements.txt`)
- Jupyter (for Adversarial Attacks notebook)

## License
See individual project documentation for license details.