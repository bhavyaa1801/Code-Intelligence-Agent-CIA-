# CIA — Code Intelligence Agent

CIA (Code Intelligence Agent) is a Repository Intelligence Engine that understands software projects using Retrieval-Augmented Generation (RAG).

Unlike a traditional chatbot, CIA analyzes an entire repository, indexes it, intelligently retrieves relevant code and documentation, and answers developer questions with repository-specific context.

---

## Vision

Build a production-grade repository understanding system capable of:

- Repository-aware Q&A
- Architecture understanding
- Knowledge transfer
- Semantic code retrieval
- Multi-language support
- Hybrid Search
- Symbol-aware retrieval
- Incremental indexing

The long-term goal is for CIA to become one of the tools inside Jarvis.

---

## Architecture

Repository
│
▼
RepositoryManager
│
▼
RepositoryScanner
│
▼
RepositoryFilter
│
▼
RepositoryClassifier
│
▼
DocumentBuilder
│
▼
RepositoryNodeParser
│
▼
IndexBuilder (ChromaDB)
│
▼
QueryAnalyzer (Gemini Planner)
│
▼
RepositoryRetriever
│
▼
PromptBuilder
│
▼
Gemini
│
▼
Answer

---

## Features

### Repository Pipeline

- Clone/Open repositories
- Recursive scanning
- Ignore build/cache folders
- File classification
- Language detection

### Indexing

- Metadata-rich Documents
- Semantic chunking
- ChromaDB persistent storage
- One collection per repository

### Retrieval

- Gemini Query Planner
- Metadata filtering
- Repository-aware prompt building

Planner output example:

```json
{
    "file_types": ["SOURCE_CODE"],
    "languages": ["python"],
    "top_k": 5,
    "confidence": 0.96
}
