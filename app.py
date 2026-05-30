
import streamlit as st
from reviewer import run_review

st.set_page_config(page_title="AI Code Reviewer", page_icon="🔍")
st.title("🔍 AI Code Reviewer")
st.caption("Paste your code — get bugs, security issues, performance fixes, and corrected code.")

language = st.selectbox("Language",
    ["Python", "JavaScript", "Java", "C++", "C#", "SQL", "Other"])

code = st.text_area("Paste your code here", height=300,
    placeholder="def my_function():\n    pass")

if st.button("🔍 Review My Code"):
    if not code.strip():
        st.warning("Please paste some code first.")
    else:
        with st.spinner("Reviewing your code..."):
            result = run_review(code, language)

        st.success("Review complete!")

        if "## ✅ Fixed Code" in result:
            parts = result.split("## ✅ Fixed Code", 1)
            st.markdown("## 📋 Review Report")
            st.markdown(parts[0])
            st.markdown("## ✅ Fixed Code")
            st.code(parts[1].strip(), language=language.lower())
        else:
            st.markdown(result)