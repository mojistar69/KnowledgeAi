from openai import OpenAI
import json
import os

client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key=os.getenv("sk-dJnOBZp2ELos63PhXwLlY15ORnLD5OtUCT5dO2dWRts2fLu3")
)

def get_word_meanings(verse: str):

    prompt = f"""
تو متخصص زبان عربی قرآن هستی.

برای آیه زیر، برای هر کلمه معنی فارسی کوتاه بنویس.

فقط JSON معتبر برگردان.

فرمت:

{{
  "words":[
    {{
      "word":"...",
      "meaning":"..."
    }}
  ]
}}

آیه:
{verse}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert in Quranic Arabic."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content.strip()
    text = text.replace("```json", "").replace("```", "")

    return json.loads(text)