# 📑🔖 Information Retrieval Tool

## 🔍 Project Overview

The **Information Retrieval Tool** is a web-based application designed to help users extract and retrieve relevant information from PDF documents effortlessly. By leveraging natural language processing (NLP) and  and GenAI concepts, this tool allows users to upload PDFs, ask questions related to their content, and receive accurate, context-based answers.

This project is built using technologies such as:
- **Streamlit** for an interactive and user-friendly web interface.
- **LangChain** for conversational AI and text processing.
- **FAISS** for efficient similarity search and document retrieval.
- **HuggingFace Transformers** for powerful text embeddings.

Whether you're dealing with research papers, legal documents, or business reports, this tool can help you quickly find the information you need without manually skimming through the entire document.

---

## 🚀 Features

- 📂 **Upload Multiple PDFs:** Easily upload and analyze multiple PDF files.
- 🧠 **Conversational AI:** Ask questions and get responses from the uploaded PDFs.
- 📏 **Configurable Chunking:** Adjust chunk size and overlap for better text processing.
- 🔍 **Efficient Information Retrieval:** Uses FAISS for fast and scalable vector search.
- 🎯 **Streamlit UI:** User-friendly and interactive web interface.

---
## 📁 Project Structure

```
📂Directory structure:
    └── kiran-91-information-retrieval-from-pdf/
        ├── README.md
        ├── LICENSE
        ├── app.py
        ├── requirements.txt
        ├── setup.py
        └── src/
            ├── __init__.py
            └── helper.py

```

## 🛠️ Installation

1. **Clone the Repository:**
```bash
git clone https://github.com/kiran-91/Information-Retrieval-from-PDF.git
cd Information-Retrieval-from-PDF
```

2. **Create a Virtual Environment:**
```bash
python -m venv venv
venv\Scripts\activate     # to activate on windows 
source venv/bin/activate  # to activate on mac
```

3. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set Environment Variables:**
   - Create a `.env` file in the root directory and add:
```bash
HF_TOKEN=<your_huggingface_api_key>    # store your huggingface api key
GROQ_API_KEY=<your_groq_api_key>       # store your groq api key
```

5. **Run the Application:**
```bash
streamlit run app.py
```
---

## 🏗️ How It Works

1. **Upload PDF Files:**
   - Use the sidebar to upload one or more PDF documents.

2. **Adjust Processing Parameters:**
   - Set chunk size and overlap to optimize text segmentation.

3. **Start Processing:**
   - Click `Submit & Process` to extract text and initialize the conversation model.

4. **Ask Questions:**
   - Type your queries in the input box, and the system will provide context-aware answers.

---

## 🔧 Configuration Options

- **Chunk Size:** Define how much text is processed in a single chunk (default: `1000`).
- **Chunk Overlap:** Set overlap between consecutive chunks (default: `20`).
- **Model Name:** Uses `all-MiniLM-L6-v2` by default for text embeddings.

---

## ⚠️ Troubleshooting

- Ensure the `.env` file contains correct API keys.
- Use appropriate chunk sizes for large PDF files.
- Check Streamlit logs for potential errors.

---

## 📜 License

This project is licensed under the General Public License-V3. See the `LICENSE` for more details

---

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

---

## 🌟 Acknowledgements

- [LangChain](https://www.langchain.com/) for conversational AI.
- [FAISS](https://faiss.ai/) for vector storage.
- [Streamlit](https://streamlit.io/) for the interactive UI.

---

