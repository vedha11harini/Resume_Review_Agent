from pypdf import PdfReader


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from an uploaded PDF file.

    Args:
        pdf_file: Uploaded PDF file from Streamlit

    Returns:
        str: Extracted text
    """

    reader = PdfReader(pdf_file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text.strip()