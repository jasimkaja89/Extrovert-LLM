import os
import requests
import gradio as gr
import random

# Define the Hugging Face API URL and retrieve the API key from environment variables
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"
API_KEY = os.getenv("HUGGINGFACE_API_KEY")

# Define the fixed question
QUESTION = "Create a creative advertisement about a new solution to the storrowing problem."

extrovert_prompts = [
    f"{QUESTION} Provide a lively and high-energy message.",
    f"{QUESTION} Create a bold, exciting advertisement.",
    f"{QUESTION} Share an enthusiastic, vibrant ad idea.",
    f"{QUESTION} Develop a high-energy promotional concept.",
    f"{QUESTION} Propose a dynamic and thrilling ad message.",
    f"{QUESTION} Present an engaging, energetic advertisement.",
    f"{QUESTION} Craft an upbeat, extroverted promotional message.",
    f"{QUESTION} Design a compelling, lively advertisement concept."
] * 50  # Replicates to create a pool of 400 options when shuffled


# Function to query the Hugging Face API
def query_huggingface():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    prompt = random.choice(extrovert_prompts)
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})

    if response.status_code == 200:
        return response.json()[0]['generated_text']
    else:
        return f"Error: {response.status_code}, {response.text}"

# Create Gradio interface
def create_extrovert_interface():
    return gr.Interface(
        fn=query_huggingface,
        inputs=None,
        outputs="text",
        title="Extrovert Profile",
        description="This interface provides an extroverted, lively response to the fixed question below.\n\n" + QUESTION
    )

# Launch interface
create_extrovert_interface().launch(server_name="0.0.0.0", server_port=7866)



