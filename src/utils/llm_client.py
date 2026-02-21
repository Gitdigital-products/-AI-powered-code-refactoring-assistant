import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_refactor_suggestion(code, issues):
    # Format the AST issues into a readable string for the AI
    issue_summary = "\n".join([f"- {i['issue']} at line {i['line']}: {i['message']}" for i in issues])

    prompt = f"""
    You are a Senior Software Engineer. Refactor the following Python code.
    
    Focus on these identified issues:
    {issue_summary}
    
    Rules:
    1. Maintain existing functionality and logic.
    2. Use modern Python (3.10+) features.
    3. Improve readability and reduce complexity.
    4. Return ONLY the refactored code. No conversational text.

    Code:
    {code}
    """

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2, # Low temperature for consistent code
    )

    return response.choices[0].message.content
