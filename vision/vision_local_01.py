# use vision by post url
import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================
import base64
import requests

# OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")

# Function to encode the image
def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

image_folder ="/Users/liuyuxiang/work/ai_vision/example_img/"

# Path to your image
image_path_01 = f"{image_folder}vomit.png"
image_path_02 = f"{image_folder}sick_dog.jpg"

# Getting the base64 string
base64_image_01 = encode_image(image_path_01)
base64_image_02 = encode_image(image_path_02)

headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}

payload = {
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "我的狗怎麼了?"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": f"data:image/jpeg;base64,{base64_image_01}"
          }
        }
      ]
    }
  ],
  "max_tokens": 1000
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json())