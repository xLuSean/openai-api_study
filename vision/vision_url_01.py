import os
# from api_keys import OPENAI_API_KEY
# os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
from dotenv import load_dotenv
load_dotenv()
#===========================================================
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "這隻狗怎麼了?"},
        {
          "type": "image_url",
          "image_url": {
            # "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            #   "url":"https://www.papayapet.com/wp-content/uploads/2023/06/how-to-care-for-your-sick-dog-or-cat-header_66628_13728-960x569.jpg"
            #   "url":"https://twinmaplesvethospital.com/wp-content/uploads/2023/01/Vomiting-in-Dogs-featured.jpg"
              "url":"https://www.thesprucepets.com/thmb/fFyH0vHcOaQnnxel15hBZVIkLqI=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/dog-animal-skin-disease-1208313049-6c58143883d2477a920ca1ed1a7bc1e6.jpg"
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])