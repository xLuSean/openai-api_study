# using opeai library to process image and texts

import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================
import base64
import requests
from langchain_openai import ChatOpenAI
from langchain_core.messages.human import HumanMessage

api_key = os.getenv("OPENAI_API_KEY")
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

def encode_image(image_bytes: bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def openai_vision(question, image_content):
    # chat = ChatOpenAI(model_name="gpt-4-vision-preview")

    encoded_image = encode_image(image_content)
    payload = {
    "model": "gpt-4-vision-preview",
    "messages": [
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{question}"
            },
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{encoded_image}"
            }
            }
        ]
        }
    ],
    "max_tokens": 1000
    }
    
    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
    except Exception as e:
        print(e)

    res = response.json()
    content = res.get("choices")[0].get("message").get("content")
    usage = res.get("usage")

    return content, usage