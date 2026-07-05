import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def predict_health(glucose, haemoglobin, cholesterol):

    prompt = f"""
You are a healthcare AI.

Analyze the following blood test values:

Glucose: {glucose}
Haemoglobin: {haemoglobin}
Cholesterol: {cholesterol}

Return ONLY valid JSON in this exact format:

{{
  "condition": "Healthy | Prediabetes | Diabetes Mellitus | Hypercholesterolemia | Anemia | Multiple Risk Factors",
  "risk_level": "Low | Medium | High",
  "recommendation": "One short recommendation under 20 words."
}}

Rules:
- The "condition" must be only the disease or health status name.
- Do not write sentences in the "condition".
- The "recommendation" should be concise.
- Return only JSON.
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        # Remove markdown fences if present
        text = text.replace("```json", "").replace("```", "").strip()

        return json.loads(text)

    except Exception as e:
        print(e)

        return {
            "condition": "Unknown",
            "risk_level": "Medium",
            "recommendation": "Consult a physician."
        }