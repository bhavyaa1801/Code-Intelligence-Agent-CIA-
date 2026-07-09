
---

# Frontend Handoff Summary

## CIA Frontend

The backend retrieval pipeline is half implemented.

The frontend should behave like ChatGPT, but specifically for repositories.

---

## Pages

### 1. Home

Simple landing page.

Features:

- Project name
- Description
- "Start Chatting"

---

### 2. Repository Screen

Allow users to either:

- Clone GitHub Repository
- Open Existing Repository

Input:

```
Repository URL
```

Button:

```
Index Repository
```

After indexing:

Navigate to Chat.

---

### 3. Chat Screen

Layout:

```
---------------------------------------

Repository Name

---------------------------------------

Chat Messages

---------------------------------------

Input Box

[ Send ]

---------------------------------------
```

Very similar to ChatGPT.

---

### Message Types

User

```
How is authentication implemented?
```

CIA

```
Authentication is implemented using...
```

---

### Show Retrieved Files (Optional Side Panel)

Example

```
Retrieved Files

README.md

auth.py

jwt.py

database.py
```

Useful for debugging.

---

### Loading Screen

While indexing

```
Scanning Repository...

██████████

Reading Files...

██████████

Building Index...

██████████
```

---

### Settings

Allow changing

- Gemini Model
- Top K
- Theme

(Not mandatory initially.)

---

## API Endpoints (Expected)

```
POST /repository/index

POST /chat

GET /repositories

DELETE /repository
```

(Backend may evolve.)

---

## Design Style

Minimal.

Inspired by

- ChatGPT
- Cursor
- Claude

Avoid dashboards.

Focus on conversation.

---

## Tech Stack

- React
- TypeScript
- TailwindCSS
- Vite

---

## Nice-to-Have

- Markdown rendering
- Syntax highlighting
- Copy code button
- Streaming responses
- Dark mode
- Repository selector
- Chat history

---

# Current Backend Status

✅ Repository Pipeline

✅ ChromaDB

✅ Metadata Filtering

✅ Gemini Planner

✅ Repository Retrieval

✅ Prompt Builder

✅ Chat Service

🚧 Tree-sitter Integration (Current Work)

---

Once Tree-sitter is complete, the frontend won't need major changes—the backend will simply return more precise, symbol-aware answers.