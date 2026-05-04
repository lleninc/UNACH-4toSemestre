import pdfplumber
import os
import sys

# Cambiar la codificación de salida
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

pdf_principal = "02-Machine-Learning/Unidad2/Tema1-Semana1/CA U2T1 CDIA-ML1.pdf"
pdf_quiz1 = "02-Machine-Learning/Unidad2/Tema1-Semana1/QUIZ U2-T1-S1 (APE5)_Machine Learning.pdf"
pdf_quiz2 = "02-Machine-Learning/Unidad2/Tema1-Semana1/QUIZ U2-T1-S1 (APE5)_MachineLearning_LL.pdf"
pdf_quiz3 = "02-Machine-Learning/Unidad2/Tema1-Semana1/QUIZ U2-T1-S1 (APE5)_MachineLearning_LL1.pdf"

print("="*80)
print("EXTRAYENDO CONTENIDO DEL PDF PRINCIPAL - TEORÍA")
print("="*80)
print()

try:
    with pdfplumber.open(pdf_principal) as pdf:
        print(f"Total de páginas: {len(pdf.pages)}\n")
        for i, page in enumerate(pdf.pages):
            try:
                text = page.extract_text()
                if text:
                    print(f"\n{'='*80}")
                    print(f"PÁGINA {i+1}")
                    print(f"{'='*80}\n")
                    # Reemplazar caracteres especiales
                    clean_text = text.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
                    print(clean_text)
            except Exception as e:
                print(f"Error en página {i+1}: {e}")
except Exception as e:
    print(f"Error en PDF principal: {e}")

# Extraer quizzes
for idx, pdf_path in enumerate([pdf_quiz1, pdf_quiz2, pdf_quiz3], 1):
    print(f"\n\n{'#'*80}")
    print(f"QUIZ {idx}: {os.path.basename(pdf_path)}")
    print(f"{'#'*80}\n")
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                try:
                    text = page.extract_text()
                    if text:
                        clean_text = text.encode('utf-8', errors='replace').decode('utf-8', errors='replace')
                        print(clean_text)
                except Exception as e:
                    print(f"Error en página: {e}")
    except Exception as e:
        print(f"Error: {e}")
