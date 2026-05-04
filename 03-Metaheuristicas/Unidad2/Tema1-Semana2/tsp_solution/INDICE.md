# 📑 ÍNDICE GENERAL - Proyecto TSP Metaheurísticas

## 🎯 Inicio Rápido

**Quiero ver los resultados AHORA:**
1. Abre `RESULTADOS.html` en tu navegador (visualización interactiva)
2. O lee `RESULTADOS.md` (resumen en texto)
3. O ejecuta `python main.py` (regenerar resultados)

---

## 📚 Documentación

### Para Empezar Rápido
📄 **[QUICKSTART.md](QUICKSTART.md)** - Inicio en 5 minutos
- Instrucciones de ejecución
- Ejemplos de código
- FAQ común
- Solución de problemas

### Para Entender el Proyecto
📄 **[README.md](README.md)** - Documentación Completa
- Estructura del proyecto
- Descripción de cada módulo
- Cómo usar cada algoritmo
- Parámetros configurables
- Ejemplos avanzados
- Referencias académicas

### Para Ver los Resultados
📄 **[RESULTADOS.md](RESULTADOS.md)** - Análisis Detallado
- Tabla comparativa
- Análisis de convergencia
- Ventajas y desventajas
- Recomendaciones

📄 **[RESULTADOS.html](RESULTADOS.html)** - Visualización Interactiva
- Tablas comparativas
- Diseño profesional
- Gráficos visuales
- Fácil de navegar

### Para Entender Todo
📄 **[RESUMEN_EJECUTIVO.md](RESUMEN_EJECUTIVO.md)** - Resumen Completo
- Tareas completadas
- Resultados obtenidos
- Características técnicas
- Estadísticas del proyecto
- Checklist final

---

## 🐍 Código Python

### Módulos Principales

**Problema TSP**
🔧 [tsp_problem.py](tsp_problem.py)
- Define el problema
- 5 ciudades
- Matriz de distancias
- Cálculo de rutas

**Algoritmo PSO**
🔧 [pso_tsp.py](pso_tsp.py)
- Particle Swarm Optimization
- Implementación completa
- Parámetros: w, c1, c2
- Rápido y eficiente

**Algoritmo GA**
🔧 [ga_tsp.py](ga_tsp.py)
- Genetic Algorithm
- OX Crossover
- Mutación swap
- Preservación de élite

**Algoritmo ACO**
🔧 [aco_tsp.py](aco_tsp.py)
- Ant Colony Optimization
- Sistema de feromonas
- Construcción probabilística
- Excelente calidad

### Módulos de Comparación

🔧 [comparison.py](comparison.py)
- Ejecuta los 3 algoritmos
- Genera tabla comparativa
- Análisis de convergencia
- Calcula estadísticas

### Script Principal

🚀 [main.py](main.py)
- Ejecuta todo el proyecto
- Genera reportes
- Crea ensayo
- Exporta resultados

### Paquete

📦 [__init__.py](__init__.py)
- Importar como paquete
- Interfaces limpias
- Fácil de reutilizar

---

## 📊 Resultados Generados

### JSON
📊 [tsp_results.json](tsp_results.json)
```json
{
  "PSO": {"best_distance": 61.2276, ...},
  "GA": {"best_distance": 61.2276, ...},
  "ACO": {"best_distance": 61.2276, ...}
}
```

### Ensayo Académico
📝 [ensayo_metaheuristicas_tsp.markdown](ensayo_metaheuristicas_tsp.markdown)
- 850+ palabras
- Análisis completo
- Recomendaciones
- Referencias

---

## 🎯 Tabla de Contenidos por Tópico

### Quiero Aprender Sobre...

**PSO**
- Qué es: `README.md` → Sección "PSO"
- Cómo usarlo: `QUICKSTART.md` → PSO
- Código fuente: `pso_tsp.py`
- Resultados: `RESULTADOS.md` → Tabla Comparativa

**GA**
- Qué es: `README.md` → Sección "GA"
- Cómo usarlo: `QUICKSTART.md` → GA
- Código fuente: `ga_tsp.py`
- Resultados: `RESULTADOS.md` → Tabla Comparativa

**ACO**
- Qué es: `README.md` → Sección "ACO"
- Cómo usarlo: `QUICKSTART.md` → ACO
- Código fuente: `aco_tsp.py`
- Resultados: `RESULTADOS.md` → Tabla Comparativa

**TSP**
- Definición: `README.md` → Contexto
- Implementación: `tsp_problem.py`
- Ejemplos: `QUICKSTART.md` → Ejemplo Completo

**Comparación**
- Resultados: `RESULTADOS.md`
- Visualización: `RESULTADOS.html`
- Análisis: `ensayo_metaheuristicas_tsp.markdown`
- Estadísticas: `RESUMEN_EJECUTIVO.md`

---

## 📈 Flujo de Uso Recomendado

### Opción 1: Solo Ver Resultados (2 min)
1. Abre `RESULTADOS.html` en navegador
2. Lee `RESUMEN_EJECUTIVO.md`
3. ¡Listo!

