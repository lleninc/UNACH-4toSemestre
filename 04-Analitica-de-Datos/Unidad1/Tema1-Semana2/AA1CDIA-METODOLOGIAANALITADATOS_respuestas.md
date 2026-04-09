# AA1CDIA - Metodologias de Analitica de Datos (Unidad 1, Tema 1, Semana 2)

## 1) Que es una metodologia de analisis de datos y por que es necesaria

Una metodologia de analisis de datos es un marco de trabajo estructurado que organiza, en etapas, como se formula un problema, como se recolectan y preparan datos, como se modela, como se interpreta y como se implementan decisiones basadas en evidencia. Su objetivo es pasar de datos crudos a valor de negocio de forma sistematica y repetible.

Es necesaria porque:
- Reduce la improvisacion y alinea el trabajo tecnico con objetivos del negocio.
- Mejora la calidad y trazabilidad de los resultados (supuestos, datos, metricas y decisiones quedan documentados).
- Disminuye riesgos de sesgos, errores de interpretacion y soluciones no implementables.
- Facilita la colaboracion entre perfiles de negocio, analistas, ingenieria y direccion.
- Permite medir impacto con KPIs y sostener mejora continua.

## 2) Clasificacion de casos (descriptiva, predictiva o prescriptiva)

a) Dashboard mensual con ventas por region, top 10 productos y variacion vs. ano anterior.
- Tipo: Analitica descriptiva.
- Justificacion: Resume y visualiza lo que ya ocurrio en el periodo, comparando desempeno historico por region y producto para entender comportamiento pasado.

b) Modelo que estima la demanda de paraguas por ciudad para el proximo mes.
- Tipo: Analitica predictiva.
- Justificacion: Usa variables explicativas (clima, estacionalidad) para proyectar un valor futuro (demanda), es decir, anticipa que podria pasar.

c) Sistema que propone mejor precio y cantidad a reponer maximizando margen y minimizando quiebres con restricciones.
- Tipo: Analitica prescriptiva.
- Justificacion: No solo predice, sino que recomienda acciones optimas (precio y reposicion) bajo objetivos y restricciones operativas.

d) Informe que segmenta clientes por RFM para entender valor actual de la cartera.
- Tipo: Analitica descriptiva.
- Justificacion: Organiza clientes segun comportamiento observado (recencia, frecuencia, monto) para explicar estado actual de la cartera.

e) Algoritmo que asigna probabilidad de churn en los proximos 60 dias.
- Tipo: Analitica predictiva.
- Justificacion: Estima la probabilidad de un evento futuro (abandono), permitiendo anticipar riesgo por cliente.

f) Optimizador de rutas que recomienda orden y horarios para reducir 20% el tiempo de reparto.
- Tipo: Analitica prescriptiva.
- Justificacion: Entrega una recomendacion de decision operativa (rutas y secuencia) optimizada para cumplir un objetivo de eficiencia.

## 3) Seis (o mas) etapas del ciclo de vida de un proyecto de analitica

1. Definicion del problema
- Objetivo: Traducir una necesidad del negocio en preguntas analiticas y criterios de exito.
- Entregable tipico: Documento de alcance con objetivo, supuestos, KPIs y restricciones.

2. Recoleccion de datos
- Objetivo: Identificar, acceder e integrar fuentes internas y externas relevantes.
- Entregable tipico: Inventario de fuentes y dataset bruto consolidado.

3. Preparacion de datos
- Objetivo: Limpiar, transformar y estructurar datos para analisis/modelado.
- Entregable tipico: Dataset analitico limpio, diccionario de datos y reglas de calidad.

4. Analisis y modelado
- Objetivo: Aplicar tecnicas estadisticas o de machine learning para explicar o predecir fenomenos.
- Entregable tipico: Modelos candidatos, metricas de desempeno y seleccion del modelo final.

5. Interpretacion y comunicacion
- Objetivo: Convertir resultados tecnicos en hallazgos accionables para tomadores de decision.
- Entregable tipico: Dashboard/reporte ejecutivo con insights y recomendaciones.

6. Implementacion de decisiones
- Objetivo: Operacionalizar hallazgos en procesos, sistemas o reglas de negocio.
- Entregable tipico: Plan de despliegue, reglas implementadas y manual operativo.

7. Medicion de impacto (KPIs)
- Objetivo: Verificar si la solucion genera valor respecto a la linea base.
- Entregable tipico: Informe de impacto con seguimiento de KPIs y ROI.

8. Monitoreo y mejora continua
- Objetivo: Detectar degradacion, cambios de contexto y oportunidades de ajuste.
- Entregable tipico: Tablero de monitoreo, alertas y backlog de mejoras.

## 4) Orden cronologico y etapa correspondiente

1. b) Definir KPI "tasa de conversion online" y la meta del trimestre.
- Etapa: Definicion del problema.
- Justificacion: Se fijan objetivo y criterio de exito antes de manipular datos o entrenar modelos.

2. c) Extraer datos de ventas de la base interna y del panel de redes sociales.
- Etapa: Recoleccion de datos.
- Justificacion: Se obtienen e integran fuentes necesarias para el analisis.

3. a) Eliminar duplicados y crear variables derivadas.
- Etapa: Preparacion de datos.
- Justificacion: Se asegura calidad y se construyen variables utiles para modelar.

4. d) Entrenar un modelo de pronostico de demanda para el proximo mes.
- Etapa: Analisis/Modelado.
- Justificacion: Se aplican tecnicas analiticas para aprender patrones y generar predicciones.

5. e) Presentar hallazgos a gerencia con un dashboard y conclusiones clave.
- Etapa: Interpretacion/Comunicacion.
- Justificacion: Los resultados se traducen a lenguaje de negocio para apoyar decisiones.

6. f) Desplegar reglas de reposicion y precios en la tienda online.
- Etapa: Implementacion.
- Justificacion: Se lleva la recomendacion analitica al entorno operativo real.

7. g) Revisar semanalmente los KPIs y ajustar parametros del modelo.
- Etapa: Monitoreo y mejora.
- Justificacion: Se controla desempeno post-despliegue y se corrigen desviaciones para sostener valor.

## Bibliografia (APA 7)

- Davenport, T. H., & Harris, J. G. (2007). Competing on analytics: The new science of winning. Harvard Business School Press.
- Han, J., Kamber, M., & Pei, J. (2012). Data mining: Concepts and techniques (3rd ed.). Morgan Kaufmann.
- Kelleher, J. D., & Tierney, B. (2018). Data science. MIT Press.
- Provost, F., & Fawcett, T. (2013). Data science for business: What you need to know about data mining and data-analytic thinking. O'Reilly Media.
- Shmueli, G., Bruce, P. C., Gedeck, P., & Patel, N. R. (2020). Data mining for business analytics: Concepts, techniques, and applications in Python (1st ed.). Wiley.
- Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. In Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining (pp. 29-39).
