from langchain_openai import ChatOpenAI
from typing import TypedDict
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class review(TypedDict):
    
        title: str
        rating: int
        summary: str
    
    
structured_review = model.with_structured_output(review)
result = structured_review.invoke("""hardware ek no. hai , softeware thoda chuda hai tumhare phone aka baki design sexy hai , but camera thoda weak hai""")

print(result)
print(result["summary"])
print(result["rating"])
print(result["title"])
