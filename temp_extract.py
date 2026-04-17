import pdfplumber
import sys

pdf_path = "05-Administracion-BD/Unidad1/Tema2-Semana3/CA_ U1T2_ADMI_BASEDATOS.pdf"
try:
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    print(full_text)
except Exception as e:
    print(f"Error: {e}")
