# using langchain_openai library to process image and texts

import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
import base64

def encode_image(image_bytes: bytes):
    return base64.b64encode(image_bytes).decode('utf-8')

def openai_vision(question, image_content):
    encoded_image = encode_image(image_content)

    chat = ChatOpenAI(model="gpt-4-vision-preview", max_tokens=1500)
    response = chat.invoke(
       [
          HumanMessage(
             content=[
                {"type": "text", "text": f"{question}"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{encoded_image}",
                        "detail": "auto",
                        },
                    },
                ]
            ),
            SystemMessage(content=f"Never apologize!\
                          Never apologize!\
    Please respond user with Chinese!\
    Please respond user with Chinese!\
    Never ask user to consult with a medical expert or a veterinarian! \
    Never ask user to consult with a medical expert or a veterinarian!\
    Never ask user to consult with a medical expert or a veterinarian!"
                          )
        ]
    )

    return response.content