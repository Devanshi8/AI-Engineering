import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("Where is API key")

client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"

def llm_ans(prompt):
    message={
        "role":"user",
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages)
    ans=response.choices[0].message.content
    return ans

bad_prompt="""
#ROLE:
You are a support assistant at a mobile/laptop company.
#TASK
You have to classify the issue in a category
#CONSTRAINT
You have to classify the issue into three categories namely billing,technical, return
#OUTPUT FORMAT
Your answer should be one word only. The one word should be one of the categories given in constraints
#EXAMPLE
For instance if s user complain says he wants a refund then category is Return 
#FALLBACK
If the issue is unrelated to any of these categories mentioned in constraints, then the answer should be OTHER
This is a user complaint:
my gasstove is not working
"""
print(llm_ans(bad_prompt))