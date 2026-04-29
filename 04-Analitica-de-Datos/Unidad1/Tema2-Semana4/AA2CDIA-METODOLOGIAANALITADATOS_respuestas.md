# AA2CDIA - Metodología Analítica Datlas

## 1. ¿Qué es una metodología Datlas?

La metodología Datlas es un marco de trabajo para organizar proyectos de analítica de datos de principio a fin. Su propósito es convertir un problema de negocio en una solución analítica clara, trazable y útil para la toma de decisiones. A diferencia de un análisis aislado, Datlas ordena el trabajo en fases: primero se entiende el problema, luego se obtienen y preparan los datos, después se exploran, se modelan, se evalúan los resultados, se implementa la solución y finalmente se monitorea para mejorarla.

En palabras simples, Datlas sirve para que el trabajo con datos no sea improvisado, sino un proceso con pasos, responsables, evidencia y resultados medibles.

## 2. Fases de la metodología Datlas

1. **Comprensión**: se define el problema, la pregunta analítica, el alcance, los objetivos y el KPI o meta de éxito.
2. **Adquisición**: se identifican y cargan las fuentes de datos necesarias.
3. **Preparación (Curación)**: se limpian, normalizan e integran los datos; también se crean variables derivadas.
4. **Exploración (EDA)**: se analizan patrones, tendencias, relaciones y hallazgos iniciales.
5. **Modelado**: se construye una solución analítica o predictiva.
6. **Evaluación y comunicación**: se compara el resultado con el KPI y se comunica la decisión.
7. **Implementación (Despliegue)**: se lleva la solución a un entorno operativo.
8. **Monitoreo y mejora continua**: se revisan resultados, se ajustan umbrales y se recalibra la solución.

## 3. Oportunidad de negocio en la vida diaria

Una oportunidad muy clara para aplicar Datlas es la gestión de inventario en una farmacia o tienda de barrio. Por ejemplo, si se observan faltantes frecuentes en analgésicos, antigripales o productos de alta rotación, Datlas permite identificar cuándo ocurren esos quiebres, qué factores los explican y cómo reabastecer con anticipación.

Yo la usaría porque ayuda a reducir pérdidas por ventas no atendidas, mejorar la experiencia del cliente y ordenar mejor las compras, especialmente cuando hay variaciones por clima, promociones o temporadas.

## 4. Orden cronológico de las actividades y fase Datlas correspondiente

| Orden | Actividad | Fase Datlas | Justificación |
|---|---|---|---|
| 1 | a) Definir KPI “% quiebre de stock” y la meta del bimestre. | Comprensión | Primero se debe entender el problema y fijar la meta de éxito. |
| 2 | c) Extraer datos de ventas semanales desde el ERP y del panel de promociones. | Adquisición | En esta fase se reúnen las fuentes de datos necesarias. |
| 3 | b) Integrar el CSV de ventas con el calendario de feriados y clima. | Preparación (Curación) | Aquí se integran y ordenan las fuentes para dejar el dato listo para analizar. |
| 4 | d) Explorar series y crear un pivote por producto-semana con 3 hallazgos. | Exploración (EDA) | Se buscan patrones, comportamiento y primeras conclusiones. |
| 5 | e) Entrenar un pronóstico simple por producto (media 3 semanas) y calcular MAE. | Modelado | Se construye la solución analítica o predictiva. |
| 6 | f) Presentar a gerencia un dashboard con KPIs y recomendaciones. | Evaluación y comunicación | Se interpretan los resultados y se comunica la decisión al negocio. |
| 7 | g) Desplegar reglas de reorden en la hoja “Reabasto” de la tienda online. | Implementación (Despliegue) | La solución se lleva a operación. |
| 8 | h) Revisar semanalmente los KPIs y recalibrar umbrales de cobertura/lead time. | Monitoreo y mejora continua | Se da seguimiento para ajustar la solución y sostener resultados. |

## 5. Ejercicio con el CSV de farmacia

### Problema

La red de farmacias presenta faltantes de inventario semanales en productos estacionales, especialmente analgésicos y antigripales, lo que impacta ventas y experiencia del cliente. Se requiere una solución analítica que mida, explique y reduzca estos faltantes priorizando reabastecimientos oportunos.

### Pregunta analítica

¿En qué productos y semanas es más probable un faltante y qué acciones de reorden deben ejecutarse para reducirlos al menos en 20%?

### Fase 1. Comprensión

**Salida esperada:** una ficha con el problema, KPI y meta.

**Interpretación:**
- Problema: evitar quiebres de stock en productos críticos.
- KPI: porcentaje de semanas con faltante (`stockout_sem`).
- Meta: reducir los faltantes al menos en 20% en un periodo de seguimiento.

### Fase 2. Adquisición

**Salida esperada:** un inventario de datos con campo, tipo, fuente, calidad y responsable.

