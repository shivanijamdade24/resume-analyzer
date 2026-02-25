import streamlit as st
import PyPDF2

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

required_skills = ["python", "java", "machine learning", "cloud", "sql", "data analysis"]

if uploaded_file is not None:
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text().lower()

    matched_skills = []
    missing_skills = []

    for skill in required_skills:
        if skill in text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    score = int((len(matched_skills) / len(required_skills)) * 100)

    st.subheader("Resume Score")
    st.write(score, "%")

    st.subheader("Matched Skills")
    st.write(matched_skills)

    st.subheader("Missing Skills")
    st.write(missing_skills)