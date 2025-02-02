import os
import streamlit as st
from dotenv import load_dotenv
from resume_parser import parse_resume
from career_model import chat_with_pdf

# Load environment variables
load_dotenv()

# Streamlit app
st.title("PDF Chat AI")
st.sidebar.header("Upload Your PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file:
    st.write("**Uploaded File:**", uploaded_file.name)
    
    try:
        # Parse the resume or document
        st.write("Extracting text from the PDF...")
        pdf_text = parse_resume(uploaded_file)
        st.text_area("Extracted Text", pdf_text, height=200)
        
        user_query = st.text_input("Ask a question about the document")
        if st.button("Get Answer") and user_query:
            response = chat_with_pdf(pdf_text, user_query)
            st.write("### AI Response:")
            st.text(response)
    
    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF file to start the chat.")
