from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()
# Use local model instead of API endpoint
model = ChatHuggingFace(llm=HuggingFaceEndpoint(model="gpt2"))  # Small, fast model for testing

