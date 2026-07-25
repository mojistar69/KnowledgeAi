from openai import OpenAI
import json

client = OpenAI(
    base_url="https://api.gapgpt.app/v1",
    api_key="sk-j0cuDPqCqkSx7hLhdb49WPLwCLqAfYnMsEDse6aJKvENKeIC"
)


# =====================================================
# ترجمه واژگان
# =====================================================

def get_word_meanings(verse: str):

    prompt = f"""
تو متخصص زبان عربی قرآن هستی.

برای آیه زیر:

{verse}

واژگان مهم را استخراج کن و معنی فارسی هر کدام را بنویس.

فقط JSON معتبر برگردان.

فرمت خروجی:

{{
  "words":[
    {{
      "word":"",
      "meaning":""
    }}
  ]
}}
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

    text = response.choices[0].message.content

    if text is None:
        raise Exception("AI returned None")

    text = text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)


# =====================================================
# بینش هوشمند
# =====================================================

def get_ai_insight(verse: str):

    prompt = f"""
قوانین:

- فقط بر مفهوم آیه تکیه کن.
- از بیان مطالب غیرمستند یا اختلافات تفسیری خودداری کن.
- لحن پاسخ گرم، امیدبخش و روان باشد.
- متن برای مخاطب عمومی قابل فهم باشد.
- از تکرار مفهوم آیه در بخش‌های مختلف خودداری کن.
- هر بخش باید اطلاعات جدیدی نسبت به بخش قبلی ارائه دهد.
- lessons باید کاربردی باشد، نه صرفاً تکرار مفهوم آیه.
- action یک اقدام عملی باشد که کاربر بتواند امروز انجام دهد.
- prayer کوتاه و صمیمی باشد.
- فقط JSON معتبر برگردان.

{verse}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are an expert Quran scholar."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4
    )

    text = response.choices[0].message.content

    if text is None:
        raise Exception("AI returned None")

    text = text.strip()
    text = text.replace("```json", "")
    text = text.replace("```", "")

    return json.loads(text)