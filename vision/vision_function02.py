# using opeai library to process image and text

import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================
import base64
import openai

def encode_image(image_bytes: bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def openai_vision(question, image_content):
    encoded_image = encode_image(image_content)

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
                "url": f"data:image/jpeg;base64,{encoded_image}",
            },
            },
        ],
        }
    ],
    max_tokens=4096,  # default max tokens is low so set higher
    )
  
    res = response.model_dump()
    content = res.get("choices")[0].get("message").get("content")
    usage = res.get("usage")

    return content, usage