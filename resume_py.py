import pdfplumber
import docx

def extract_text_from_pdf(pdf_file):
    text = ' '
    with pdfplumber.open(pdf_file) as pdf:
        for i in pdf.pages:
            text += i.extract_text() + "\n"
    return text

def extract_text_from_docx(docx_file):
    doc = docx.document(docx_file)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_resume_text(file):
    if file.name.endswith('.pdf'):
        return extract_text_from_pdf(file)
    elif file.name.endwith('.docx'):
        return extract_text_from_docx(file)
    return ""