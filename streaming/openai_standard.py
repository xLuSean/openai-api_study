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
    messages=[
        {'role': 'user', 'content': 'Count to 100, with a comma between each number and no newlines. E.g., 1, 2, 3, ...'}
    ],
    temperature=0,
)
# calculate the time it took to receive the response
response_time = time.time() - start_time

# print the time delay and text received
# print(f"Full response received {response_time:.2f} seconds after request")
# print(f"Full response received:\n{response}")

reply = response.choices[0].message
print(f"Extracted reply: \n{reply}")

reply_content = response.choices[0].message.content
print(f"Extracted content: \n{reply_content}")
