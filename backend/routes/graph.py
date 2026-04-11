from fastapi import APIRouter, HTTPException
from services.data_service import load_file, suggest_graphs
from services.graph_service import generate_graph

router = APIRouter()

@router.post("/graphs")
def create_graphs(file_path: str):
    try:
        df = load_file(file_path)
        graphs = suggest_graphs(df)
        results = []

        for g in graphs:
            path = generate_graph(df, g["type"], d["column"])

            results.append({
                "type": g["type"],
                "column": g["column"],
                "path": path
            })
        
        return { "graphs": results }
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))