### Opción 2: Entender el Proyecto (20 min)
1. Lee `QUICKSTART.md`
2. Lee `README.md`
3. Revisa `RESULTADOS.md`
4. Abre `RESULTADOS.html`
5. ¡Listo!

### Opción 3: Aprender en Profundidad (1 hora)
1. Lee `QUICKSTART.md`
2. Lee `README.md` (completo)
3. Revisa código Python (tsp_problem.py, pso_tsp.py, etc.)
4. Lee `RESULTADOS.md`
5. Lee `ensayo_metaheuristicas_tsp.markdown`
6. ¡Listo!

### Opción 4: Usar en Tu Proyecto (30 min)
1. Lee `QUICKSTART.md` → "Usar en Tu Código"
2. Copia ejemplos de `QUICKSTART.md`
3. Adapta parámetros
4. ¡Listo!

---

## 🔗 Referencias Cruzadas Rápidas

### Si Quieres Ejecutar el Proyecto
- `QUICKSTART.md` → "Inicio Rápido"
- `README.md` → "Instalación y Uso"
- Terminal: `python main.py`

### Si Quieres Personalizar Parámetros
- `QUICKSTART.md` → "Personalizar Parámetros"
- `README.md` → "Parámetros Configurables"
- Archivos: `pso_tsp.py`, `ga_tsp.py`, `aco_tsp.py`

### Si Quieres Entender Los Resultados
- `RESULTADOS.md` → "Tabla Comparativa"
- `RESUMEN_EJECUTIVO.md` → "Resultados Obtenidos"
- `RESULTADOS.html` → Visualización interactiva
- `tsp_results.json` → Datos crudos

### Si Quieres Aprender Algoritmos
- `README.md` → "Descripción de Algoritmos"
- `ensayo_metaheuristicas_tsp.markdown` → Análisis completo
- Código: `pso_tsp.py`, `ga_tsp.py`, `aco_tsp.py`

### Si Quieres Más Información
- `README.md` → "Referencias"
- `ensayo_metaheuristicas_tsp.txt` → Referencias académicas

---

## 📊 Estadísticas del Proyecto

| Elemento | Cantidad |
|----------|----------|
| Archivos Python | 7 |
| Líneas de código | 1,300+ |
| Documentos | 7 |
| Palabras de documentación | 5,000+ |
| Ensayo académico | 850+ palabras |
| Archivos de resultado | 4 |
| Tablas comparativas | 5+ |

---

## ✅ Checklist de Lectura

Marca lo que has leído:

**Documentación Principal**
- [ ] QUICKSTART.md
- [ ] README.md
- [ ] RESULTADOS.md
- [ ] RESUMEN_EJECUTIVO.md

**Visualización**
- [ ] RESULTADOS.html

**Ensayo Académico**
- [ ] ensayo_metaheuristicas_tsp.txt

**Código**
- [ ] tsp_problem.py
- [ ] pso_tsp.py
- [ ] ga_tsp.py
- [ ] aco_tsp.py
- [ ] comparison.py
- [ ] main.py

**Resultados**
- [ ] tsp_results.json

---

## 🆘 Si Tienes Dudas

**Sobre cómo ejecutar:**
→ Lee `QUICKSTART.md` → "Inicio Rápido"

**Sobre parámetros:**
→ Lee `QUICKSTART.md` → "Personalizar Parámetros"
→ O `README.md` → "Parámetros Configurables"

**Sobre algoritmos:**
→ Lee `README.md` → "Descripción de Algoritmos"
→ O `ensayo_metaheuristicas_tsp.txt`

**Sobre resultados:**
→ Lee `RESULTADOS.md`
→ O abre `RESULTADOS.html`

**Sobre código:**
→ Revisa `QUICKSTART.md` → "Código de Ejemplo"
→ O `README.md` → "Ejemplos de Código"

---

## 🚀 Próximos Pasos

Después de familiarizarte con el proyecto:

1. **Ejecuta main.py** para ver los algoritmos en acción
2. **Personaliza parámetros** para experimentar
3. **Añade más ciudades** al problema
4. **Implementa nuevos algoritmos** (Simulated Annealing, etc.)
5. **Visualiza convergencia** con gráficos
6. **Prueba con problemas más grandes**

---

## 📞 Información de Contacto

**Proyecto:** Comparación de Metaheurísticas para TSP
**Semestre:** 4to
**Asignatura:** Metaheurísticas
**Universidad:** UNACH
**Año:** 2024-2025

---

## 🎓 Referencias Rápidas

Conceptos clave explicados en:
- **TSP:** README.md → "Conceptos Clave"
- **Metaheurística:** ensayo_metaheuristicas_tsp.txt → Introducción
- **PSO:** README.md → "Particle Swarm Optimization"
- **GA:** README.md → "Genetic Algorithm"
- **ACO:** README.md → "Ant Colony Optimization"

---

**¡Bienvenido al Proyecto TSP Metaheurísticas!** 🎉

Elige un documento arriba y comienza tu exploración.

