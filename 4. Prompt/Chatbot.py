from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

load_dotenv()

# Use local model instead of API endpoint
model_name = "gpt2"  # Small, fast model for testing
tokenizer = AutoTokenizer.from_pretrained(model_name)
model_hf = AutoModelForCausalLM.from_pretrained(model_name)
pipe = pipeline("text-generation", model=model_hf, tokenizer=tokenizer, max_new_tokens=100)
llm = HuggingFacePipeline(pipeline=pipe)
model = ChatHuggingFace(llm=llm)

chat_history = []

while True:
    user_input = input("you: ")
    if user_input.lower() == 'exit':
        break
    try:
        result = model.invoke(user_input)
        # HuggingFace returns an AIMessage object with .content attribute
        ai_text = result.content if hasattr(result, 'content') else str(result)
        print("AI:", ai_text)
        chat_history.append({"user": user_input, "AI": ai_text})
    except Exception as e:
        import traceback
        print(f"Error: {type(e).__name__}: {e}")
        traceback.print_exc()

print("Chat History:", chat_history)