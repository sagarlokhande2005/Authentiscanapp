import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_USER = os.getenv("API_USER")
API_SECRET = os.getenv("API_SECRET")

def check_image(image_path):
    url = "https://api.sightengine.com/1.0/check.json"

    with open(image_path, "rb") as img:
        files = {"media": img}
        data = {
            "models": "genai",
            "api_user": API_USER,
            "api_secret": API_SECRET
        }

        response = requests.post(url, files=files, data=data)
        result = response.json()

    if "type" in result and "ai_generated" in result["type"]:
        score = result["type"]["ai_generated"]
        percent = round(score * 100, 2)

        if score > 0.5:
            return (
                f"🤖 AI Generated Image — {percent}%",
                "This image shows synthetic texture patterns, overly smooth surfaces, "
                "and lighting inconsistencies commonly produced by AI models."
            )
        else:
            return (
                f"📸 Real Image — {100 - percent}%",
                "This image shows natural texture variations, realistic lighting, "
                "and camera noise typical of real photographs."
            )

    return ("❌ Detection Failed", "Unable to analyze the image.")