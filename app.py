import streamlit as st
from PIL import Image
import os
from process_pdf import load_and_split_pdf
from rag_pipeline import build_qa_chain

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

# Handle logic
if not pdf_file:
    st.warning("Please upload a PDF file to continue.")
elif not question:
    st.info("Enter a question about the uploaded document.")
else:
    with st.spinner("🔄 Processing your document and question..."):
        try:
            # Save PDF locally
            file_path = os.path.join("data", pdf_file.name)
            os.makedirs("data", exist_ok=True)
            with open(file_path, "wb") as f:
                f.write(pdf_file.getbuffer())

            # Load + chunk
            chunks = load_and_split_pdf(file_path)

            # Build chain
            qa_chain = build_qa_chain(chunks)

            # Generate answer
            answer = qa_chain.run(question)

            st.success("✅ Answer generated!")
            st.markdown("### 🧠 Answer:")
            st.write(answer)
        except Exception as e:
            st.error(f"❌ Something went wrong:\n\n{e}")
