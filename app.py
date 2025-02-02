import os
import streamlit as st
from dotenv import load_dotenv
from ExtractText import ExtractText
from OpenAiService import chat_with_pdf

# Load environment variables
load_dotenv()

# Streamlit app
st.title("PDF Chat AI")
st.sidebar.header("Upload Your PDF")
uploaded_file = st.sidebar.file_uploader("Choose a PDF file", type=["pdf"])

# Initialize session state for conversation history and query count
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "query_count" not in st.session_state:
    st.session_state.query_count = 0

# Button to clear history
if st.button("Clear History"):
    st.session_state.conversation = []
    st.session_state.query_count = 0
    st.success("Conversation history cleared!")

if uploaded_file:
    st.write("**Uploaded File:**", uploaded_file.name)
    
    try:
        # Parse the resume or document
        st.write("Extracting text from the PDF...")
        pdf_text = ExtractText(uploaded_file)
        st.text_area("Extracted Text", pdf_text, height=200)

        # Handle user queries
        if st.session_state.query_count < 10:
            user_query = st.text_input("Ask a question about the document")
            if st.button("Send Query") and user_query:
                response = chat_with_pdf(pdf_text, user_query)
                st.session_state.conversation.append(f"User: {user_query}")
                st.session_state.conversation.append(f"AI: {response}")
                st.session_state.query_count += 1
        else:
            st.info("You have reached the maximum number of queries (10).")

        # Display conversation history
        if st.session_state.conversation:
            st.write("### Conversation History:")
            for message in st.session_state.conversation:
                st.write(message)

    except Exception as e:
        st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF file to start the chat.")
