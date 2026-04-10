from fastapi import APIRouter, HTTPException
from services.data_service import load_file, basic_analysis, statistical_analysis, clean_data

router = APIRouter()

@router.post("/analyze")
def analyze(file_path: str):
    try:
        df = load_file(file_path)

        df = clean_data(df)

        basic = basic_analysis(df)
        stats = statistical_analysis(df)

        return {
            "basic_analysis": basic,
            "statistics": stats
        }
    
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))