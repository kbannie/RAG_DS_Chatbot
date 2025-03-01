from llm import get_retriever
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large')
retriever = get_retriever()
test_query = "자연과학소가 뭐야?"
retrieved_docs = retriever.invoke(test_query)

print("검색된 문서:", retrieved_docs)

from llm import get_rag_chain

rag_chain = get_rag_chain()
print(rag_chain)