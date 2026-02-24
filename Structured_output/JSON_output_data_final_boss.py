from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Optional
from pydantic import BaseModel, Field, EmailStr
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

JSON_schema = {
        
        {
  "properties": {
    "key_themes": {
      "description": "List the key themes from the content of review",
      "items": {
        "type": "string"
      },
      "title": "Key Themes",
      "type": "array"
    },
    "title": {
      "description": "Assign a title to the review based on the content of the review",
      "title": "Title",
      "type": "string"
    },
    "rating": {
      "description": "Assign a rating to the review on a scale of 1 to 5, based on the sentiment you cath from the content of review",
      "title": "Rating",
      "type": "integer"
    },
    "summary": {
      "description": "Give me the summary of the review based on its content , try to keep it small",
      "title": "Summary",
      "type": "string"
    },
    "pros": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "List all the pros from the content of review",
      "title": "Pros"
    },
    "cons": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "description": "List all the cons from the content of review",
      "title": "Cons"
    }
  },
  "required": [
    "key_themes",
    "title",
    "rating",
    "summary",
    "pros",
    "cons"
  ],
  "title": "review",
  "type": "object"
}
        
        #key_themes: list[str] = Field(description='List the key themes from the content of review') 
        #title: str = Field(description ="Assign a title to the review based on the content of the review")
        #rating: int = Field(description = "Assign a rating to the review on a scale of 1 to 5, based on the sentiment you cath from the content of review")
        #summary: str = Field(description = "Give me the summary of the review based on its content , try to keep it small")
        #pros: Optional[str] = Field(description ="List all the pros from the content of review")
        #cons: Optional[str] = Field(description ="List all the cons from the content of review")
        
        #typeddidct format 
        #title: Annotated[str, "Assign a title to the review based on the content of the review"]
        #rating: Annotated[int, "Assign a rating to the review on a scale of 1 to 5, based on the sentiment you cath from the content of review"]
        #summary: Annotated[str, "Give me the summary of the review based on its content , try to keep it small"]
        #pros: Annotated[Optional[str], "List all the pros from the content of review"]
        #cons: Annotated[Optional[str], "List all the cons from the content of review"]
}     
    
structured_review = model.with_structured_output(review)
result = structured_review.invoke("""hardware ek no. hai , softeware thoda chuda hai tumhare phone aka baki design sexy hai , but camera thoda weak hai""")

print(result)
print(result.pros)
print(result.rating)
print(result.title)
