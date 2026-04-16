from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv
from routes import upload, analyze, graph, ai, analysis

load_dotenv()

APP_NAME = os.getenv("APP_NAME")
DEBUG = os.getenv("DEBUG")

app = FastAPI(title=APP_NAME)

#CORS Configuration
origins = [
    "http://localhost:5173", #React
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

app.include_router(upload.router, prefix = "/api")
app.include_router(analyze.router, prefix = "/api")
app.include_router(graph.router, prefix = "/api")
app.mount("/uploads", StaticFiles(directory = "uploads"), name = "uploads")
app.include_router(ai.router, prefix = "/api")
app.include_router(analysis.router, prefix = "/api")

@app.get("/")
def read_root():
    return {"message": "AI Data Analyzer API is running"}

@app.get("/config")
def get_config():
    return {
        "app_name": APP_NAME,
        "debug": DEBUG
    }