# 💰 AI Finance Assistant

An AI-powered personal finance assistant built with:

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![OpenAI](https://img.shields.io/badge/OpenAI-API-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-orange)

This application allows users to:

✅ Record expenses

✅ View spending history

✅ Visualize spending patterns

✅ Receive AI-generated financial insights

✅ Chat with an AI finance assistant

---

## 🚀 Features

### Expense Tracking

Store:

- Amount
- Category
- Description
- Date

using SQLite.

---

### Dashboard Analytics

View:

- Total Spending
- Number of Transactions
- Average Spending

---

### Spending Visualization

Includes:

- Bar Chart
- Pie Chart

to help understand spending patterns.

---

### AI Financial Analysis

Uses OpenAI to:

- Analyze spending habits
- Identify spending patterns
- Suggest ways to save money
- Provide weekly action plans

---

### AI Chatbot

Ask questions such as:

- Where am I spending most?
- How can I reduce expenses?
- What should I budget better?

and receive AI-powered answers.

---

# 🏗 Architecture

User
↓
Streamlit UI
↓
SQLite Database
↓
OpenAI API
↓
Financial Insights

---

# 📂 Project Structure

```text
AI-Finance-Assistant/
│
├── app.py
├── chatbot.py
├── database.py
├── requirements.txt
├── .env.example
├── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Finance-Assistant.git

cd AI-Finance-Assistant
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Mac/Linux

```bash
python -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Configure OpenAI API Key

Create a file named:

```text
.env
```

Add:

```env
OPENAI_API_KEY=your_api_key_here
```

---

# ▶ Run Application

```bash
streamlit run app.py
```

Application will be available at:

```text
http://localhost:8501
```

---

# 📊 Screenshots

## Dashboard

Insert screenshot here.

---

## AI Analysis

Insert screenshot here.

---

## Chatbot

Insert screenshot here.

---

# 🌍 Deployment

This project can be deployed on:

- Streamlit Community Cloud
- Render
- Railway

---

## Streamlit Deployment

1. Push code to GitHub

2. Login to Streamlit Cloud

3. Create New App

4. Select repository

5. Add secret:

```toml
OPENAI_API_KEY="your_api_key"
```

6. Deploy

---

# 🎯 Future Improvements

- User Authentication
- Multi-user Support
- Monthly Reports
- Budget Tracking
- WhatsApp Integration
- Telegram Integration
- RAG-based Financial Knowledge Base

---

# 👨‍💻 Workshop Project

This project was developed as part of the:

**AI for Business & Income Workshop**

Organized by:

### Algorithmic Explorers

Building the next generation of AI innovators across Africa.

---

# 📜 License

MIT License
