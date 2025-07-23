# 📚 AI PDF Chatbot

Your personal assistant to chat with your PDFs using powerful open-source models and local embeddings.

---

![Banner](https://img.shields.io/badge/PDF%20Chatbot-Streamlit%20App-green?style=flat-square&logo=streamlit)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Zephyr--7B--Beta-yellow?style=flat-square&logo=huggingface)
![License](https://img.shields.io/github/license/yourusername/ai-pdf-chatbot?style=flat-square)

---

## ✨ Features

- Upload any PDF and ask questions about it
- Uses [HuggingFace Zephyr-7B Beta](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) LLM
- Local vector search using FAISS
- Embeddings via Sentence Transformers
- Streamlit web interface with clean UI
- HuggingFace Inference API support

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/ai-pdf-chatbot.git
cd ai-pdf-chatbot
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```

### 3. Add Environment Variables
Create a `.env` file in the project root:
```
PDF_CHATBOX_API=your_huggingface_api_key
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 🛠 Technologies Used
- Python 3.11+
- Streamlit
- LangChain
- FAISS
- HuggingFace Inference API
- HuggingFace Embeddings
- PyMuPDF (PDF Loader)

---

## 📦 Create Executable (Windows Only)
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole app.py
```
Output will be in `dist/app.exe`

---

## 🐳 Run with Docker
### Dockerfile
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Build & Run
```bash
docker build -t ai-pdf-chatbot .
docker run -p 8501:8501 ai-pdf-chatbot
```

---

## 🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

---

## 📄 License
[MIT](LICENSE)

---

## ❤️ Author
Made with love by **Ifiok & Zephyr**
# -ai-pdf-chatbot
