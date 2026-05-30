
from crewai import Agent, LLM
import os
from dotenv import load_dotenv

load_dotenv()


def get_secret(key):
    try:
        import streamlit as st
        return st.secrets[key]
    except:
        return os.getenv(key)
    

llm = LLM(
    model = "groq/llama-3.3-70b-versatile",
    api_key=get_secret("GROQ_API_KEY"),
    temperature = 0.2, # low temperatur , more precise technical output
    max_tokens=1500 # writer agent needs more space
)

bug_detector = Agent(
    role = "Expert Bug Detector and Code Reviewer",

    goal =  (
        "Find logical bugs, broken conditionals, infinite loops, "
        "edge cases, null pointer issues, syntax mistakes, runtime "
        "errors, and hidden implementation flaws in the code."
    ),

    backstory =  (
        "A senior software engineer with 15+ years of experience "
        "in debugging large-scale production systems and competitive "
        "programming. Known for identifying hard-to-find bugs and "
        "writing highly optimized and reliable code."
    ),

    llm = llm,
    verbose = False
)


security_auditor = Agent(
    role = "Senior security Consultant",

    goal =  (
        "Identify security vulnerabilities, unsafe coding practices, "
        "API exposure risks, injection attacks, authentication flaws, "
        "hardcoded secrets, insecure dependencies, and data leaks."
    ),

    backstory = (
        "A cybersecurity expert with 20+ years of experience in "
        "application security, penetration testing, cloud security, "
        "and secure software architecture. Has audited enterprise "
        "systems handling millions of users."
    ),

    llm = llm,
    verbose = False
)



performance_optimizer = Agent(
    role = "Performance Optimization Expert",

    goal =  (
        "Detect slow algorithms, inefficient loops, memory leaks, "
        "database/query inefficiencies, scalability issues, and "
        "system design problems that slow down the application."
    ),

    backstory =  (
        "A systems performance engineer with 15+ years of experience "
        "working on high-scale distributed applications and optimizing "
        "products used by millions of users globally."
    ),

    llm = llm,
    verbose = False
)



code_writer = Agent(
    role = "Technical Report Writer",

    goal = (
        "Collect all findings from the bug detector, security auditor, "
        "and performance optimizer. Produce a structured review report "
        "AND a complete rewritten version of the code with all issues fixed."
    ),

    backstory =  (
        "An experienced technical architect and documentation expert "
        "who specializes in converting complex engineering analysis "
        "into clean, understandable, and actionable reports."
    ),

    llm = llm,
    verbose = False
)

