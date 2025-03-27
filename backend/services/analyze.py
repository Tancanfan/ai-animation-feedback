from google import genai
from pathlib import Path
import time
import os


model = "gemini-2.5-pro-exp-03-25"
prompt = f"""You are an expert animation instructor. 
        Consider the context of the animation and provide feedback on the quality of the animation 
        based on overall impressions.
        Remember to be constructive in your feedback. 
        
        If you see a learning opportunity, take the time to explain it
        and be a sort of mentor to the animator. If something can be fixed, 
        give actionable feedback with specific instructions if possible.

        If there is a void background, consider if it is a test animation or a final product.
        Give praise where it's deserved, and be specific about what you like. Be encouraging.

        If this were for an animation reel, how is it? Is the animator ready for a job in the industry?

        Here are some specific termininlogies to consider. Please only use them if they are relevant to the animation.
        You DO NOT have to go down the entire list. It's just for reference:
        - The Invisible Suitcase Syndrome: When a character (usually in 3d animation) has their arms
        parented to the root bone, rather than the uppermost spine bone, causing them to move independently
        of the body. This is mainly an issue if the arms are not pressed up against something like a table
        or wall. So, make sure you consider the context.
        - The Nonsexual Insertion Method: When an animation has heavy focus on joint design, pay attention
        to the way the joints are designed. If they are plain cylinders, suggest a staggered design, wherein
        perhaps the center of one joint is extruded inward, and the connecting joint is extruded outward.
        This is just one example of a nonsexual insertion method. Obviously, there are more involved applications.
        - The 12 Principles of Animation: These are the basic principles that every animator should know.
        - Googling: If something seems like it is very lacking in foundational knowledge, suggest that the animator
        google it. This is a good way to learn more about animation.
        - The Rule of Thirds: This is a basic composition principle that can be applied to animation. The exception
        is if the animation is a test animation, in which case the rule of thirds may not apply.
        - Texturinig: If the animation has textures, consider how the textures are applied. If the style is
        realism, assess the quality accordingly. If the style is more abstract, consider how the textures contribute
        to the overall aesthetic. If there are no textures, consider if the animation is a test animation or a final product.
        Provide two branches of feedback if you are unsure if it is a test animation or a final product.
        - The 180 Degree Rule: This is a basic rule of cinematography that can be applied to animation. If the animation
        seems to break this rule, suggest that the animator google it. If it is intentional, consider the story implications.   
        - Blender's Industry Compatible Keymaps: If the animation is made in Blender, suggest that the animator use
        Blender's industry compatible keymaps. This will make it easier for them to transition to other software.
        Additionally, i will speed up the workflow significantly. The basic workflow involves using "W", "E", "R",
        "MMB", "LMB", "RMB", and "Alt" as the primary keys. As for secondary actions remember that using "Tab" will
        bring up the search menu to allow users to instantly look up any commands needed at a high level.
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
