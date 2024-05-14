# use vision by openai lib

import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================

import openai
import base64
image_folder ="/Users/liuyuxiang/work/ai_vision/example_img/"

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

# Path to your image
image_path_01 = f"{image_folder}vomit.png"
image_path_02 = f"{image_folder}sick_dog.jpg"
image_path_03 = f"{image_folder}dog-skin-disease.jpg"

# Getting the base64 string
base64_image_01 = encode_image(image_path_01)
base64_image_02 = encode_image(image_path_02)
base64_image_03 = encode_image(image_path_03)

def openai_vision(question):
    prompt = f"Combine what you learned from the image and the text to reframe user's question in detail.\
    reframed question should be in user's tone!\
    reframed question should be in user's tone!\
    reframed question should be in user's tone!\
    your full response should be in interrogative sentence\
    your full response should be in interrogative sentence\
    your full response should be in interrogative sentence\
    Never ask user to consult with a medical expert or a veterinarian! \
    Never ask user to consult with a medical expert or a veterinarian!\
    Never ask user to consult with a medical expert or a veterinarian!\
    Please respond user with Chinese!\
    Please respond user with Chinese!\
    Please respond user with Chinese!\
    User:{question}"


    # prompt = question # NOTE: test

    response = openai.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": f"{prompt}"},
            {
            "type": "image_url",
            "image_url": {
                "url": f"data:image/jpeg;base64,{base64_image_03}",
            },
            },
        ],
        }
    ],
    max_tokens=4096,  # default max tokens is low so set higher
    )
    return response
  

res = openai_vision("我的狗怎麼了？請仔細說明")
res = res.model_dump()

print(res.get("choices")[0].get("message").get("content"))