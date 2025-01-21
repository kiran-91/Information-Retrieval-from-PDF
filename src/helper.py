import os
import logging
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_groq import ChatGroq
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv

load_dotenv()
os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        try:
            pdf_reader = PdfReader(pdf)
            for page in pdf_reader.pages:
                text += page.extract_text()
        except Exception as e:
            logger.error(f"Error reading {pdf}: {e}")
    return text

def get_text_chunks(text, chunk_size=1000, chunk_overlap=20):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks, model_name="all-MiniLM-L6-v2"):
    try:
        embeddings = HuggingFaceEmbeddings(model_name=model_name)
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        return vector_store
    except Exception as e:
        logger.error(f"Error creating vector store: {e}")
        return None

def get_coversational_chain(vector_store):
    try:
        llm = ChatGroq(api_key=GROQ_API_KEY, model_name="Gemma2-9b-It")
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, retriever=vector_store.as_retriever(), memory=memory)
        return conversation_chain
    except Exception as e:
        logger.error(f"Error creating conversational chain: {e}")
        return None
