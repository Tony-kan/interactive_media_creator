import streamlit as st
from clarifai.client.model import Model
import base64
from dotenv import load_dotenv
from PIL import Image
from io import BytesIO

load_dotenv()
import os

clarifai_pat = os.getenv("CLARIFAI_PAT")
openai_api_key = os.getenv("OPEN_AI")


def generate_image(user_description,api_key):
    
    
    prompt=f"You are a professional comic artist. 
        Based on the below user's description and content, 
        create a proper story comic: {user_description}"

    inference_params = dict(quality="standard",size="1024x1024")
    model_prediction=Model(
        f"https://clarifai.com/openai/dall-e/models/dall-e-3?api_key={api_key}").predict_by_bytes(
        prompt.encode(),input_type="text",inference_params=inference_params
    )

    output_base64 = model_prediction.outputs[0].data.image.base64
    with open("generated_image.png", "wb") as f:
        f.write(output_base64)

    return "generated_image.png"


def understand_image(base64_image,api_key):
    prompt = f"Analyze the content of this image and write a creative,
                engaging story that brings the scene to life.
                Describe the characters, setting, 
                and actions in a way that would captivate a young audience:"
    inferenece_params = dict(temperature=0.2,image_base64=base64_image,api_key=api_key)
    model_prediction=Model(
              "https://clarifai.com/openai/chat-completion/models/gpt-4-vision"
    ).predict_by_bytes(
        prompt.encode(),input_type="text",inference_params=inferenece_params
    )  
    
    return model_prediction.outputs[0].data.text.raw
  
    def encode_image(image_path):
        with open(image_path,"rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')
