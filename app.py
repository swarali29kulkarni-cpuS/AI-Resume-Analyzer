import PyPDF2
import streamlit as st

st.title("Resume Analyzer")

st.write("Upload your resume below")

uploaded_file = st.file_uploader(
    "Choose a Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    # Extract text safely
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    # SAFE LOWERCASE
    text_lower = text.lower() if text else ""

    # SKILLS
    skills = []
    if "python" in text_lower:
        skills.append("Python")
    if "aws" in text_lower:
        skills.append("AWS")
    if "sql" in text_lower:
        skills.append("SQL")
    if "machine learning" in text_lower:
        skills.append("Machine Learning")

    # EDUCATION
    if "bca" in text_lower:
        education = "BCA detected"
    else:
        education = "Not clearly found"

    # PROJECTS
    if "project" in text_lower:
        projects = "Project section found"
    else:
        projects = "No project section found"

    # OUTPUT
    st.subheader("Resume Analysis")
    st.subheader("Extracted Resume Text")
    st.write(text)

    st.markdown("### Skills")
    st.write(skills)

    st.markdown("### Education")
    st.write(education)

    st.markdown("### Projects")
    st.write(projects)