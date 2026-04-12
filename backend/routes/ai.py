from fastapi import APIRouter, HTTPException
from services.data_service import load_file, basic_analysis, statistical_analysis, missing_values, suggest_graphs
from services.ai_service import build_prompt, analyze_with_ia
import json

router = APIRouter()

@router.post("/ai-analysis")
def ai_analyis(file_path: str):
    try:
        df = load_file(file_path)

        basic = basic_analysis(df)
        stats = statistical_analysis(df)
        missing = missing_values(df)
        graphs = suggest_graphs(df)

        prompt = build_prompt(basic, stats, missing, graphs)

        ai_result = analyze_with_ia(prompt)

        return{
            "insights": ai_result
        }
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))