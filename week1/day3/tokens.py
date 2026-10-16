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
role="system"
# 3 Prompts
prompt1="Hi!"
prompt2="Explain Time Travel in Detail but under 100 words"
prompt3="Write a 1000 word Essay on Machine Learning"

prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
        "role":role,
        "content":prompt
    }
    messages=[message]
    response=client.chat.completions.create(model=model,messages=messages,max_tokens=5000)
    usage=response.usage
    print(f"Prompt : {prompt} --> Your Tokens:{usage.prompt_tokens} completion_token:{usage.completion_tokens} Total Tokens:{usage.total_tokens} Finish Reason:{response.choices[0].finish_reason}")

# prompt="Do you know Padho with Pratyush"
# # in msg its role and content we need to pass
# message={
#     "role":role,
#     "content":prompt
# }

# messages=[message]

# response=client.chat.completions.create(model=model,messages=messages)
# print(response)

#-------------------------------------------------------------------------------
# 3 Prompts
# prompt1="Hi!"
# prompt2="Explain Time Travel in Detail"
# prompt3="Write a 1000 word Essay on Machine Learning"
# O/P:-
# Prompt : Hi! --> Your Tokens:72 completion_token:41 Total Tokens:113
# Prompt : Explain Time Travel in Detail --> Your Tokens:75 completion_token:2752 Total Tokens:2827
# Prompt : Write a 1000 word Essay on Machine Learning --> Your Tokens:80 completion_token:2356 Total Tokens:2436
#----------------------------------------------------------------------------------------
# 3 Prompts
# prompt1="Hi!"
# prompt2="Explain Time Travel in Detail  but under 100 words"
# prompt3="Write a 1000 word Essay on Machine Learning"
# O/P:-
# Prompt : Hi! --> Your Tokens:72 completion_token:50 Total Tokens:122
# Prompt : Explain Time Travel in Detail but under 100 words --> Your Tokens:80 completion_token:208 Total Tokens:288
# Prompt : Write a 1000 word Essay on Machine Learning --> Your Tokens:80 completion_token:2273 Total Tokens:2353
#----------------------------------------------------------------------------------------
# response=client.chat.completions.create(model=model,messages=messages,max_tokens=50)
#print(Finish Reason:{response.choices[0].finish_reason})
# Finish Reason = stop-> natural || length->due to tokens limit
    #O/P:-
# Prompt : Hi! --> Your Tokens:72 completion_token:50 Total Tokens:122 Finish Reason:length
# Prompt : Explain Time Travel in Detail but under 100 words --> Your Tokens:80 completion_token:50 Total Tokens:130 Finish Reason:length
# Prompt : Write a 1000 word Essay on Machine Learning --> Your Tokens:80 completion_token:50 Total Tokens:130 Finish Reason:length

#----------------------------------------------------------------------------------------
# response=client.chat.completions.create(model=model,messages=messages,max_tokens=500)
   #O/P:-
# Prompt : Hi! --> Your Tokens:72 completion_token:70 Total Tokens:142 Finish Reason:stop
# Prompt : Explain Time Travel in Detail but under 100 words --> Your Tokens:80 completion_token:272 Total Tokens:352 Finish Reason:stop
# Prompt : Write a 1000 word Essay on Machine Learning --> Your Tokens:80 completion_token:500 Total Tokens:580 Finish Reason:length