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
prompt="Sugggest a name for my clothing company."

# SYSTEM
message_sys = {
    "role" : "system",
    "content" : "You are a brand manager who suggests brand name for my company. name should be one word. sugeest one name only"
}

# in msg its role and content we need to pass
message = {
    "role" : role,
    # "prompt" : prompt   #msg dict key_name is content not prompt otherwise it gives u n error
    "content" : prompt
}

messages = [message_sys, message]
# Temperature By Default = 0, range [0,2]
response=client.chat.completions.create(model=model,messages=messages,temperature=0)
# ------------------------------------------------------------------------------------------------
# response=client.chat.completions.create(model=model,messages=messages)#gives u an error bcoz in msg keyname is prompt. keyname should be content. without adding temperature 
# check role-system, content-"" then role-user,content-prompt => here we tell the system about the role first and then give our promot accordingly
# print(response)

print("###########################################################################")
answer=response.choices[0].message.content  #main answer
print(answer)