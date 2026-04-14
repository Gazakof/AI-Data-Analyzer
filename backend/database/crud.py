import json
from  database.db import get_connection

def save_analysis(data):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO analyses (
        filename,
        file_path,
        basic_analysis,
        statistics,
        missing_values,
        graphs,
        ai_insights
    )
    VALUE (%s, %s, %s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        data["filename"],
        data["file_path"],
        json.dumps(data["basic_analysis"]),
        json.dumps(data["statistics"]),
        json.dumps(data["missing_values"]),
        json.dumps(data["graphs"]),
        json.dumps(data["ai_insights"])
    ))

    conn.commit()
    cursor.close()
    conn.close()