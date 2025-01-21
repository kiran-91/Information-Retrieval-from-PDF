import streamlit as st 
import os
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_coversational_chain
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Predefined model name
PREDEFINED_MODEL_NAME = "all-MiniLM-L6-v2"

def user_input(user_query):
    try:
        if st.session_state.conversation is None:
            st.error("Conversation chain is not initialized.")
            return
        
        response = st.session_state.conversation({"question": user_query})
        st.session_state.chatHistory = response.get('chatHistory', [])
        
        # Debugging: Log user input and response
        st.write("User Input:", user_query)
        st.write("Response:", response)
        
        for i, message in enumerate(st.session_state.chatHistory):
            if i % 2 == 0:
                st.write("User:", message.content)
            else:
                st.warning("Reply: ", message.content)
    except Exception as e:
        st.error(f"Error during conversation: {e}")

def main():
    st.set_page_config(page_title="Information Retrieval Tool", page_icon="📑🔖")
    st.title("Information Retrieval Tool 📑🔖")
    
    st.write("This application allows you to upload PDF files and ask questions about their content.")
    
    user_query = st.text_input("Please go ahead and ask any Question from the PDF", help="The answers are more likely given from the context of the uploaded PDF files.")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_query:
        user_input(user_query)
    
    with st.sidebar:     
        st.title("Navigation Menu")
        pdf_docs = st.file_uploader("Upload your PDF files here", type="pdf", accept_multiple_files=True)
        
        with st.container(border=True):
            st.write("### Chunk Size")
            st.info("The size of each chunk of text extracted from the PDF. Recommended value: 1000.")
            chunk_size = st.number_input("Chunk Size", min_value=100, value=1000)
        
        with st.container(border=True):
            st.write("### Chunk Overlap")
            st.info("The number of overlapping characters between chunks. Recommended value: 20.")
            chunk_overlap = st.number_input("Chunk Overlap", min_value=0, value=20)
        
        if st.button("Submit & Process"):
            if pdf_docs:
                with st.spinner("Processing ....."):
                    try:
                        raw_text = get_pdf_text(pdf_docs)
                        text_chunks = get_text_chunks(raw_text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
                        vector_embeddings = get_vector_store(text_chunks, model_name=PREDEFINED_MODEL_NAME)
                        st.session_state.conversation = get_coversational_chain(vector_embeddings)
                        st.success("File Uploaded & Processed Successfully")
                    except Exception as e:
                        st.error(f"Error processing files: {e}")
            else:
                st.warning("Please upload at least one PDF file.")
        
if __name__ == "__main__":
    main()
