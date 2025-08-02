import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="📚 StudyMate AI", layout="centered")

# Show Logo
logo_path = "assets/logo.png"
if os.path.exists(logo_path):
    st.image(Image.open(logo_path), width=100)

# Title and Instructions
st.markdown("## 📚 StudyMate AI")
st.markdown("Upload a PDF and ask questions to get AI-generated answers.")

# PDF Upload
pdf_file = st.file_uploader("📄 Upload your PDF", type=["pdf"])

# Question Box
question = st.text_input("🧠 Ask a question about your PDF:", placeholder="What is the conclusion?")

# Show warning if fields are empty
if not pdf_file:
    st.warning("Please upload a PDF file to continue.")
elif not question:
    st.info("Enter a question about the uploaded document.")
else:
    st.success("Ready to process!")
    # (Call your RAG + summary logic here)
