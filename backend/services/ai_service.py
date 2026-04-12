import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.mistral.ai/v1/chat/completions"
MODEL = "mistral-small"

def build_prompt(basic_analysis, stats, missing_values, graphs):
    return f"""
You are a data analyst.
Analyze the dataset and provide clear insights.
Basic info:
{basic_analysis}

Statistics:
{stats}

Missing values:
{missing_values}

Graphs:
{graphs}

Tasks:
1. Explain the dataset in simple terms
2. Highlight important patterns
3. Identify anomalies or trends 
4. Explain what the graphs show
5. Give actionable insights

Keep it clear and concise.
"""
def analyze_with_ia(prompt):
    try:
        response = requests.post(
            API_URL,
            headers = {
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json = {
                "model": MODEL,
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )
        data = response.json()

        return data["choices"][0]["message"]["content"]
    except Exception as e:
        return f"AI Error: {str(e)}"