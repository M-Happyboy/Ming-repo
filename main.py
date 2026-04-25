import os
import gradio as gr
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Google AI Studio
if api_key:
    genai.configure(api_key=api_key)
else:
    print("Warning: GOOGLE_API_KEY not found in environment.")

def describe_image(input_image):
    if not api_key:
        return "Error: GOOGLE_API_KEY not found. Please add your key to the .env file."
    
    if input_image is None:
        return "Please upload an image first."

    try:
        # Initialize the model
        model = genai.GenerativeModel(model_name="gemma-4-31b-it")
        
        # System prompt to enforce detailed analysis and length constraint
        prompt = (
            "Provide a comprehensive visual analysis of this image. "
            "Describe the composition, lighting, colors, key objects, and the overall mood or narrative. "
            "Be specific and thorough. Your response MUST be between 3 and 5 sentences long."
        )
        
        # Generate content
        response = model.generate_content([prompt, input_image])
        return response.text
        
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Gradio UI Definition
with gr.Blocks(title="AI Image Describer") as demo:
    gr.Markdown("# 🖼️ AI Image Describer")
    gr.Markdown("Upload an image to get a detailed 3-5 sentence visual analysis using Gemma-4.")
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="pil", label="Upload Image")
            submit_btn = gr.Button("Describe Image", variant="primary")
        
        with gr.Column():
            text_output = gr.Textbox(label="Detailed Analysis", interactive=False)

    submit_btn.click(
        fn=describe_image,
        inputs=image_input,
        outputs=text_output
    )

if __name__ == "__main__":
    demo.launch()
