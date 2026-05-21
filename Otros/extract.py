import pdfplumber
import io

pdf_path = '05-Administracion-BD/Unidad1/Tema2-Semana3/CA_ U1T2_ADMI_BASEDATOS.pdf'
try:
    with pdfplumber.open(pdf_path) as pdf:
        text = '\n'.join([p.extract_text() or "" for p in pdf.pages])
    with io.open('extracted_utf8.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extraction successful")
except Exception as e:
    print(f"Error: {e}")
