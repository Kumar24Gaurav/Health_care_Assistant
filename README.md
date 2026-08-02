# 🩺 Medical AI Assistant

An AI-powered medical chatbot built using **Python**, **Gradio**, and **Mistral AI**. The chatbot provides general medical guidance, answers health-related questions, and encourages users to seek professional medical advice when symptoms appear serious.

> **Disclaimer:** This chatbot is intended for educational and informational purposes only. It is **not** a substitute for professional medical advice, diagnosis, or treatment.

---

# 📌 About the Project

Medical AI Assistant is a conversational chatbot that leverages the **Mistral Large Language Model (LLM)** to answer medical-related queries.

The chatbot uses a carefully designed **system prompt** to:

- Restrict responses to medical-related questions only.
- Provide general medical suggestions.
- Recommend consulting a healthcare professional for serious symptoms.
- Avoid generating misleading or fabricated medical information.
- Refuse questions unrelated to the medical domain.

The application features a simple and interactive user interface built with **Gradio**, making it easy for users to interact with the AI directly from their browser.

---

# ✨ Features

- 💬 Conversational AI chatbot
- 🩺 Medical-specific system prompt
- 🚫 Rejects non-medical questions
- ⚠️ Warns users to consult a doctor when necessary
- 🌐 Interactive Gradio web interface
- 🔐 Secure API key management using `.env`
- ⚡ Real-time responses using Mistral AI API

---

# 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend development |
| Gradio | User Interface |
| Mistral AI API | Large Language Model |
| python-dotenv | Environment variable management |
| UV | Dependency management |

---

# 📂 Project Structure

```
medical-ai-assistant/
│
├── app.py              # Gradio UI
├── chatbot.py          # Mistral API integration
├── config.py           # API key configuration
├── prompts.py          # System prompt
├── .env                # API Key (Not pushed to GitHub)
├── pyproject.toml
├── uv.lock
├── requirements.txt    # (Optional)
└── README.md
```

---

# ⚙️ Installation & Setup

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/medical-ai-assistant.git

cd medical-ai-assistant
```

---

## 2. Create a virtual environment

Using **uv**

```bash
uv venv
```

Activate it

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install dependencies

```bash
uv sync
```

Or install manually

```bash
uv add gradio mistralai python-dotenv
```

---

## 4. Create a `.env` file

```env
MISTRAL_API_KEY=your_api_key_here
```

---

## 5. Get a Mistral API Key

1. Create an account on Mistral AI.
2. Generate an API Key.
3. Copy the key into the `.env` file.

---

## 6. Run the application

```bash
uv run app.py
```

Open the browser at

```
http://127.0.0.1:7860
```

---

# 🧠 How It Works

```
                User
                  │
                  ▼
            Gradio Interface
                  │
                  ▼
       generate_response()
                  │
                  ▼
        System Prompt Added
                  │
                  ▼
           Mistral AI API
                  │
                  ▼
         AI Generated Response
                  │
                  ▼
          Displayed in Gradio
```

---

# 📸 Screenshots

---

## Chat Conversation

images/chat-01.png

images/chat-02.png

images/chat-03.png

---


# 📝 Example Queries

### General Medical Questions

- What is the normal blood pressure?
- What causes headaches?
- How can I treat a sore throat?
- What is a normal blood sugar level?
- Why do I have stomach pain?

---

### Serious Symptoms

- I have severe chest pain.
- I fell from my bike and cannot move my arm.
- I have difficulty breathing.

The chatbot recommends seeking immediate medical attention when appropriate.

---

# 🚫 Non-Medical Questions

The chatbot intentionally refuses unrelated questions.

Example:

```
User:
Who is the Prime Minister of India?

Response:
I am only responsible for answering medical-related questions.
```

---

# 🔒 Safety Measures

The chatbot follows several safety rules:

- Does not diagnose diseases with certainty.
- Encourages consultation with healthcare professionals.
- Rejects non-medical queries.
- Avoids generating fabricated medical information.
- Includes a medical disclaimer in responses.

---

# 📈 Future Improvements

- Conversation memory
- Voice input
- Medical PDF RAG
- Drug interaction lookup
- Appointment booking integration
- User authentication
- Chat history storage
- Response streaming
- Dark mode
- Multi-language support

---



# 👨‍💻 Author

**Kumar Gaurav**

GitHub: https://github.com/Kumar24Gaurav

LinkedIn: https://www.linkedin.com/in/kumar-gaurav-814a58299

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.