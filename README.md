# 🏛️ Multi-Agent Arabic Heritage RAG Assistant

A multi-agent RAG (Retrieval-Augmented Generation) application built with CrewAI that provides intelligent answers about Arabic heritage and culture. The system supports both Arabic and English queries and automatically responds in the detected language.

## 🌟 Features

- **Multilingual Support**: Understands and responds in both Arabic and English
- **Intelligent RAG System**: Semantic search over 39,000+ lines of Arabic heritage knowledge
- **Multi-Agent Architecture**: Powered by CrewAI framework with specialized agents
- **Local LLM**: Uses Ollama's aya-expanse:8b model for privacy and performance
- **Interactive Web UI**: Clean Streamlit interface for easy interaction
- **Language Detection**: Automatically detects query language and responds accordingly

## 🏗️ Architecture

### Technology Stack

- **CrewAI**: Multi-agent orchestration framework
- **Ollama (aya-expanse:8b)**: Local LLM with Arabic/English support
- **Streamlit**: Web interface
- **sentence-transformers**: Semantic search using MiniLM-L6-v2
- **Hugging Face Transformers**: Language detection with XLM-RoBERTa

### System Components

#### 1. Web Interface (`app.py`)

- Streamlit-based UI for user interaction
- Accepts questions about Arabic heritage
- Displays agent research results

#### 2. Core Crew System (`src/rag_crewai/crew.py`)

- Heritage Guide agent with multilingual capabilities
- Sequential processing workflow
- Integrated with custom tools

#### 3. Custom Tools

**Heritage Search Tool** (`tools/heritage_tool.py`):

- Loads heritage knowledge base from text corpus
- Creates semantic chunks (400 words each)
- Generates embeddings using sentence-transformers
- Retrieves top-3 most relevant chunks using cosine similarity

**Language Detection Tool** (`tools/language_detection.py`):

- Detects whether question is in Arabic or English
- Uses XLM-RoBERTa multilingual model
- Returns language code ('ar' or 'en')

**Weather Tool** (`tools/weather_tool.py`):

- Provides weather information for heritage locations

#### 4. Configuration

**Agents** (`config/agents.yaml`):

- Heritage Guide agent configuration
- Role, goal, and backstory definitions

**Tasks** (`config/tasks.yaml`):

- Language detection task
- Heritage search task
- Response generation in detected language

## 📚 Knowledge Base

The system includes a comprehensive knowledge base (`knowledge/_ALL_ARAB_HERITAGE_EN.txt`):

- 39,000+ lines of curated content
- Information about Arab heritage sites
- Historical locations including Jerusalem, Palestine, and more
- Compiled from Wikipedia and authoritative sources

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**
2. **Ollama** installed with aya-expanse:8b model
   ```bash
   ollama pull aya-expanse:8b
   ```

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Multi-Agent-Arabic-Heritage-RAG-Assistant-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   uv run
   ```

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💡 Usage

1. Open the web interface
2. Enter your question in Arabic or English
3. Click "🔍 Search & Answer"
4. The system will:
   - Detect your question's language
   - Search the heritage knowledge base
   - Generate a comprehensive answer in your language

### Example Questions

**English:**

- "Tell me about Arabic calligraphy traditions"
- "What is the history of the Great Mosque of Damascus?"
- "Describe traditional Arabic architecture"

**Arabic:**

- "أخبرني عن تقاليد الخط العربي"
- "ما هو تاريخ المسجد الأموي؟"
- "صف العمارة العربية التقليدية"

## 📁 Project Structure

```
.
├── app.py                          # Streamlit web interface
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project configuration
├── README.md                       # Documentation
├── knowledge/
│   └── _ALL_ARAB_HERITAGE_EN.txt  # Heritage knowledge base
└── src/
    └── rag_crewai/
        ├── __init__.py
        ├── crew.py                 # CrewAI agent configuration
        ├── main.py                 # Entry point
        ├── config/
        │   ├── agents.yaml         # Agent definitions
        │   └── tasks.yaml          # Task definitions
        └── tools/
            ├── __init__.py
            ├── heritage_tool.py    # RAG search tool
            ├── language_detection.py # Language detection
            └── weather_tool.py     # Weather information
```

## 🔧 Configuration

### Agent Configuration (`config/agents.yaml`)

Define agent roles, goals, and capabilities

### Task Configuration (`config/tasks.yaml`)

Define task sequence and dependencies

### LLM Configuration

The system uses Ollama's aya-expanse:8b model. To change the model, update the configuration in `crew.py`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Knowledge base compiled from Wikipedia and public sources
- Built with CrewAI framework
- Powered by Ollama and open-source LLMs

## 📧 Support

For questions or issues, please open an issue on the repository.
