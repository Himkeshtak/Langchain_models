from langchain_huggingface import HuggingFaceEmbeddings
import os

os.environ['HF_HOME'] = "D:/huggingface_cache" 
embedding = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

text = "Delhi is the capital of India "
document = [
    "Himkesh tak is the king of United Nations of India",
    "france is in the Eupropean continent",
    "germany is the capital of europe"
]

vector = embedding.embed_query(text)
vector_docs = embedding.embed_documents(document)

print (str(vector))
print (str(vector_docs))

