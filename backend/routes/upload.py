from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

ALLOWED_EXTENSIONS = ["csv","xlsx"]

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    filename = file.filename

    if not filename: 
        raise HTTPException(status_code = 400, detail = "No file provided")
    
    #Vérifier extension
    ext = filename.split(".")[-1]
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code = 400, detail = "File type not allowed")
    
    return {
        "filename": filename,
        "message": "File received successfully"
    }