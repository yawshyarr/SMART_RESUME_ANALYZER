from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")


def compute_similarity(jd_text, resume_texts, filenames):
    documents = [jd_text] + resume_texts
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(documents)
    cosine_similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    df = pd.DataFrame({
        "Resume": filenames,
        "Match %": [round(score * 100, 2) for score in cosine_similarities]
    })
    return df.sort_values(by="Match %", ascending=False)

def extract_keywords(text):
    doc = nlp(text)
    return {token.lemma_.lower() for token in doc if token.pos_ in ['NOUN', 'PROPN', 'ADJ'] and not token.is_stop}

def missing_keywords(jd_text, resume_text):
    jd_keywords = extract_keywords(jd_text)
    resume_keywords = extract_keywords(resume_text)
    return jd_keywords - resume_keywords