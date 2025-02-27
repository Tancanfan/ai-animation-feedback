from fastapi import FastAPI, UploadFile, File

app = FastAPI()

@app.post("/")
async def root():
    return {"message": "AI Animation Feedback API is running!"}

@app.post("/upload")
async def upload_animation(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "File received!"}

@app.get("/feedback")
async def feedback(animation_description: str):
    ai_response = get_animation_feedback(animation_description)
    return {"feedback": ai_response}