**Interpretación:**
- El archivo CSV aporta las variables base del análisis: semana, fecha, producto, precio, promoción, stock inicial, unidades vendidas, stock final, faltante, lluvia, feriado, competencia, lead time y riesgo futuro.
- Esta fase deja claro qué dato proviene del inventario, cuáles del área comercial y cuáles del contexto externo.

### Fase 3. Preparación (Curación)

**Salida esperada:** bitácora de cambios y diccionario actualizado.

**Interpretación:**
- Se convierte `fecha_semana` a formato fecha.
- Se asegura que `semana` sea numérica.
- Se crea `tasa_venta` como razón entre `unidades_vendidas` y `stock_inicio_sem`.
- El diccionario actualizado deja documentada la nueva variable y su significado.

### Fase 4. Exploración (EDA)

**Salida esperada:** ranking de productos con mayor porcentaje de faltante y serie total de unidades vendidas por semana.

**Hallazgos principales del CSV:**
- El faltante total es bajo: **0.6%** de las observaciones.
- Solo dos productos presentan quiebres de stock: **Paracetamol_500mg** e **Ibuprofeno_400mg**, ambos con **3.8%** de semanas con faltante.
- Los faltantes ocurrieron en las semanas **14 y 15**.
- Los productos con mayor demanda promedio son **Paracetamol_500mg** y **Ibuprofeno_400mg**, por lo que son los más sensibles a una mala planificación.

### Fase 5. Modelado

**Salida esperada:** pronóstico del total de unidades para la siguiente semana.

**Resultado calculado:**
- Pronóstico para la semana 27: **191.4 unidades** aproximadamente.
- La tendencia lineal global es levemente descendente, por lo que no se observa crecimiento fuerte del total semanal.

**Interpretación:**
- El volumen total de venta se mantiene relativamente estable alrededor de 190 a 205 unidades por semana.
- Esto sugiere que el problema no es una caída general de demanda, sino una mala sincronización del reabastecimiento en productos específicos.

### Fase 6. Evaluación y comunicación

**Salida esperada:** resumen ejecutivo con KPI antes y decisión propuesta.

**Resultado calculado:**
- KPI base de faltantes: **0.64%**.
- Productos críticos: Paracetamol_500mg e Ibuprofeno_400mg.
- Se recomienda aplicar reglas de reorden preventivo para reducir al menos un 20% los faltantes.

**Interpretación:**
- La solución no debe enfocarse solo en vender más, sino en evitar quiebres puntuales que afectan la disponibilidad.
- Con una política de reabastecimiento anticipado, el negocio puede reducir pérdidas de venta y mejorar la atención al cliente.

### Fase 7. Implementación (Despliegue)

**Propuesta de regla operativa en la hoja “Reabasto”:**
- **Paracetamol_500mg:** reordenar si el stock inicial cae a **35 unidades o menos**.
- **Ibuprofeno_400mg:** reordenar si el stock inicial cae a **30 unidades o menos**.
- **Antigripal:** reordenar si el stock inicial cae a **25 unidades o menos**.
- Activar la compra con al menos una semana de anticipación cuando el `lead_time_dias` esté entre 5 y 7 días.

**Interpretación:**
- Estas reglas cubren los productos de mayor rotación y reducen la probabilidad de quedarse sin inventario justo cuando la demanda alcanza su punto más alto.

### Fase 8. Monitoreo y mejora continua

**Acción recomendada:**
- Revisar semanalmente el KPI de faltantes.
- Comparar stock proyectado contra stock real.
- Ajustar umbrales cuando cambie el clima, haya feriados o aumente el lead time.

**Interpretación:**
- El modelo no debe quedarse fijo; debe recalibrarse conforme cambie el comportamiento de compra y suministro.

## Conclusión

Datlas permite resolver el problema de farmacia de manera ordenada: primero se entiende la necesidad, después se preparan y exploran los datos, luego se modela una solución simple y finalmente se implementan reglas de reorden y seguimiento. En este CSV, el foco debe ponerse en Paracetamol_500mg e Ibuprofeno_400mg, que son los productos que realmente presentan quiebres y por tanto los mejores candidatos para una intervención de inventario.

## Referencias

- Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O'Reilly Media.
- Witten, I. H., Frank, E., Hall, M. A., & Pal, C. J. (2016). *Data Mining: Practical Machine Learning Tools and Techniques* (4th ed.). Morgan Kaufmann.
- Han, J., Kamber, M., & Pei, J. (2011). *Data Mining: Concepts and Techniques* (3rd ed.). Morgan Kaufmann.
- Shmueli, G., Bruce, P. C., Gedeck, P., & Patel, N. R. (2020). *Data Mining for Business Analytics*. Wiley.
- Zipkin, P. H. (2000). *Foundations of Inventory Management*. McGraw-Hill.
