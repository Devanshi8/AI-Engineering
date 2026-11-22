import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b" 
prompt = "Explain how internet works."
message={
    "role":"user",
    "content":prompt
}
messages = [message]
# ===============================================================================
# # without streaming as by default stream = false
# response1 = client.chat.completions.create(model=model,messages=messages)
# # print(response1)
# answer=response1.choices[0].message.content
# print(answer)
# ===============================================================================
# with streaming  add stream=true and response data comes chunk by chunk
stream = client.chat.completions.create(model=model,messages=messages,stream=True)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True) # print immediately as chunk arrived