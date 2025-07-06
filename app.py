import streamlit as st
from resume_py import extract_resume_text
from analyzer import compute_similarity, missing_keywords

#THEME (DARK MODE)
st.markdown("""
    <style>
    .main {
        background-color: black;
        color: white;
    }
    .css-1d391kg {  /* sidebar */
        background-color: #111;
        color: white;
    }
    div, p, span, label, h1, h2, h3 {
        color: white !important;
    }
    </style>
""", unsafe_allow_html=True)

#TITLE CODE
st.title("SMART RESUME ANALYZER")

#FOR SIDEBAR
st.sidebar.header("UPLOAD SECTION")
jd_text = st.text_area("PASTE JOB DESCRIPTION:")

resume_files = st.sidebar.file_uploader("UPLOAD RESUMES", type=['pdf', 'docx'], accept_multiple_files=True)

#BUTTON
if st.button("ANALYZE RESUMES"):
    if jd_text and resume_files:
        st.success(" Processing resumes...")

        resume_texts = []
        filenames = []

        for file in resume_files:
            text = extract_resume_text(file)
            if text:
                resume_texts.append(text)
                filenames.append(file.name)

        #RANK
        result_df = compute_similarity(jd_text, resume_texts, filenames)
        st.subheader(" Resume Ranking")
        st.dataframe(result_df)

        #MISSING KEYWORD
        st.subheader("Missing Keywords")
        for i, name in enumerate(filenames):
            missing = missing_keywords(jd_text, resume_texts[i])
            st.markdown(f"**{name}**: {', '.join(missing) if missing else 'All keywords matched'}")
    else:
        st.warning(" Please upload resumes and paste a job description.")
