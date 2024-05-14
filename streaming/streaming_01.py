from dotenv import load_dotenv
load_dotenv()

import time  # for measuring time duration of API calls
from openai import OpenAI
import os

# Example of an OpenAI ChatCompletion request
# https://platform.openai.com/docs/guides/text-generation/chat-completions-api

# record the time before the request is sent
start_time = time.time()

client = OpenAI()
# send a ChatCompletion request to count to 100
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    # messages=[
    #     {'role': 'user', 'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
    # ],
    messages=[{'role':'user', 'content':'What is the capital of France?'}],
    temperature=0,
    stream=True
)

for chunk in response:
    # print(chunk)
    print(chunk.choices[0].delta.content)
    print("****************")