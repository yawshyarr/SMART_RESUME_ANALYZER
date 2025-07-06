# Title - Smart Resume Analyzer

Smart Resume Analyzer is a Streamlit-based web app that helps HR professionals or recruiters evaluate multiple resumes by comparing them to a given job description. It ranks candidates based on skill match and highlights missing keywords.

# Features

-  Upload multiple resumes (PDF/DOCX)
-  Paste a job description
-  Analyze resumes and compute match scores
-  Display resume ranking in a table
-  Show missing keywords for each resume


# Tech Stack

- Python 
- Streamlit
- spaCy
- scikit-learn
- PyMuPDF
- python-docx
- Pandas


# Project Structure

smart_resume_analyzer/
│
├── app.py                  # Main Streamlit app
├── analyzer.py             # Similarity and keyword analyzer
├── resume_py.py            # Resume text extractor
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── screenshots/            # Folder for app screenshots

# How to run 

Smart Resume Analyzer - Step-by-Step Setup Guide

1. Install Python:

 - Ensure Python 3.8+ is installed.
 - Check with: python --version
 - If not, download from https://www.python.org/downloads

2. Download or Clone the Project:
 - Clone: git clone https://github.com/YOUR-USERNAME/smart-resume-analyzer.git
 - Or download and extract the ZIP file.

3. Navigate into the Project Directory:
 cd smart-resume-analyzer

4. (Optional) Create a Virtual Environment:
 - python -m venv venv
 - venv\Scripts\activate (Windows)
 - source venv/bin/activate (Mac/Linux)

5. Install Required Libraries:
 - pip install -r requirements.txt

6. Download SpaCy Language Model:
 - python -m spacy download en_core_web_sm

7. Run the Streamlit App:
 - streamlit run app.py

8. Open the App in Browser:
 - Visit the local URL shown in terminal (usually http://localhost:8501)

9. Use the Application:
 - Paste Job Description
 - Upload Resume(s) in PDF/DOCX format
 - Click 'Analyze'
 - View rankings and missing keywords.





