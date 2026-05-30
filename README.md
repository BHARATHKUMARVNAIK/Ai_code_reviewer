# AI Code Reviewer

An AI-powered code review tool that analyzes your code for bugs, security vulnerabilities, and performance issues — then rewrites it with all problems fixed.

🔗 **[Live Demo](https://aicodereviewer-52nerq5gxfq92cprdfbp8t.streamlit.app/)

---

## 📸 Demo

![AI Code Reviewer Screenshot](./Screenshot%202026-05-30%20at%204.41.41 PM.png)
<!-- Take a screenshot of your working app and add it to the repo -->

---

## ✨ Features

- 🐛 **Bug Detection** — logic errors, edge cases, null handling, runtime errors
- 🔒 **Security Audit** — SQL injection, hardcoded secrets, input validation, auth flaws
- ⚡ **Performance Analysis** — O(n²) loops, memory leaks, inefficient queries
- ✅ **Auto-Fix** — complete rewritten version of your code with all issues resolved
- 🌐 **Multi-language** — Python, JavaScript, Java, C++, C#, SQL

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| [Groq](https://groq.com) | LLM inference (Llama 3.3 70B) |
| [Streamlit](https://streamlit.io) | Web interface |
| [Python](https://python.org) | Core language |

---

## 🚀 Quick Start

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/ai-code-reviewer.git
cd ai-code-reviewer
```

**2. Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Create `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "your_groq_key_here"
```

Get a free key at [console.groq.com](https://console.groq.com) — no credit card needed.

**5. Run**
```bash
streamlit run app.py
```

---

## 💡 Example

Paste this into the app and see what it catches:

```python
def get_user(user_id):
    password = "admin123"
    query = "SELECT * FROM users WHERE id = " + user_id
    result = db.execute(query)
    for i in range(len(result)):
        for j in range(len(result)):
            print(result[i][j])
    return result
```

The reviewer will catch:
- SQL injection vulnerability
- Hardcoded password
- O(n²) nested loop
- Division by zero risk
- Undefined variable

---

## 📁 Project Structure

```
ai-code-reviewer/
├── app.py          ← Streamlit UI
├── reviewer.py     ← Groq client + review logic
├── requirements.txt
└── .streamlit/
    └── secrets.toml  ← API keys (never commit this)
```

---

## 🔑 Free APIs Used

| API | Purpose | Cost |
|-----|---------|------|
| Groq | LLM inference | Free tier |

---

## 📄 License

MIT — free to use and modify.

---

## 👤 Author
Bharath Kumar V Naik
