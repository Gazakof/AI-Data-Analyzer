from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG")

app = FastAPI(title=APP_NAME)

#CORS Configuration
origins = [
    "http://localhost:3000", #React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/")
def read_root():
    return {"message": "AI Data Analyzer API is running"}

@app.get("/config")
def get_config():
    return {
        "app_name": APP_NAME,
        "debug": DEBUG
    }