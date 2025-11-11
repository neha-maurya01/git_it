from langchain.memory import ConversationBufferMemory
from langchain_ollama.llms import OllamaLLM
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from config import OLLAMA_MODEL

memory = ConversationBufferMemory(memory_key="chat_history")
loan_details = {}  # Store dynamically received loan details

llm = OllamaLLM(model=OLLAMA_MODEL)

def update_loan_details(details: dict):
    global loan_details
    loan_details = details
    memory.clear() 

def generate_prompt():
    if not loan_details:
        return "No loan details provided. Please start a new session."

    loan_text = ", ".join(f"{key}: {value}" for key, value in loan_details.items())
    initial_query = f"Hello {loan_details['name']}. I am calling from ICICI Home Finance regarding payment. Can I continue?"

    template = f"""\
You are a professional loan collection agent for ICICI Bank. Start the conversation EXACTLY as follows:
{initial_query}

Customer details: {loan_text}

Guidelines for the conversation:

Dispute:
- Customer claims the loan does not belong to them or that it has been closed.
- Response: "Please contact your nearest branch or our customer care. Thank you."

Generic Yes:
- Customer expresses interest and requests the payment date.
- Response: "{loan_details['loan_type']} payment is pending for {loan_details['days']} days. You need to pay {loan_details['amount']}. When will you pay?"
- Once confirmed, conclude with a thank-you message.

Generic No:
- Customer declines the conversation.
- Politely persuade them at least 3 times.
- If still refusing, end the conversation.

Wrong Number:
- If the customer states it is the wrong number, apologize for the inconvenience.
- Wish them a good day.

Previous conversation:
{{chat_history}}

New human question: {{question}}

Ensure professional and empathetic communication. 
Avoid repeating statements already made. 
If a similar question was asked before, provide a slightly different answer or add more details.  

Response:
"""
    return PromptTemplate.from_template(template)

def generate_response(user_input: str) -> str:
    """Process user input and generate an AI response."""
    prompt = generate_prompt()
    if not prompt:
        return "Please provide loan details first."

    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        verbose=True,
        memory=memory,
    )
    response = conversation.run(question=user_input)
    memory.chat_memory.add_user_message(user_input)
    memory.chat_memory.add_ai_message(response)
    return response

def get_chat_history():
    """Retrieve chat history."""
    return memory.load_memory_variables({})["chat_history"]