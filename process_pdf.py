from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split_pdf(file_path):
    # Step 1: Load the PDF using PyPDF2
    reader = PdfReader(file_path)
    raw_text = ""
    for page in reader.pages:
        raw_text += page.extract_text()

    # Step 2: Split the raw text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.create_documents([raw_text])
    return chunks
