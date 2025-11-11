import subprocess
import threading
import time
from config import OLLAMA_STARTUP_TIME

def run_ollama():
    """Start Ollama server in a separate thread."""
    subprocess.run(["ollama", "serve"], check=True)

def start_ollama():
    """Ensure Ollama is running before making requests."""
    ollama_thread = threading.Thread(target=run_ollama, daemon=True)
    ollama_thread.start()
    time.sleep(OLLAMA_STARTUP_TIME)  # Wait for Ollama to initialize