# 🪄 PostCraft-AI

> Generate professional, engaging, and audience-focused LinkedIn posts using Google Gemini AI.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 🚀 Overview

PostCraft-AI is an AI-powered LinkedIn content generation platform built with **Python**, **Streamlit**, and **Google Gemini AI**.

The application helps creators, professionals, founders, marketers, and students generate high-quality LinkedIn posts in seconds using proven copywriting frameworks and customizable writing styles.

---

## ✨ Features

### 📝 Smart Post Generation
Generate engaging LinkedIn posts on any topic using Gemini AI.

### 🎭 Multiple Writing Tones
Choose from:

- Professional
- Inspirational
- Humorous
- Funny
- Angry
- Sad

### 🎯 Audience Targeting
Customize content for specific audiences such as:

- Developers
- Founders
- Students
- Recruiters
- Marketers
- Entrepreneurs

### 📚 Copywriting Frameworks

Supports:

- AIDA (Attention, Interest, Desire, Action)
- PAS (Problem, Agitate, Solution)
- Storytelling
- Listicle
- How-To / Tips
- Custom Style

### 📏 Flexible Post Lengths

- Short (100–150 words)
- Medium (200–300 words)
- Long (400–500 words)

### 🎨 Modern Streamlit UI

- Beautiful dark theme
- Responsive layout
- Download generated posts
- Session history
- One-click regeneration

---

## 🏗️ Project Structure

```text
PostCraft-AI/
│
├── app.py                # Streamlit UI
├── main.py               # CLI Entry Point
├── config.py             # Gemini Configuration
├── prompt_builder.py     # Prompt Engineering Logic
├── user_inputs.py        # Input Collection
│
├── requirements.txt
├── .gitignore
├── README.md
└── .env
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/priyam-10/PostCraft-AI.git
cd PostCraft-AI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Gemini API

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

Get your Gemini API key from:

https://aistudio.google.com/

---

## ▶️ Run Application

### Streamlit App

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

### CLI Version

```bash
python main.py
```

---

## 🧠 How It Works

1. User enters a topic.
2. Selects tone, audience, framework, and length.
3. Prompt Builder creates a structured prompt.
4. Gemini AI generates the LinkedIn post.
5. Streamlit displays the result.
6. User can copy or download the post.

---

## 🛠️ Tech Stack

| Technology | Usage |
|------------|--------|
| Python | Backend |
| Streamlit | Frontend UI |
| Gemini AI | Content Generation |
| dotenv | Environment Variables |
| Git & GitHub | Version Control |

---

## 📈 Future Improvements

- LinkedIn carousel generation
- Multi-language support
- Content scheduling
- Hashtag optimization
- Post analytics
- Export to PDF
- User authentication

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 👨‍💻 Author

**Priyam**

GitHub:
https://github.com/priyam-10

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and motivates future improvements.

---

Made with ❤️ using Python, Streamlit, and Google Gemini AI.
