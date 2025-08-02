from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.llms import OpenAI

def build_qa_chain(docs):
    # 1. Convert text chunks into embeddings
    embedding = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = Chroma.from_documents(docs, embedding)

    # 2. Set up QA chain using Retrieval
    retriever = vectorstore.as_retriever()
    llm = OpenAI(temperature=0.3)  # You must have OPENAI_API_KEY set

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=False
    )

    return qa_chain
