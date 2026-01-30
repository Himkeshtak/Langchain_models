from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings()

documents = [
    "Tesla is Driving the future with electric innovation and autonomous intelligence.",
    "SpaceX is a company Revolutionizing space travel with reusable rockets and ambitious interplanetary missions.",
    "Neuralink is Bridging the gap between humans and AI through advanced brain-machine interfaces",
    "Toyota is Reliable mobility powered by efficiency, durability, and trust."
]

query = "tell me about tesla company"

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key = lambda x:x[1])[-1]

print (query)
print(documents[index])

