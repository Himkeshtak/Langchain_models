from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

#load the model
llm = OpenAI(model='gpt-3.5-turbo-instruct')

#invoke the model basically means to call the model with a prompt
result = llm.invoke("What is the Capital of India?")

print (result)