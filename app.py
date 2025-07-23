# ------------------------- #
#      IMPORT SECTION      #
# ------------------------- #
from dotenv import load_dotenv
import os
try:
    import streamlit as st
except ModuleNotFoundError:
    raise ImportError("The 'streamlit' module is not installed. Please install it using 'pip install streamlit' and try again.")

from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from huggingface_hub import login, InferenceClient

# ------------------------- #
#      ENV VARIABLES       #
# ------------------------- #

load_dotenv()
hf_token = os.getenv("PDF_CHATBOX_API")
if not hf_token:
    raise EnvironmentError("Missing HuggingFace API token in environment variable 'PDF_CHATBOX_API'")

# Login using the token from your .env file
login(token=hf_token)

# ------------------------- #
#         STYLING          #
# ------------------------- #

st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
            padding: 2rem;
        }

        h1 {
            color: #2d2d2d;
            font-size: 2.8rem;
            font-family: 'Segoe UI', sans-serif;
        }

        .stFileUploader {
            background-color: #ffffff;
            border: 1px solid #ccc;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 1.5rem;
        }

        .stMarkdown {
            background-color: #ffffff;
            padding: 1rem;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            margin-bottom: 1rem;
        }

        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 0.5rem 1.2rem;
            border-radius: 8px;
            border: none;
            font-size: 1rem;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------- #
#      APP TITLE UI        #
# ------------------------- #

st.title("📚 AI PDF Chatbot")

uploaded_file = st.file_uploader("Upload a PDF to chat with 👇", type="pdf")

# ------------------------- #
#    CHATBOT FUNCTIONALITY #
# ------------------------- #

def ask_llm(client, question, context):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
        {"role": "user", "content": f"Context:\n{context}"},
        {"role": "user", "content": question}
    ]

    try:
        response = client.chat_completion(messages=messages, max_tokens=200, temperature=0.7)

        print("Raw LLM Response:", response)

        if isinstance(response, dict) and "choices" in response:
            return response["choices"][0]["message"]["content"].strip()

        return f"Unexpected response: {response}"

    except Exception as e:
        import traceback
        traceback.print_exc()
        st.error(traceback.format_exc())
        return f"LLM call failed: {str(e)}"

if uploaded_file:
    st.success("✅ PDF uploaded successfully!")

    with open("uploaded_doc.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyMuPDFLoader("uploaded_doc.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
    except Exception as e:
        st.error(f"Failed to load embeddings: {e}")
        st.stop()

    try:
        db = FAISS.from_documents(docs, embeddings)
    except Exception as e:
        st.error(f"Failed to initialize FAISS vectorstore: {e}")
        st.stop()

    # ✅ Using chat_completion with Zephyr model
    client = InferenceClient(model="HuggingFaceH4/zephyr-7b-beta", token=hf_token)

    user_question = st.text_input("💬 Ask something from the PDF:")
    if user_question:
        try:
            matched_docs = db.similarity_search(user_question)
            context = "\n\n".join([doc.page_content for doc in matched_docs])
            answer = ask_llm(client, user_question, context)
            st.markdown(f"**🤖 Answer:** {answer}")
        except Exception as e:
            st.error(f"Error during question answering: {e}")

# ------------------------- #
#         FOOTER           #
# ------------------------- #

st.markdown("<hr><center>🚀 Created with ❤️ by Ifiok & Zephyr</center>", unsafe_allow_html=True)
