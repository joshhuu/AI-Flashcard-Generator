import streamlit as st
import tempfile
import os

from flashcard_generator import generate_question
from utils.pdf_reader import extract_text_from_pdf

st.set_page_config(page_title="AI Flashcard Generator", layout="wide")
st.title("📚 AI Flashcard Generator (PDF & Text)")

# Preserve text in session state
if "content" not in st.session_state:
    st.session_state.content = ""

mode = st.radio("Input type:", ["Paste Text", "Upload PDF"], index=0)

if mode == "Paste Text":
    st.session_state.content = st.text_area(
        "Paste your content here:", value=st.session_state.content, height=300
    )
else:
    uploaded = st.file_uploader("Upload a PDF file", type="pdf")
    if uploaded is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded.read())
            tmp_path = tmp.name
        with st.spinner("Extracting text from PDF…"):
            st.session_state.content = extract_text_from_pdf(tmp_path)
        os.remove(tmp_path)
        st.success("PDF text extracted!")

keywords = st.text_input(
    "Enter comma-separated keywords (e.g., sun, solar system):"
).strip()
kw_list = [k.strip() for k in keywords.split(",") if k.strip()]

if st.button("Generate Flashcards"):
    if not st.session_state.content:
        st.warning("⚠️ Please provide some content (text or PDF).")
    elif not kw_list:
        st.warning("⚠️ Please enter at least one keyword.")
    else:
        with st.spinner("Generating flashcards…"):
            for kw in kw_list:
                try:
                    card = generate_question(kw, st.session_state.content)
                    st.markdown(f"**Q:** {card['question']}")
                    st.markdown(f"**A:** {card['answer']}")
                    st.markdown("---")
                except ValueError as e:
                    st.error(str(e))
    