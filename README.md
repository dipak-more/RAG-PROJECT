# 📄 PDF RAG Chatbot using Mistral AI, LangChain & ChromaDB

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Mistral](https://img.shields.io/badge/Mistral-AI-orange)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-red)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-blue)

> A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask natural language questions. The system retrieves the most relevant content from the uploaded documents using vector search and generates accurate answers using the Mistral Large Language Model.

---

# 🚀 Project Overview

Large Language Models cannot answer questions about private documents unless those documents are provided as context.

This project solves that problem by implementing a complete **Retrieval-Augmented Generation (RAG)** pipeline.

The application:

* Uploads PDF documents
* Extracts text
* Splits text into semantic chunks
* Converts chunks into embeddings
* Stores embeddings inside ChromaDB
* Retrieves the most relevant chunks for a question
* Sends retrieved context to Mistral AI
* Generates accurate answers grounded in the uploaded PDFs

---

# 🏗️ Architecture

```
                 PDF Upload
                     │
                     ▼
             PyPDFLoader
                     │
                     ▼
     RecursiveCharacterTextSplitter
                     │
                     ▼
          Mistral Embeddings
                     │
                     ▼
               ChromaDB
                     │
        Similarity Search (Top-K)
                     │
                     ▼
          Retrieved Context
                     │
                     ▼
       Context + User Question
                     │
                     ▼
             Mistral LLM
                     │
                     ▼
             Final Response
                     │
                     ▼
              Streamlit UI
```

---

# ✨ Features

* Upload one or multiple PDF files
* Automatic PDF text extraction
* Intelligent text chunking
* Vector embeddings using Mistral AI
* ChromaDB vector database
* Semantic similarity search
* Context-aware question answering
* Streamlit web interface
* Fast document retrieval
* Easy to extend with new LLMs or vector databases

---

# 🛠 Tech Stack

| Category              | Technology                     |
| --------------------- | ------------------------------ |
| Programming Language  | Python                         |
| LLM                   | Mistral AI                     |
| Framework             | LangChain                      |
| Vector Database       | ChromaDB                       |
| Embedding Model       | Mistral Embeddings             |
| PDF Loader            | PyPDFLoader                    |
| Text Splitter         | RecursiveCharacterTextSplitter |
| Frontend              | Streamlit                      |
| Environment Variables | python-dotenv                  |

---

# 📂 Project Structure

```
RAG-PDF-Chatbot/
│
├── app.py                    # Streamlit application
├── main.py                   # Main RAG logic
├── requirements.txt
├── .env
├── README.md
│
├── data/
│   └── sample.pdf
│
├── chroma_db/
│
├── utils/
│   ├── loader.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── rag_pipeline.py
│
└── assets/
    └── architecture.png
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/RAG-PDF-Chatbot.git
```

Move into the project

```bash
cd RAG-PDF-Chatbot
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file.

```env
MISTRAL_API_KEY=your_api_key_here
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

The application will launch in your browser.

---

# 🔄 Workflow

### Step 1

Upload one or more PDF files.

↓

### Step 2

Extract text using PyPDFLoader.

↓

### Step 3

Split text into manageable chunks.

↓

### Step 4

Generate embeddings using Mistral AI.

↓

### Step 5

Store embeddings inside ChromaDB.

↓

### Step 6

User asks a question.

↓

### Step 7

Retrieve the most relevant chunks.

↓

### Step 8

Send retrieved context to Mistral LLM.

↓

### Step 9

Generate the final answer.

---

# 📸 Application Preview

```
+------------------------------------------------------+
|               PDF RAG Chatbot                        |
+------------------------------------------------------+

Upload PDF

[ Choose File ]

--------------------------------------------

Ask your question:

______________________________________

[ Get Answer ]

--------------------------------------------

Answer:

The generated response appears here...

```

---

# 💡 Example Questions

* Summarize this document.
* What is Retrieval-Augmented Generation?
* Explain the main conclusion.
* What technologies are discussed?
* List the important points.
* Give a detailed summary.

---

# 📈 Future Improvements

* Multi-document retrieval
* Chat history memory
* Hybrid Search (BM25 + Vector Search)
* FAISS support
* Pinecone integration
* Source citation highlighting
* PDF page references
* Conversation memory
* Docker support
* FastAPI backend
* Authentication
* Cloud deployment
* Streaming responses

---

# 🎯 Learning Outcomes

Through this project, I learned:

* Retrieval-Augmented Generation (RAG)
* Large Language Models
* LangChain Pipelines
* Prompt Engineering
* Semantic Search
* Vector Databases
* Embedding Models
* ChromaDB
* Streamlit
* Environment Variable Management
* Document Processing
* Similarity Search
* Production-ready AI Workflow

---

# 🤝 Contributing

Contributions are welcome.

Feel free to fork the repository, create a new branch, and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Dipak More**

AI Engineer | Generative AI | LLMs | RAG | LangChain | AI Agents | MLOps

* GitHub: https://github.com/dipak-more
* LinkedIn: https://www.linkedin.com/in/dipak-more-ai

---

⭐ If you found this project helpful, consider giving it a **Star** on GitHub!
