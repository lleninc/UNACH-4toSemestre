# Flask app para Autonomo 3

Esta aplicacion convierte el notebook `Autonomo3_Analitica.ipynb` en una pagina web con resultados visibles.

## Que muestra

- Limpieza y deteccion automatica del encabezado del CSV.
- Resumen de provincias y categorias.
- Graficos de emisiones por provincia y heatmaps.
- Modelo de priorizacion Top vs no Top con metrica visible.
- Tabla de focalizacion operativa.

## Como ejecutar

Desde `04-Analitica-de-Datos/Unidad2/Tema1-Semana2/Autonomo/flask_app`:

```powershell
python app.py
```

Luego abre `http://127.0.0.1:5000/`.

## Datos

El CSV se resuelve automaticamente desde la carpeta padre `Autonomo`.
