from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

class review(TypedDict):
    
        title: Annotated[str, "Assign a title to the review based on the content of the review"]
        rating: Annotated[int, "Assign a rating to the review on a scale of 1 to 5, based on the sentiment you cath from the content of review"]
        summary: Annotated[str, "Give me the summary of the review based on its content , try to keep it small"]
        pros: Annotated[Optional[str], "List all the pros from the content of review"]
        cons: Annotated[Optional[str], "List all the cons from the content of review"]
        
    
structured_review = model.with_structured_output(review)
result = structured_review.invoke("""hardware ek no. hai , softeware thoda chuda hai tumhare phone aka baki design sexy hai , but camera thoda weak hai""")

print(result)
print(result["summary"])
print(result["rating"])
print(result["title"])
