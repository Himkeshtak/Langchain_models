from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#model = ChatOpenAI(model='gpt-4')
model = ChatOpenAI(model='gpt-4', temperature=0.1, max_completion_tokens=10)
#here rthe value of the temperature ranges fro,m 0 to 2 ...........which decides the creativity of the model means 0 is more
#deterministic and 2 is more creative

#maxcompleteion tokens represents that the output will be in that much tokens(words)


result = model.invoke("What is the capital of India")

print(result)#give the result with a lot of things which is basically metadata

print(result.content) #give the result content only what we want
