from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI()

response = client.images.generate(
  model="dall-e-3",
  prompt="Create an elegant table setting with daffodils and vases, arranged on plates and glasses. A bouquet of spring flowers sits in the center as a centerpiece for wedding guests to enjoy during their meal at home. The soft yellow color adds warmth and vibrancy against grey concrete flooring. It's perfect for celebrating a special day or adding beauty to your dining area.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)