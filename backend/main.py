from fastapi import FastAPI, UploadFile, File
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
    ai_response = get_animation_feedback(animation_description)
    return {"feedback": ai_response}


# from fastapi import FastAPI, UploadFile, File
# from backend.services.ai_feedback import get_animation_feedback
# import os
# from dotenv import load_dotenv


# # Explicitly set .env path
# env_path = os.path.join(os.path.dirname(__file__), ".env")

# # Load environment variables
# if not load_dotenv(env_path):
#     print("⚠️ WARNING: Could not load .env file!")

# # Check API key
# api_key = os.getenv("OPENAI_API_KEY")
# if not api_key:
#     print("❌ ERROR: OPENAI_API_KEY is still None!")
# else:
#     print("✅ Loaded API Key:", api_key)

# print(get_animation_feedback("Test animation"))


# app = FastAPI()

# @app.post("/")
# async def root():
#     return {"message": "AI Animation Feedback API is running!"}

# @app.post("/upload")
# async def upload_animation(file: UploadFile = File(...)):
#     return {"filename": file.filename, "message": "File received!"}

# @app.get("/feedback")
# async def feedback(animation_description: str):
#     ai_response = get_animation_feedback(animation_description)
#     return {"feedback": ai_response}