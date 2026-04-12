import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

def build_prompt(basic_analysis, stats, missing_values, graphs):
    return f"""
You are a data analyst.
Analyze the dataset and respond in JSON format (Return ONLY valid JSON, No explanation, No markdown):
{{
  "summary": "...",
  "key_insights": ["...", "..."],
  "anomalies": ["...", "..."],
  "graph_explanations": ["...", "..."]
}}
Data:
{basic_analysis}
{stats}
{missing_values}
{graphs}
"""

def analyze_with_ia(prompt):
    try:
        response = requests.post(
            API_URL,
            headers = {
                "Content-Type": "application/json"
            },
            json = {
                "contents": [
                    {
                        "parts": [
                            { "text": prompt }
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7,
                    "maxOutputTokens": 2000
                }
            }
        )

        if response.status_code != 200:
            return f"Erreur API: {response.status_code} - {response.text}"

        data = response.json()

        if "candidates" not in data:
            return f"Réponse inattendue: {data}"

        return data["candidates"][0]["content"]["parts"][0]["text"]
    
    except Exception as e:
        return f"AI Error: {str(e)}"