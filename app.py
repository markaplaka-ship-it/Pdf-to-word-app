import streamlit as st
from pdf2docx import Converter

st.set_page_config(page_title="PDF a Word", layout="centered")

st.title("📄 Convertidor de PDF a Word")
st.write("Sube tu archivo PDF y descarga el documento Word.")

uploaded_file = st.file_uploader("Seleccionar un PDF", type=["pdf"])

if uploaded_file is not None:
    with open("input.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.info("⏳ Conversión en curso...")

    try:
        cv = Converter("input.pdf")
        cv.convert("output.docx")
        cv.close()

        st.success("✅ Conversión terminada")

        with open("output.docx", "rb") as f:
            st.download_button(
                label="📥 Descargar archivo Word",
                data=f,
                file_name="convertido.docx"
            )

    except Exception as e:
        st.error(f"❌ Error: {e}")
