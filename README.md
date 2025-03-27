# 🎥 AI Animation Feedback Tool

Get precise, structured animation feedback from Google's Gemini Pro on any video you upload — without needing to open a single animation forum post again.

---

## Features

- Upload animation videos directly via Postman or your frontend
- Automatically sends videos to Gemini 2.5 Pro Experimental for critique
- Returns detailed feedback: strengths, weaknesses, tech notes, career advice, etc.
- Re-analyze without re-uploading — feedback is idempotent
- FastAPI backend, modular structure, easy to extend

---

## Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/ai-animation-feedback.git
cd ai-animation-feedback
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your `.env`
```env
GEMINI_API_KEY=your-google-api-key-here
```

### 5. Run the server
```bash
uvicorn backend.main:app --reload
```

---

## API Endpoints

### `POST /upload?file=...`
Upload a video file. Accepts `.mp4`, `.mov`, `.gif`, `.png`, and `.jpg`.

- **Body (form-data):**
  - `file`: (UploadFile) Your animation clip (max 50MB)

- **Response:**
```json
{
  "message": "File uploaded successfully",
  "filename": "yourfile.mp4",
  "saved_path": "uploads/yourfile.mp4"
}
```

---

### `GET /feedback?filename=yourfile.mp4`
Gets AI feedback on a previously uploaded file.

- **Query Param:**
  - `filename`: (str) Name of file in `uploads/`

- **Response:**
```json
{
  "filename": "yourfile.mp4",
  "feedback": "1. Strengths: ... 2. Weaknesses: ..."
}
```

---

## Project Structure

```
backend/
├── main.py          # FastAPI entrypoint
├── services/
│   ├── analyze.py   # Handles Gemini logic
│   └── file_upload.py # Handles uploads
uploads/             # Uploaded video files
.env                 # Environment config
README.md            # This file :P
```

---

## Powered By

- [Google Generative AI SDK (Gemini)](https://ai.google.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Postman](https://www.postman.com/) for API testing

---

## Notes

- Only `.mp4`, `.mov`, `.gif`, `.png`, `.jpg` are allowed.
- Max file size = **50MB**.
- Gemini response is cached by filename — reuploads with same name will be overwritten.

---

## Author

Built with love by Jasper Wu.  
YouTube: [FrameCubed](https://www.youtube.com/@framecubed)

---

## License

MIT — use freely, remix bravely.
