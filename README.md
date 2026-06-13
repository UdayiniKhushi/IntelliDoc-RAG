# IntelliDoc-RAG: Context-Aware PDF Interaction System

IntelliDoc is a professional-grade **Retrieval-Augmented Generation (RAG)** application that allows users to have natural language conversations with their PDF documents. It leverages Large Language Models (LLMs) and Vector Databases to provide accurate, context-based answers with specific citations.

## 🚀 Features
- **Semantic Search:** Uses Google Gemini Embeddings to understand the meaning behind queries, not just keywords.
- **Efficient Retrieval:** Powered by **Qdrant (Vector Database)** running in a Docker container for high-performance data fetching.
- **Citation-Aware Responses:** The system prompt ensures that the AI provides page numbers and specific references from the PDF.
- **Hallucination Reduction:** Strict context-grounding prevents the AI from making up information not present in the document.

## 🛠 Tech Stack
- **Language:** Python
- **LLM:** Google Gemini 1.5 Flash (via OpenAI SDK)
- **Framework:** LangChain
- **Vector Database:** Qdrant
- **Orchestration:** Docker
- **Embeddings:** Google Generative AI Embeddings

## ⚙️ Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourUsername/IntelliDoc-RAG.git
   cd IntelliDoc-RAG
   ```

2. **Setup Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. **Docker Setup (Qdrant):**
   Ensure Docker is running and start the Qdrant container:
   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your key:
   ```env
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

5. **Run the Application:**
   ```bash
   python chat.py
   ```

## 📈 Future Scope
- Integration of a Streamlit/Next.js frontend.
- Support for multiple document uploads.
- Implementation of hybrid search (Keyword + Semantic).

> **Note:** Currently uses Google Gemini Free Tier API; performance may be subject to provider rate limits.
  

