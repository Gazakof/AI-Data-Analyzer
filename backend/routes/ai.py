import json
import os
import uuid
from fastapi import APIRouter, HTTPException
from services.data_service import load_file, basic_analysis, statistical_analysis, missing_values, suggest_graphs
from services.ai_service import build_prompt, analyze_with_ia

UPLOAD_DIR = "uploads"
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
        text = ai_result

        try:
            text = text.strip()
            if text.startswith("```"):
                text = text.replace("```json","").replace("```", "")
            
            start = text.find("{")
            end = text.rfind("}")

            if start != -1 and end != -1:
                text = text[start:end + 1]

            ai_json = json.loads(text)
        except:
            ai_json = {"raw_text": text}

        file_id = str(uuid.uuid4())[:6]
        json_file_name = f"{file_id}_analysis.json"
        json_file_path = os.path.join(UPLOAD_DIR, json_file_name)

        with open(json_file_path, "w", encoding = "utf-8") as f:
            json.dump(ai_json, f, indent = 4, ensure_ascii = False)

        return{
            "insights": ai_result,
            "file_path": json_file_path
        }
    except Exception as e:
        return HTTPException(status_code = 500, detail = str(e))