# Multi-Agent Arabic Heritage RAG Assistant - Complete Project Documentation

## 1. Project Name and Description

**Project Name:** Multi-Agent Arabic Heritage RAG Assistant

**Description:**
A multi-agent Retrieval-Augmented Generation (RAG) system that answers questions about Arabic heritage and culture. It uses CrewAI and a local LLM (Ollama) to provide accurate, culturally relevant information in both Arabic and English. The system automatically detects the user's language and draws from a large knowledge base on Arab heritage.

---

## 2. End User Benefits

End users benefit from instant, multilingual (Arabic/English) access to a rich database of Arabic heritage. The user-friendly interface makes learning about cultural sites and traditions easy and engaging. Because it runs locally, the tool ensures user privacy and can work offline. It also helps with travel planning by providing information on heritage sites and weather. For students and researchers, it's a quick and reliable educational resource.

---

## 3. Business Benefits

Businesses can use this application to improve customer service in the tourism sector, provide an interactive learning tool for educational institutions, and serve as a virtual guide for museums. It helps reduce operational costs by automating responses to inquiries, enhances user engagement, and can be scaled to a global audience. The system also supports cultural preservation efforts and can be white-labeled by tech companies as a specialized AI solution.

---

## 4. Technical Architecture and Components

### **System Architecture Diagram**

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE LAYER                            │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    Streamlit Web Interface                        │  │
│  │                          (app.py)                                 │  │
│  │  - User query input                                               │  │
│  │  - Display results                                                │  │
│  │                                                                │  │
│  └─────────────────────────────┬─────────────────────────────────────┘  │
└─────────────────────────────────┼──────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      ORCHESTRATION LAYER                                │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    CrewAI Framework                               │  │
│  │                  (src/rag_crewai/crew.py)                         │  │
│  │                                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │           Heritage Guide & Travel Assistant Agent          │  │  │
│  │  │                                                            │  │  │
│  │  │  Role: Heritage Guide & Travel Assistant                  │  │  │
│  │  │  Process: Sequential Task Execution                       │  │  │
│  │  │  LLM: Ollama (qwen2.5:0.5b)                              │  │  │
│  │  └─────────────────────┬──────────────────────────────────────┘  │  │
│  └────────────────────────┼───────────────────────────────────────────┘  │
└─────────────────────────────┼──────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          TASK EXECUTION LAYER                            │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    Task Workflow                                  │  │
│  │              (config/tasks.yaml)                                  │  │
│  │                                                                   │  │
│  │  STEP 1: Language Detection                                      │  │
│  │         ↓                                                         │  │
│  │  STEP 2: Tool Selection & Execution                              │  │
│  │         ↓                                                         │  │
│  │  STEP 3: Response Generation                                     │  │
│  └─────────────────────────┬─────────────────────────────────────────┘  │
└─────────────────────────────┼──────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          TOOLS LAYER                                    │
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │  Language        │  │  Heritage        │  │  Weather Forecast    │  │
│  │  Detection Tool  │  │  Search Tool     │  │  Tool                │  │
│  │                  │  │                  │  │                      │  │
│  │  - XLM-RoBERTa   │  │  - Semantic      │  │  - Weather API       │  │
│  │  - Multilingual  │  │    Search        │  │  - Location-based    │  │
│  │  - Returns       │  │  - Top-3         │  │  - Forecast data     │  │
│  │    'ar' or 'en'  │  │    Retrieval     │  │                      │  │
│  └──────────────────┘  └────────┬─────────┘  └──────────────────────┘  │
└─────────────────────────────────┼──────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      DATA & MODEL LAYER                                 │
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │  Knowledge Base  │  │  Embedding Model │  │  Language Models     │  │
│  │                  │  │                  │  │                      │  │
│  │  - 39,000+ lines │  │  - SentenceXfer  │  │  - Ollama (Local)    │  │
│  │  - Arab heritage │  │  - MiniLM-L6-v2  │  │  - qwen2.5:0.5b     │  │
│  │  - Text chunks   │  │  - Cosine        │  │  - Arabic/English    │  │
│  │  - 400 words/    │  │    similarity    │  │    support           │  │
│  │    chunk         │  │  - Normalized    │  │                      │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

### **Component Descriptions**

The system is composed of five main layers:

1.  **User Interface (Streamlit):** A simple web interface for users to ask questions.
2.  **Orchestration (CrewAI):** Manages the agents and tasks, ensuring a smooth workflow from question to answer.
3.  **Task Execution:** A workflow that first detects the language, then selects the right tools to answer the question.
4.  **Tools:**
    - **Heritage Search Tool:** Searches the knowledge base for relevant information using semantic search.
    - **Language Detection Tool:** Identifies if the question is in Arabic or English.
    - **Weather Forecast Tool:** Provides weather information for heritage sites.
5.  **Data & Models:**
    - **Knowledge Base:** A text file with over 39,000 lines of information on Arab heritage.
    - **Embedding Model:** Converts text into numerical representations for semantic search.
    - **Language Model (Ollama):** A local LLM that generates answers based on the retrieved information.

### **Data Flow**

The process is straightforward: a user asks a question, CrewAI orchestrates the agents to detect the language, find relevant information, and generate an answer, which is then displayed to the user.

### **Technologies and Tools Tried But Not Used**

- **OpenAI GPT Models:** Avoided due to cost and privacy concerns. Chose a local LLM instead.
- **Vector Databases (e.g., Pinecone):** Not used to keep the architecture simple, as the current knowledge base is manageable in-memory.
- **LangChain:** CrewAI was chosen for its stronger multi-agent capabilities.

---

## 5. Current Limitations and Drawbacks

- **Knowledge Base:** The information is static, primarily in English, and may not be exhaustive.
- **Performance:** The local LLM is slower than cloud-based alternatives, and the system has a noticeable cold start time.
- **Features:** The user interface is basic, lacking features like conversation history. The system also has limited tool integration and error handling.
- **Deployment:** Requires manual setup of Ollama and other dependencies.

---

## 6. References and Citations

- **CrewAI:** [https://docs.crewai.com/](https://docs.crewai.com/)
- **Streamlit:** [https://streamlit.io/](https://streamlit.io/)
- **Sentence Transformers:** [https://www.sbert.net/](https://www.sbert.net/)
- **Ollama:** [https://ollama.ai/](https://ollama.ai/)

---

## Document Metadata

- **Document Version:** 1.1
- **Last Updated:** December 31, 2025
- **Project Repository:** Multi-Agent-Arabic-Heritage-RAG-Assistant

---
