# 🧠 IntelliSQL  
### Intelligent SQL Querying with LLMs Using Gemini 2.5 Flash  

---

🚀 AI-powered web application that converts natural language queries into executable SQL using Google Gemini.

---

## 📌 Project Overview

IntelliSQL is an AI-driven system that enables users to interact with relational databases using plain English instead of SQL syntax.  

The application uses Google Gemini 2.5 Flash to translate natural language into structured SQL queries, executes them on a SQLite database, and displays the results in a Streamlit web interface.

## 🚀 Features

- 🗣 Natural Language to SQL Conversion  
- 🤖 Google Gemini 2.5 Flash Integration  
- 🗄 SQLite Database Execution  
- 📊 Structured Result Display using Pandas  
- 🖥 Multi-Page Streamlit Interface  
- 🔐 Secure API Key Handling using .env  
- 🛡 SELECT Query Restriction for Safety  
- 📦 Docker Deployment Ready  

---

## 🏗 System Architecture
User (Browser)
        ↓
Streamlit UI
        ↓
get_response()
        ↓
Gemini 2.5 Flash LLM
        ↓
Generated SQL
        ↓
read_query()
        ↓
SQLite Database
        ↓
Results Displayed in UI

## 🛠 Technology Stack

- **Programming Language:** Python  
- **Web Framework:** Streamlit  
- **LLM:** Google Gemini 2.5 Flash  
- **Database:** SQLite  
- **Data Handling:** Pandas  
- **Containerization:** Docker  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
IntelliSQL/
│
├── app.py
├── database.py
├── llm_engine.py
├── prompt_config.py
├── requirements.txt
├── Dockerfile
├── README.md
├── assets/
---

## 🗄 Database Schema

```sql
CREATE TABLE STUDENTS(
    NAME TEXT,
    CLASS TEXT,
    MARKS INTEGER,
    COMPANY TEXT
);
```

## 📸 Application Screenshots

### 🏠 Home Page
![Home Page](assets/home.png)

### 🤖 Query Interface
![Query Page](assets/query.png)

### 📊 Results Display
![Result Page](assets/result.png)

---

## ⚙ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/akhila2308/IntelliSQL.git
cd IntelliSQL
```
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Setup API Key
API_KEY=A***************

▶ Run Application
streamlit run app.py

Access in browser:
http://localhost:8501

