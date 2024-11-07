from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from test import ChatSession
import cloudinary
from cloudinary.uploader import upload
import os
from youtube_search import YoutubeSearch



app = FastAPI()

# Configure your Cloudinary account
# cloudinary.config(
#     cloud_name="",
#     api_key="",
#     api_secret=""
# )

# # Configure CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Adjust this to specify allowed origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Adjust this to specify allowed HTTP methods
#     allow_headers=["*"],  # Adjust this to specify allowed headers
# )

chat_session = ChatSession()

class QueryRequest(BaseModel):
    query: str
    endpoint_id: Optional[str] = "predefined-openai-gpt4turbo"
    plugin_ids: Optional[list] = None

class UploadRequest(BaseModel):
    url: str

@app.post("/create_session/")
def create_session():
    try:
        chat_session.create_session()
        return {"session_id": chat_session.session_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/submit_query/")
def submit_query(request: QueryRequest):
    try:
        response = chat_session.submit_query(request.query, request.endpoint_id, request.plugin_ids)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload_image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        contents=await file.read()
        upload_result = upload(contents)
        url = upload_result.get("url")

        print(url)
        response = chat_session.upload_image(url)
        # print(response.json())
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload_youtube/")
def upload_youtube(request: UploadRequest):
    try:
        results = YoutubeSearch(f'Travel_vlogs for {request.query}', max_results=1).to_dict()

        url = f"https://www.youtube.com/watch?v={results[0]['id']}"
        print(url)

        youtube_rs = chat_session.upload_youtube(url)
        response = chat_session.submit_query("Tell me about famous travel places from youtube link given")
        
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/upload_docs/")
async def upload_docs(file: UploadFile = File(...)):
    try:
        contents=await file.read()
        upload_result = upload(contents)
        url = upload_result.get("url")

        print(url)
        response = chat_session.upload_docs(url)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/delete_chat_session/")
def delete_chat_session():
    try:
        chat_session.delete_chat_session()
        return {"message": "Session deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
