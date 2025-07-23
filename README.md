# 🤖 AI PDF Chatbot

An intelligent chatbot that reads and understands your PDF files — built with LangChain, HuggingFace Embeddings, and Streamlit.

---

## 🚀 Overview

The **AI PDF Chatbot** allows users to upload any PDF document and ask questions about its content. Whether it's a business report, research paper, contract, or user manual — this app gives you instant, context-aware answers.

---

## 🔧 Features

- 📄 Upload and parse PDF documents
- 🧠 Smart question-answering using LangChain
- 💬 Chat interface built with Streamlit
- 🔍 Semantic search using HuggingFace Embeddings
- ⚡ Fast and local (no OpenAI API required)
- 🛠️ Clean and lightweight interface

---

## 🛠️ Tech Stack

- [Python 3.11+](https://www.python.org)
- [Streamlit](https://streamlit.io/)
- [LangChain](https://www.langchain.com/)
- [HuggingFace Transformers & Embeddings](https://huggingface.co/)
- [FAISS](https://github.com/facebookresearch/faiss) for vector search
- [PyMuPDF (`fitz`)](https://pymupdf.readthedocs.io/) for PDF text extraction

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/NestedE/ai-pdf-chatbot-new.git
cd ai-pdf-chatbot-new

```

### 2. (Recommended) Create a virtual environment
```bash
python -m venv zephyr_env
source zephyr_env/bin/activate  # on macOS/Linux
# OR
zephyr_env\Scripts\activate  # on Windows
```

### 3. Install dependencies
pip install -r requirements.txt
```
PDF_CHATBOX_API=your_huggingface_api_key
```

### 4. Usage
```bash
streamlit run app.py
```
Then open http://localhost:8501 in your browser.

- Upload any .pdf file
- Ask natural-language questions like:
- "What is the summary of this document?"
- "Who is the main author?"
- "List all key points mentioned."
- Get instant, intelligent responses from the embedded AI
---

## 🛠 🔒 Environment Variables
- Create a .env file in the project root:
```bash
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
```

## 🌐 Deployment
You can deploy this to Streamlit Cloud by:

- Uploading this repo
- Setting your HuggingFace token as a secret
- Defining app.py as the main entry point
---

## 📸 Screenshots
Coming soon
---

## 🧠 Future Improvements

- Multi-PDF support
- Chat history memory
- Option to switch between local and cloud LLMs
- PDF summarization on upload
---

## 📜 License
MIT License
---

## 💬 Questions or Feedback?
- Feel free to open an issue or message me directly.
---

## ❤️ Author
- Made with love by **Ifiok & Zephyr**
---


