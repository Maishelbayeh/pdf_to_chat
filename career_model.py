import os
import json
import requests
import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume


API_URL = "https://api.openai.com/v1/chat/completions"

def chat_with_pdf(pdf_text, user_query):
    headers = {
        "Authorization": f"Bearer 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",
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