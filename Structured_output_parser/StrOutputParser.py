from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Use Google Gemma model via HuggingFace Inference API
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2b-it",  # Google Gemma 2B instruction-tuned model
    task="text-generation",
    temperature=0.7,
    max_new_tokens=200,
)

model = llm

#prompt 1 -> detailed description of content
template1 = PromptTemplate(
    template = "Give the detailed description of the {topic}",
    input_variables = ["topic"]
)
#prompt 2 -> summary
template2 = PromptTemplate(
    template = "Give me the summary of the {text} in 20 words",
    input_variables = ["text"]
)

prompt1 = template1.invoke({"topic": "Maharana Pratap"})

result = model.invoke(prompt1)

prompt2 = template2.invoke({"text": result})

result2 = model.invoke(prompt2)

print("Detailed description:")
print(result)
print("\nSummary:")
print(result2)
