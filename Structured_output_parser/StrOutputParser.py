from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="TinyLlama/TinyLLama-1.1B-Chat-v0.4-GGUF",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm )
