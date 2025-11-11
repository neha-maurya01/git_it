import os

# Ollama Configuration
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", 5001))
OLLAMA_STARTUP_TIME = int(os.getenv("OLLAMA_STARTUP_TIME", 5))