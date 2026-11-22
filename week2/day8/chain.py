import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
from time import sleep

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("API Key kaha hai bhai")

client=Groq(api_key=my_api_key)

model="openai/gpt-oss-120b" 

JD = """
We are hiring a Backend Python Developer.

Requirements:
- Strong Python
- FastAPI or Django
- PostgreSQL
- Docker
- AWS
- REST APIs
- 2+ years of experience
"""

RESUME="""
Name: Rahul Sharma

Experience:
3 years as a Software Developer.

Skills:
Python, FastAPI, MySQL, Docker,
REST APIs, Git

Projects:
Built a food delivery backend using
FastAPI and MySQL.

Deployed applications using Docker.
"""
# function used for LLM call
def ask_llm(system_prompt,user_prompt):
    sys_msg={
        "role":"system",
        "content": system_prompt
    }
    user_msg={
        "role":"user",
        "content":user_prompt
    }
    messages=[sys_msg,user_msg]
    response=client.chat.completions.create(model=model,messages=messages)
    answer=response.choices[0].message.content
    return answer

def step1_res_extract(RESUME):
    # extract skills from resume
    print("STEP 1")
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the candidate resume provided.
    Only return skills no other informations. Do not invent any skills by your self. 
    Output Format:
    Skills should be seperated by commas. Just return comma seperated skills do not return any other filler information.
    """
    user_prompt=f"""
    Extract the skills from this resume 
    {RESUME}
    """
    #whenever u use variable in string use f before """" otherwise it consider as normal string
    return ask_llm(system_prompt,user_prompt)

def step2_JD_extract(JD):
    print("STEP 2")
    # extract skills from resume
    system_prompt="""
    You are a professional HR assistant. Extract the skills from the Job description provided.
    Only return skills no other informations. Do not invent any skills by your self. 
    Output Format:
    Skills should be seperated by commas. Just return comma seperated skills do not return any other filler information.
    """
    user_prompt=f"""
    Extract the skills from this JD 
    {JD}
    """
    return ask_llm(system_prompt,user_prompt)

def step3_match(candidate,jd):
    print("STEP 3")
    system_prompt="""
    You are a professional HR assistant. Compare the skills of candidate and the skills required in the JD and produce a final score between 1 and 100. Also produce a short verdict whether the candidate is a good fit for the role.
    """
    user_prompt=f"""
    Compare and match the skills
    JD:
    {jd}
    Candidate:
    {candidate}
    """
    return ask_llm(system_prompt,user_prompt)

candidate=step1_res_extract(RESUME)
print(candidate)
sleep(2) # whenever u call multiple LLM apply sleep
jd=step2_JD_extract(JD)
print(jd)
sleep(2)
score = step3_match(candidate,jd)
print(score)