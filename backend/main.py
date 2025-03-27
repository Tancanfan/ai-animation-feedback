from fastapi import FastAPI, UploadFile, File, Query
from backend.services.analyze import analyze_video_with_gemini
from backend.services.file_upload import save_uploaded_file
import os
from dotenv import load_dotenv
import google.generativeai as genai



dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".env"))
load_dotenv(dotenv_path)

# Get the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Gemini API key not found. Make sure it's set in the .env file.")

# Configure Gemini API with the key
genai.configure(api_key=api_key)

for model in genai.list_models():
    print(model.name)  # Print available model names

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "AI Animation Feedback API is running with Gemini!"}

@app.post("/upload")
async def upload_video(file: UploadFile = File(...)):
    file_path = await save_uploaded_file(file)  # Call helper function
    if isinstance(file_path, dict): return file_path  # Return error message 
    return {"message": "File uploaded successfully", 
            "filename": file.filename, 
            "saved_path": file_path}

@app.get("/feedback")
async def feedback(filename: str = Query(..., description="Name of the uploaded animation file")):
    file_path = os.path.join("uploads", filename)
    if not os.path.exists(file_path):
        return {"error": f"File '{filename}' not found."}
    feedback_response = analyze_video_with_gemini(file_path)
    return {
        "filename": filename, 
        "feedback": feedback_response
        }