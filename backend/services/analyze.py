from google import genai
from pathlib import Path
import time
import os


model = "gemini-1.5-pro-latest"
prompt = f"""You are an expert animation critic. 
        You provide detailed feedback on animation.
        Analyze timing, weight, anticipation, staging, 
        appeal, follow-through, overlapping action, 
        squash and stretch, arcs, smoothness, 
        pose or silhouette readability, timing, spacing,
        exxaeration, secondary aaction, emotion, and expression 
        where applicable.        
        Provide detailed feedback on animation data.
        You will strucutre your feedback as follows:
        1. 💪 Strengths: Explain what you liked.
        2. 📉 Weaknesses: Detail areas for growth.
        3. 🔨 Technical feedback: Provide practical tips on improvements.
        4. 🎨 Artistic feedback: Offer creative suggestions.
        5. 🌟 Overall feedback: Summarize your thoughts.
        6. 📝 Assessed skill level: Beginner, Intermediate, Advanced
        **Return your response with the exact numbering and headings as listed above.**    
        """

def analyze_video_with_gemini(file_path: str):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    # Sends video file to Gemini for analysis
    try:
        #Upload the video file
        media_path = Path(file_path)
        uploaded_file = client.files.upload(file=media_path)
        while True:
            uploaded_file = client.files.get(name=uploaded_file.name)
            state = uploaded_file.state.name

            if state == "ACTIVE":
                break
            elif state == "FAILED":
                raise RuntimeError("❌ File processing failed.")
            
            print(f"Current file state: {state}")
            time.sleep(5)

            
        result = client.models.generate_content(
            model=model, contents=[uploaded_file, prompt]
            )
    
        return result.text
        # return 0
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"

if __name__ == "__main__":
    for model in genai.list_models():
        print(model.name)
