import streamlit as st
from pdf2docx import Converter

st.set_page_config(page_title="PDF → Word", layout="centered")

st.title("📄 Convertisseur PDF → Word")
st.write("Upload ton fichier PDF et télécharge le Word.")

uploaded_file = st.file_uploader("Choisir un PDF", type=["pdf"])

if uploaded_file is not None:
    with open("input.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("⏳ Conversion en cours...")

    try:
        cv = Converter("input.pdf")
        cv.convert("output.docx")
        cv.close()

        st.success("✅ Conversion terminée !")

        with open("output.docx", "rb") as f:
            st.download_button(
                label="📥 Télécharger le fichier Word",
                data=f,
                file_name="converted.docx"
            )

    except Exception as e:
        st.error(f"❌ Erreur : {e}")
