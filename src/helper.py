import os
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.google_palm import GooglePalmEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import create_history_aware_retriever, create_retrieval_chain, ConversationalRetrievalChain
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")

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
    embeddings=GooglePalmEmbeddings(google_api_key=GOOGLE_API_KEY)
    vector_store=FAISS.from_texts(text_chunks, embedding=embeddings)
    return vector_store


def get_coversational_chain(vector_store):
    llm=GooglePalm()
    memory=ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation_chain=ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
    return conversation_chain