import streamlit as st 
from src.helper import get_pdf_text, get_text_chunks, get_vector_store, get_coversational_chain

def user_input(user_query):
    response=st.session_state.conversation({"Question":user_query})
    st.session_state.chatHistory=response['chatHistory']
    for i, message in enumerate(st.session_state.chatHistory):
        if i%2==0:
            st.write(f"User: ",message.content)
        else:
            st.warning("Reply: ",message.content)



def main():
    st.set_page_config(page_title="Information Retrieval Tool", page_icon="📑🔖")
    st.title("Information Retrieval Tool 📑🔖")
    
    user_query=st.text_input("Please go ahead and ask any Question from the PDF")
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_query:
        user_input(user_query)
    
    
    
    with st.sidebar:     
        st.title("Navigation Menu")
        pdf_docs=st.file_uploader("Upload your PDF files here", type="pdf", accept_multiple_files=True)
        
        if st.button("Submit & Process"):
            with st.spinner("Processing ....."):
                raw_text=get_pdf_text(pdf_docs)
                text_chunks=get_text_chunks(raw_text)
                vector_embeddings=get_vector_store(text_chunks)
                st.session_state.conversation=get_coversational_chain(vector_embeddings)
                # Process the uploaded PDF files here
                st.success("File Uploaded & Processed Successfully")
        
if __name__=="__main__":
    main()
    