import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"]=os.getenv("HF_TOKEN")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")


def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_spitter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    chunks=text_spitter.split_text(text)
    return chunks
    
def get_vector_store(text_chunks):
    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vector_store=FAISS.from_texts(text_chunks, embeddings=embeddings)
    return vector_store


def get_coversational_chain(vector_store):
    llm=ChatGroq(api_key=GROQ_API_KEY, model_name="Gemma2-9b-It")
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain=ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain