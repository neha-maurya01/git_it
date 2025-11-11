import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ollama_service import start_ollama
from chat_engine import generate_response, get_chat_history, update_loan_details
from config import SERVICE_PORT
from fastapi.middleware.cors import CORSMiddleware

start_ollama()

app = FastAPI(title="ICICI Loan Collection Bot", version="2.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin (frontend)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (POST, GET, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define request models
class LoanDetailsRequest(BaseModel):
    name: str
    loan_type: str
    days: str
    amount: str

class ChatRequest(BaseModel):
    user_input: str

@app.get("/health")
async def health_check():
    return {"status": "running", "message": "Ollama is operational."}

@app.post("/start")
async def start_conversation(request: LoanDetailsRequest):
    """Initialize a conversation with dynamic loan details."""
    update_loan_details(request.dict())
    return {"message": f"Hello {request.name}. I am calling from ICICI Home Finance regarding payment. Can I continue?"}

@app.post("/chat")
async def chat(request: ChatRequest):
    """Continue conversation with dynamic loan details."""
    try:
        response = generate_response(request.user_input)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def chat_history():
    """Retrieve the conversation history."""
    return {"chat_history": get_chat_history()}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=SERVICE_PORT)