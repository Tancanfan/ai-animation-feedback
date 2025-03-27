import os
from fastapi import APIRouter, UploadFile, File
from pathlib import Path

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {".mp4", ".mov", ".gif", ".png", ".jpg"}  # Add valid file types
MAX_FILE_SIZE = 50 * 1024 * 1024  # 50MB limit


@router.post("/upload/")
async def save_uploaded_file(file: UploadFile) -> str:
    # Ensure file type is allowed
    ext = Path(file.filename).suffix.lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {ext}")

    # Ensure file isn't too large
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:
        raise ValueError("File is too large (max 50MB).")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    try:
        # Save the uploaded file
        with open(file_path, "wb") as buffer:
            buffer.write(contents)
        return file_path
    
    except Exception as e:
        raise RuntimeError(f"Error saving file: {e}")