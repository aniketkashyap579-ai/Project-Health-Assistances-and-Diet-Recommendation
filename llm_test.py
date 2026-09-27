

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
HF_token=os.getenv("HF_TOKEN")

Client=OpenAI(base_url="http://router.huggingface.co/v1",
              api_key=HF_token)
response=Client.chat.completions.create(model="openai/gpt-oss-120b",
                               messages=[{
                                   "role":"user",
                                   "content":"what is good source of protein in Vegetarian"
                               }])
answer=response.choices[0].message.content

print(answer)
