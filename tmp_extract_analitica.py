from pathlib import Path

pdf_path = Path(r"e:\Unach\Semestre4\EstudioGITClaude\UNACH-4toSemestre\04-Analitica-de-Datos\Unidad1\Tema1-Semana2\AA1CDIA-METODOLOGIAANALITADATOS.pdf")
out_path = pdf_path.with_name("AA1CDIA-METODOLOGIAANALITADATOS_extraido.txt")

text = ""
try:
    from pypdf import PdfReader
    reader = PdfReader(str(pdf_path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        t = page.extract_text() or ""
        pages.append(f"\n\n===== PAGINA {i} =====\n\n" + t)
    text = "".join(pages)
except Exception as e:
    text = f"ERROR: {e}"

out_path.write_text(text, encoding="utf-8")
print(out_path)
print("chars:", len(text))
