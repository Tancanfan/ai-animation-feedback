import os
from dotenv import load_dotenv
from openai import OpenAI
import google.generativeai as genai



def get_animation_feedback(animation_description: str):
    """
    Sends an animation description to Gemini Pro and retrieves feedback.
    """
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    response = model.generate_content(f"You are an expert animation critic. Provide detailed feedback on this animation: {animation_description}")

    return response.text

# def get_animation_feedback(animation_description: str):
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#     print("📌 Retrieving available models...")
    
#     try:
#         models = client.models.list()
#         print("✅ Models retrieved:")
#         for model in models:
#             print("➡️", model.id)
#     except Exception as e:
#         print("❌ Error retrieving models:", str(e))
#         return "Error: Unable to retrieve models."


# def get_animation_feedback(animation_description: str):
#     client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#     response = client.chat.completions.create(
#         model="gpt-4o",
#         messages=[
#             {"role": "system", "content": "You are an expert animation critic."},
#             {"role": "user", "content": f"Analyze this animation: {animation_description}"}
#         ]
#     )
#     return response.choices[0].message["content"]

