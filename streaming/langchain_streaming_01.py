##########################################################################
### basic streaming example from langchain website
##########################################################################
from dotenv import load_dotenv
load_dotenv()
from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0, max_tokens=512)
# llm = OpenAI(model="gpt-3.5-turbo", temperature=0, max_tokens=512) # not support
for chunk in llm.stream("Write me a song about sparkling water."):
    print(chunk, end="", flush=True)