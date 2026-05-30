# AI Code Reviewer

A Streamlit app that reviews pasted code using Groq LLM and returns:
- bug and logic issue analysis
- security vulnerability findings
- performance improvement suggestions
- fixed code output

## Project Files
- `app.py` — Streamlit UI
- `reviewer.py` — Groq client and review logic
- `agents.py`, `tasks.py` — project support files
- `.env` — local secrets file (should not be pushed)
- `requirements.txt` — Python dependencies

## Setup

1. Create and activate a Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file with your Groq API key:
```text
GROQ_API_KEY=your_groq_api_key_here
```

4. Run the app:
```bash
streamlit run app.py
```

## Notes
- Keep `.env` secret and do not commit it.
- If you deploy to Streamlit Cloud, use Streamlit Secrets rather than `.env`.

## Push to GitHub

If the repository is already initialized and has a remote:

```bash
cd /Users/bharathkumarvnaik/Downloads/programing/AI_projects/ai_code_reviewer
git add README.md
git commit -m "Add project README"
git push origin main
```

If you still need to add the remote:

```bash
cd /Users/bharathkumarvnaik/Downloads/programing/AI_projects/ai_code_reviewer
git add README.md
git commit -m "Add project README"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```
