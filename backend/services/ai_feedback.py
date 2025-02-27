import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

def get_aniamtion_feedback(animation_description: str):
    client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))

    # Send request to OpenAI
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert animation critic. Provide detailed feedback on animation techniques."},
            {"role": "user", "content": f"Analyze this animation: {animation_description}"}
        ]
    )

    return response.choices[0].message["content"]