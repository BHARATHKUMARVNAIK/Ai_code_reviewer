
'''  

Bug Detector    ┐
Security Auditor├→ all run at same time → Code Writer (waits for all 3)
Perf Optimizer  ┘

''' 

from crewai import Task
from agents import bug_detector, security_auditor, performance_optimizer, code_writer

def create_tasks(code: str):

    bug_task = Task(
        description=f"Review this code and identify ALL bugs, logic errors, edge cases:\n\n{code}\n\nBe specific — cite exact line or function.",
        expected_output="Numbered list of bugs with: location, what's wrong, why it's a problem, severity (High/Medium/Low).",
        agent=bug_detector
    )

    security_task = Task(
        description=f"Perform a full security audit of this code:\n\n{code}\n\nCheck for injection, hardcoded secrets, auth issues, data exposure.",
        expected_output="Numbered list of vulnerabilities with: type, location, risk level (Critical/High/Medium/Low), explanation.",
        agent=security_auditor
    )

    performance_task = Task(
        description=f"Analyse performance of this code:\n\n{code}\n\nFind slow algorithms, unnecessary loops, memory leaks, missing caching.",
        expected_output="Numbered list of performance issues with: location, current complexity, suggested fix, expected improvement.",
        agent=performance_optimizer
    )

    writer_task = Task(
        description="""Using ALL findings from the bug detector, security auditor, and performance optimizer:

        1. Write a structured review report with sections:
           - Critical Issues
           - Security Vulnerabilities
           - Performance Problems
           - Priority fix order

        2. rite the COMPLETE fixed version of the original code.
            You MUST include the full corrected code at the end.
            Do not skip the fixed code — it is required.
        """,
        
        expected_output="""A full review report followed by the heading 
            '## Fixed Code' and the complete corrected code block.""",

        agent=code_writer,
        context=[bug_task, security_task, performance_task]  # ✅ waits for all 3
    )

    return bug_task, security_task, performance_task, writer_task