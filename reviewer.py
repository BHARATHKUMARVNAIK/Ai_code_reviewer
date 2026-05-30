
from groq import Groq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

def get_client():
    try:
        return Groq(api_key=st.secrets["GROQ_API_KEY"])
    except:
        return Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_review(code: str, language: str = "Python"):
    client = get_client()

    user_content = f"""Review this {language} code thoroughly.

## 🐛 Bugs & Logic Errors
List each bug with: location, what's wrong, severity (High/Medium/Low)

## 🔒 Security Vulnerabilities
List each issue with: type, location, risk level (Critical/High/Medium/Low)

## ⚡ Performance Issues
List each issue with: location, current problem, suggested fix

## 📋 Priority Fix Order
Numbered list of what to fix first and why

## ✅ Fixed Code
Complete rewritten code with ALL issues resolved and comments explaining each fix.

Here is the code:

{code}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": f"You are an expert {language} code reviewer."},
            {"role": "user",   "content": user_content}
        ],
        temperature=0.2,
        max_tokens=2000
    )

    return response.choices[0].message.content