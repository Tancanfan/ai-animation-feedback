from fastapi import FastAPI, UploadFile, File, HTTPException
from backend.services.ai_feedback import get_animation_feedback
import os
from dotenv import load_dotenv
import google.generativeai as genai

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv(dotenv_path)

# Get the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found. Make sure it's set in the .env file.")

# Configure Gemini API with the key
genai.configure(api_key=api_key)

for model in genai.list_models():
    print(model.name)  # Print available model names

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Animation Feedback API is running with Gemini!"}

@app.post("/upload")
async def upload_animation(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "File received!"}



@app.get("/feedback")
async def feedback(animation_description: str):
    """
    Fetch AI-generated animation feedback.

    **Params:**
    - `animation_description` (str): A brief text describing the animation.

    **Returns:**
    - JSON response containing the AI's feedback.
    """
    try:
        ai_response = get_animation_feedback(animation_description)

        # If the response is an error message, raise an HTTPException
        if ai_response.startswith("⚠️ Error:"):
            raise HTTPException(status_code=400, detail=ai_response)

        return {"feedback": ai_response}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"⚠️ Server error: {str(e)}")