from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = """
You are a coding AI assistant.
You help the user write, fix, and explain code.
Be correct, short, and useful.
"""

def ask_ai(messages):
    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages
    )
    return res.choices[0].message.content
