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
role="user"



#structure it
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    issue:str

schema=Ticket.model_json_schema()

response_format={
    "type":"json_object"
}

system_prompt=f"""
Extract personal information from the ticket strictly based on this schema and give a json output.
{schema}
"""

message_system={
    "role":"system",
    "content":system_prompt
}
text="My name is John. I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 12345"
prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text}
"""
# in msg its role and content we need to pass
message = {
    "role" : role,
    # "prompt" : prompt   #msg dict key_name is content not prompt otherwise it gives u n error
    "content" : prompt
}

messages = [message_system,message]

response=client.chat.completions.create(model=model,messages=messages,response_format=response_format)#gives u an error bcoz in msg keyname is prompt. keyname should be content

answer=response.choices[0].message.content  #main answer
print(answer)

# How to read it
import json
raw_json=answer
data_file=json.loads(raw_json)
ticket=Ticket(**data_file)

# Pass these information further
print(ticket.name)
print(ticket.email)
print(ticket.issue)

