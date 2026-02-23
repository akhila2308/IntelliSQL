import streamlit as st
import pandas as pd
from database import init_db, read_query, DB_NAME
from llm_engine import get_response
from prompt_config import prompt

# Initialize database
init_db()

# ---------------- HOME PAGE ---------------- #
def page_home():
    st.markdown("""
        <style>
        body {
            background-color: #2E2E2E;
        }
        h1, h2, h3 {
            color: #4CAF50;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title("⭐ IntelliSQL")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🚀 Features")
        st.write("""
        - Intelligent Query Assistance  
        - Data Exploration and Insights  
        - Efficient Data Retrieval  
        - Performance Optimization  
        - Syntax Suggestions  
        - Trend Analysis  
        """)

    with col2:
        st.info("Convert natural language into executable SQL using Gemini 2.5 Flash.")


# ---------------- ABOUT PAGE ---------------- #
def page_about():
    st.title("📘 About IntelliSQL")

    st.write("""
    IntelliSQL is an AI-powered SQL assistant built using Streamlit and Google Gemini.

    It leverages Large Language Models (LLMs) to translate natural language queries
    into structured SQL statements.

    Architecture:

    User → Streamlit UI → Gemini LLM → SQL → SQLite → Results

    Key Components:
    - NLP-to-SQL Translation
    - Gemini 2.5 Flash Integration
    - SQLite Query Execution
    - Modular Architecture
    - Secure API Handling
    """)

    st.image("https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png")


# ---------------- INTELLIGENT QUERY PAGE ---------------- #
def page_intelligent_query_assistance():
    st.title("🤖 Intelligent Query Assistance")

    que = st.text_input("Enter Your Query:")
    submit = st.button("Get Answer")

    if submit and que:
        try:
            response = get_response(que, prompt)

            # 🔐 Security Validation
            if not response.upper().startswith("SELECT"):
                st.error("Only SELECT queries are allowed.")
                return

            st.write("### Generated SQL Query:")
            st.code(response)

            result = read_query(response, DB_NAME)

            if result:
                df = pd.DataFrame(result)
                st.write("### Query Result:")
                st.table(df)
            else:
                st.warning("No results found.")

        except Exception as e:
            st.error(f"An error occurred: {e}")


# ---------------- MAIN CONTROLLER ---------------- #
def main():
    st.set_page_config(
        page_title="IntelliSQL",
        page_icon="⭐",
        layout="wide"
    )

    pages = {
        "Home": page_home,
        "About": page_about,
        "Intelligent Query Assistance": page_intelligent_query_assistance
    }

    selection = st.sidebar.radio("Go to", list(pages.keys()))
    pages[selection]()


if __name__ == "__main__":
    main()
