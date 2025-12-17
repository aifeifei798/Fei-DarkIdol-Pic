import base64
import os
from PIL import Image # Pillow for image manipulation
from io import BytesIO

# Attempt to import the new Google Generative AI SDK
try:
    import google.generativeai as genai
    from google.generativeai.types import HarmCategory, HarmBlockThreshold # For safety settings, good practice
except ImportError:
    raise ImportError("Google Generative AI SDK not found. Please install it using 'pip install google-generativeai'")

# Initialize the Gemini client (using the new configure method)
try:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise KeyError("GEMINI_API_KEY environment variable not set.")
    genai.configure(api_key=api_key)
except KeyError as e:
    raise EnvironmentError(f"Configuration error: {e}")
except Exception as e:
    raise RuntimeError(f"An unexpected error occurred during genai configuration: {e}")

# Function to encode image to base64
def encode_image_to_base64(image_path_or_pil_image):
    """Encode the image to base64 with resizing."""
    try:
        if isinstance(image_path_or_pil_image, str): # if it's a filepath
            img = Image.open(image_path_or_pil_image).convert("RGB")
        elif isinstance(image_path_or_pil_image, Image.Image): # if it's already a PIL Image object
            img = image_path_or_pil_image.convert("RGB")
        else:
            print("Error: Input is not a valid filepath or PIL Image object.")
            return None

        # Resize the image to a height of 512 while maintaining the aspect ratio
        base_height = 512
        h_percent = (base_height / float(img.size[1]))
        w_size = int((float(img.size[0]) * float(h_percent)))
        img = img.resize((w_size, base_height), Image.Resampling.LANCZOS)

        # Convert the image to a byte stream
        buffered = BytesIO()
        img.save(buffered, format="JPEG") # Save as JPEG for consistency with mime_type
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return img_str
    except FileNotFoundError:
        print(f"Error: The file {image_path_or_pil_image} was not found.")
        return None
    except Exception as e:
        print(f"Error encoding image: {e}")
        return None

def feifeiflorence(image_input): # Gradio's Image component with type="filepath" gives a path
    """Generate a description for the given image using Gemini."""
    try:
        # Using a generally available and stable flash model supporting multimodal input
        model_name = "gemini-1.5-flash-latest"

        # Encode the image (Gradio provides a filepath for gr.Image type="filepath")
        base64_image = encode_image_to_base64(image_input)
        if not base64_image:
            return "Failed to encode image. Please check the image file and try again."

        # Prepare the image part for the model
        # Using genai.types.ImagePart or the dictionary format
        image_part = {
            "mime_type": "image/jpeg",
            "data": base64.b64decode(base64_image)
        }
        # Alternative using types (ensure 'from google.generativeai import types' or use genai.types)
        # from google.generativeai import types as genai_types
        # image_part_typed = genai_types.ImagePart(mime_type="image/jpeg", data=base64.b64decode(base64_image))


        # Configure the model and prompt
        model = genai.GenerativeModel(model_name)
        #prompt = "Please description flux prompt of this photo."
        prompt = "Please describe this image and generate a detailed English visual prompt suitable for the Flux text-to-image model."
        # Generate content
        response = model.generate_content([prompt, image_part]) # Pass image_part directly

        # Extract and return the description
        return response.text

    except genai.types.BlockedPromptException as e:
        print(f"Content generation blocked: {e}")
        return f"Content generation was blocked. Prompt feedback: {response.prompt_feedback if 'response' in locals() and hasattr(response, 'prompt_feedback') else 'N/A'}"
    except Exception as e:
        # Attempt to get more detailed error information if it's an API error
        error_message = str(e)
        if hasattr(e, 'message'): # Some API errors have a 'message' attribute
             error_message = e.message
        print(f"Error generating description: {error_message}")
        return f"An error occurred while generating the description: {error_message}. Please try again."