from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from dotenv import load_dotenv
from openai import OpenAI


from langchain_qdrant import QdrantVectorStore
from langchain_community.document_loaders import PyPDFLoader
load_dotenv()


openai_client = OpenAI(
    api_key=os.getenv("GOOGLE_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001",  # ✅ New correct name
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    request_per_minute=50 
)

vector_db=QdrantVectorStore.from_existing_collection(
            url="http://localhost:6333",
            embedding=embedding_model,
            collection_name="learning_rag"

)

# Take user input 
user_query=input("Ask something:")

# Relevant chunks from the vector db
search_result = vector_db.similarity_search(query=user_query)

Context = "\n\n\n".join([f"Page Content: {result.page_content}\nPage Number:{result.metadata['page_label']}\nFile Location: {result.metadata['source']}"
for result in search_result])

SYSTEM_PROMPT=f"""

You are a helpfull AI Assistant who answeres user query based on the available context retrieved from a PDF file along with page_contents and page number.
You should only ans the user based on the following context and navigate the user to open the right page number to know more 

Context:
{Context}

"""
response = openai_client.chat.completions.create(
           model="gemini-2.5-flash",
           messages=[
               { "role": "system", "content": SYSTEM_PROMPT },
               { "role": "user", "content":user_query },])

print(f"🤖:{response.choices[0].message.content}")