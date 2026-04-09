import os
import shutil
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

now = datetime.now().strftime("%Y%m%d_%H%M%S")
ALLOWED_EXTENSIONS = ["csv","xlsx"]
UPLOAD_DIR = "uploads"
MAX_FILE_SIZE = 60 * 1024 * 1024        # 60Mo

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename

    if not filename: 
        raise HTTPException(status_code = 400, detail = "No file provided")
    
    #Vérifier extension
    ext = filename.split(".")[-1]
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code = 400, detail = "File type not allowed")
    
    contents = await file.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code = 400, detail = "File too large")
    
    if file.size == 0:
        raise HTTPException(status_code = 400, detail = "Empty file")
    
    #remettre la lecture au debut
    file.file.seek(0)
    
    #Créer nom unique
    unique_filename = f"{now}_{filename}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    #Sauvegarde
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception:
        raise HTTPException(status_code = 500, details = "Error saving file")
    
    return {
        "filename": unique_filename,
        "path": file_path,
        "message": "File received successfully"
    }