import google.generativeai as genai

def get_animation_feedback(animation_description: str):
    """
    Sends an animation description to Gemini and retrieves feedback.
    
    Params:
    - animation_description (str): The description of the animation.

    Returns:
    - str: AI-generated feedback or an error message.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")
        
        # Ensure we actually got a valid input
        if not animation_description.strip():
            return "⚠️ Error: The animation description cannot be empty."

        response = model.generate_content(
            f"You are an expert animation critic. Provide detailed feedback on this animation: {animation_description}"
        )
        
        # Ensure a valid response was received
        if not response.text:
            return "⚠️ Error: No response received from the AI model."
        
        return response.text

    except genai.types.NotFoundError:
        return "⚠️ Error: The specified AI model was not found. Check the model name."
    
    except genai.types.PermissionDeniedError:
        return "⚠️ Error: API access is denied. Check your API key and permissions."
    
    except genai.types.ResourceExhaustedError:
        return "⚠️ Error: You've exceeded your API quota. Try again later or check your plan."

    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"
