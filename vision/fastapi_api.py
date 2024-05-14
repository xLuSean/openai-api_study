import os
from dotenv import load_dotenv
load_dotenv()
#===========================================================
from fastapi import FastAPI, File, UploadFile, Form
from typing import Union
from pydantic import BaseModel
from typing import Optional
from vision_function03 import openai_vision
# NOTE:1. one pic request is cost around 1k token, so we may need to block frequent request 2.limit user request 3. limit the image size

### OpenAI API Key
api_key = os.getenv("OPENAI_API_KEY")
headers = {
  "Content-Type": "application/json",
  "Authorization": f"Bearer {api_key}"
}
###

app = FastAPI()



# for test
@app.get("/sean")
async def root():
    return {"message": "Hello World"}

@app.post("/upload-image")
async def upload_image(master_id: Optional[str] = Form(None), question: str = Form(...) ,image: UploadFile = File(...)):
    # Read the image as bytes
    image_content = await image.read()
    # content, usage = openai_vision(question, image_content)
    # qa_slot = {"master_id":master_id, "question":question ,"response": content, "usage": usage}
    content = openai_vision(question, image_content)
    qa_slot = {"master_id":master_id, "question":question ,"response": content}
    return qa_slot


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fastapi_api:app", host='0.0.0.0', port=8000, reload=True)