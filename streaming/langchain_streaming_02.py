##########################################################################
### example found on pinecone github
### https://github.com/pinecone-io/examples/blob/master/learn/generation/langchain/handbook/09-langchain-streaming/09-langchain-streaming.ipynb
##########################################################################
from dotenv import load_dotenv
load_dotenv()
# from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.schema import HumanMessage

llm = ChatOpenAI(
    # model="gpt-3.5.turbo",
    temperature=0,
    streaming=True,
    callbacks=[StreamingStdOutCallbackHandler()] # !!!streaming!!!
    )

messages = [HumanMessage(content="tell me a short story")]

res = llm.invoke(messages)
print(res)