import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the OpenAI API key securely
openai_api_key = os.getenv("OPENAI_API_KEY")
API_URL = "https://api.openai.com/v1/chat/completions"

def chat_with_pdf(pdf_text, user_query):
    headers = {
        "Authorization": f"Bearer {openai_api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": "You are an AI assistant analyzing the given PDF."},
            {"role": "user", "content": f"Here is the extracted text from a PDF:\n{pdf_text}"},
            {"role": "user", "content": user_query}
        ]
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"
