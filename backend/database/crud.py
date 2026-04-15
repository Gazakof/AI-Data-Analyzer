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

def get_analyses():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM analyses ORDER BY upload_date DESC")
    
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append(dict(zip(columns,row)))

    cursor.close()
    conn.close()

    return result