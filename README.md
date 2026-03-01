# 🔍 Sherlock — A Persona-Based AI Chatbot

A conversational AI chatbot built with LangChain and Google Gemini, wrapped in a 
Gradio web interface. The bot maintains a consistent persona and remembers 
conversation history within a session.

---

## 🧠 What It Does

- Talks to you as a specific AI persona (defined via system prompt)
- Remembers everything said in the current conversation
- Runs as a local web app with a clean chat UI
- Supports sharing via a public Gradio link

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| `LangChain` | Prompt management, chain orchestration |
| `Google Gemini 2.5 Flash` | The underlying LLM |
| `Gradio` | Web UI for the chatbot |
| `python-dotenv` | Keeps API keys and prompts out of source code |

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/sherlock-chatbot.git
cd sherlock-chatbot
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your `.env` file
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_google_gemini_api_key_here

Never commit this file. It's in `.gitignore` for a reason.

### 4. Run the app
```bash
python main.py
```
Then open the local URL shown in your terminal.

---

## 📁 Project Structure
```
sherlock-chatbot/
│
├── main.py              # Main application file
├── sherlock.png        # Avatar image for the chatbot
├── .env                # Secret keys and prompt (never commit this)
├── .gitignore          # Ensures .env stays private
└── README.md           # You're reading this
```

---

## ⚠️ Important Notes

- The `.env` file is **never** pushed to GitHub — it contains your API key and persona prompt
- Session memory resets when you refresh the page (by design)
- The `share=True` flag in `page.launch()` creates a temporary public URL via Gradio's servers

---

## 🧩 How It Works (Architecture)
```
User Input
    ↓
Gradio UI (manages session history)
    ↓
LangChain Chain:
  [System Prompt] + [Chat History] + [New Input]
    ↓
Google Gemini 2.5 Flash
    ↓
Response → displayed in chat
```

---

## 📦 Requirements

Generate this file by running:
```bash
pip freeze > requirements.txt
```

Key packages:
- `langchain`
- `langchain-google-genai`
- `gradio`
- `python-dotenv`

---

## 🙋 Author

Built by Fahmid Alam — feel free to fork, modify, and make the persona your own.