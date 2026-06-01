import sys

if len(sys.argv) < 2:
    print("Uso: python extract_target.py <ruta_pdf>")
    sys.exit(1)

pdf_path = sys.argv[1]

# Intentar con pdfplumber primero
try:
    import pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        pages = []
        for p in pdf.pages:
            try:
                pages.append(p.extract_text() or "")
            except Exception:
                pages.append("")
    text = "\n".join(pages)
    print(text)
    sys.exit(0)
except Exception as e:
    err1 = str(e)

# Intentar con PyPDF2
try:
    from PyPDF2 import PdfReader
    reader = PdfReader(pdf_path)
    pages = []
    for p in reader.pages:
        try:
            pages.append(p.extract_text() or "")
        except Exception:
            pages.append("")
    text = "\n".join(pages)
    print(text)
    sys.exit(0)
except Exception as e:
    err2 = str(e)

print("ERROR: No fue posible extraer el PDF. Errores:\n", err1, "\n", err2)
sys.exit(2)
