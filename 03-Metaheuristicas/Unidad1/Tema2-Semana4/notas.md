# 03-Metaheuristicas - U1 T2 S4

## Objetivo de la semana
Analizar aplicaciones de Datlas en proyectos de negocio e identificar sus ventajas y limitaciones frente a CRISP-DM, SEMMA y KDD.


## 2.3 Aplicaciones de Datlas en proyectos de negocio

Datlas se aplica en organizaciones que buscan convertir datos dispersos en decisiones operativas. Su enfoque resulta útil cuando existen objetivos claros, integración de múltiples fuentes y comunicación constante con usuarios finales.

**Aplicaciones frecuentes:**
- Inteligencia comercial y análisis de mercado.
- Monitoreo ambiental y evaluación de impacto.
- Predicción de demanda y planificación operativa.
- Segmentación y analítica de comportamiento de clientes.
- Dashboards ejecutivos para decisión rápida.

**Casos de negocio destacados en el material:**
- Caso Sigma Alimentos (retail/consumo): integración de múltiples fuentes y migración de reportes manuales a dashboards interactivos.
- Caso ProNatura (ambiental): consolidación de datos de campo y contexto para monitorear reforestación con indicadores trazables.
- Caso Cinépolis (entretenimiento): uso de analítica predictiva para anticipar demanda y apoyar decisiones comerciales.

**Valor en negocio:**
- Reduce tiempos de respuesta para áreas usuarias.
- Mejora trazabilidad de indicadores y resultados.
- Facilita escalamiento de soluciones analíticas.
- Incrementa el uso de evidencia en decisiones tácticas.


## Tabla 1

**Caracteristicas comparativas de PSO, GA y ACO en distintos aspectos de desempeno resumido**

| Aspecto | PSO (Particle Swarm Optimization) | GA (Genetic Algorithm) | ACO (Ant Colony Optimization) |
|---|---|---|---|
| Velocidad de convergencia inicial | Alta en espacios continuos y problemas bien calibrados | Media; depende de seleccion, cruce y mutacion | Media-baja al inicio por fase de exploracion de feromonas |
| Equilibrio exploracion/explotacion | Bueno con ajuste de inercia y coeficientes cognitivo/social | Flexible; controlado por operadores geneticos y elitismo | Fuerte exploracion inicial y explotacion progresiva por refuerzo de caminos |
| Riesgo de optimo local | Medio; puede estancarse sin diversidad | Medio-alto si la poblacion pierde diversidad | Medio; mejora con evaporacion y ruido estocastico |
| Sensibilidad a parametros | Media (inercia, c1, c2, topologia) | Alta (tamano poblacion, tasa de cruce, mutacion) | Alta (alfa, beta, evaporacion, numero de hormigas) |
| Tipo de problemas donde destaca | Continuos, ajuste de parametros, optimizacion numerica | Combinatorios y continuos; diseno y seleccion | Ruteo, caminos minimos, TSP, asignacion y secuenciacion |
| Costo computacional | Bajo-medio por iteracion | Medio-alto segun evaluacion y tamano poblacional | Medio-alto por construccion de soluciones y actualizacion de feromonas |
| Paralelizacion | Buena; particulas evaluables en paralelo | Muy buena; individuos evaluables en paralelo | Buena; hormigas independientes en construccion de rutas |
| Interpretabilidad del proceso | Media; dinamica de velocidades/posiciones | Media; evolucion de aptitud y operadores | Alta en problemas de rutas por trazas de feromonas |
| Robustez ante ruido | Media; sensible a oscilaciones | Media-alta con poblaciones grandes | Media-alta por acumulacion colectiva de evidencia |
| Facilidad de implementacion | Alta (estructura simple) | Media (mas componentes de diseno) | Media-baja (matriz de feromonas y reglas probabilisticas) |


---


## 2.4 Ventajas y limitaciones de Datlas frente a otros modelos

### Ventajas de Datlas
- Enfoque práctico y comprensible para equipos multidisciplinarios.
- Integra validación de negocio durante todo el ciclo.
- Favorece trazabilidad de decisiones y resultados.
- Promueve iteración y mejora continua.
- Es adaptable a distintos tamaños de proyecto.

### Limitaciones de Datlas
- Requiere disciplina documental para mantener coherencia entre fases.
- Puede volverse lento si el equipo sobredimensiona entregables.
- Depende de calidad y disponibilidad de datos desde etapas tempranas.
- En organizaciones poco maduras, la adopción puede ser parcial.
- Tiene menor estandarización formal que metodologías ampliamente consolidadas.

### Comparacion breve con otros modelos
- Frente a enfoques ad-hoc: Datlas ofrece mayor orden y control del proceso.
- Frente a CRISP-DM: comparten enfoque iterativo; Datlas enfatiza colaboración y comunicación, mientras CRISP-DM posee mayor detalle estandarizado de fases y despliegue.
- Frente a SEMMA: Datlas integra mejor el contexto de negocio; SEMMA es más técnico y secuencial.
- Frente a KDD: ambos son iterativos, pero Datlas prioriza traducción de hallazgos a decisiones operativas.

### Contextos donde conviene Datlas
- Proyectos de alcance pequeño o mediano que requieren resultados accionables en poco tiempo.
- Equipos que necesitan una guía clara para coordinar negocio y analítica.
- Escenarios de formación, consultoría o prototipado con fuerte componente comunicativo.

### Contextos donde puede quedar corto
- Proyectos muy grandes que exigen estándares maduros de despliegue y gobierno de datos.
- Organizaciones que requieren marcos ampliamente estandarizados y muy documentados.

## Conceptos clave
- Aplicación empresarial
- Trazabilidad
- Iteración
- Madurez de datos
- Valor de negocio

## Resumen breve
Datlas demuestra utilidad en casos reales de negocio cuando se busca velocidad, claridad y comunicación efectiva de resultados. Sus ventajas principales son la flexibilidad y orientación práctica; sus limitaciones aparecen frente a modelos más consolidados cuando se requiere mayor estandarización y profundidad metodológica.

## Dudas para investigar
- ¿Qué tipo de proyectos no son buenos candidatos para Datlas?
- ¿Cómo medir retorno de inversión al aplicar Datlas en una pyme?
- ¿Qué adaptaciones necesita Datlas para equipos con metodologías ágiles?

## Ejercicios realizados
- Comparación de Datlas con CRISP-DM, SEMMA y KDD en una tabla de fortalezas y riesgos.
- Análisis de un caso real para identificar valor de negocio generado por Datlas.

## Quiz

### QUIZ 1 - U1-T2-S4 (APE4)

### Pregunta 1: Uso principal de Datlas en negocio

**Pregunta:** ¿Para qué se aplica Datlas en proyectos de negocio?

**Opciones:**
- ❌ Solo para crear dashboards sin analisis profundo.
- ✅ Para estructurar desde el problema hasta la implementacion analitica.
- ❌ Unicamente para almacenar bases de datos.

**Respuesta correcta:** Para estructurar desde el problema hasta la implementacion analitica.

**Explicacion breve:**
Datlas organiza el ciclo completo para transformar datos en decisiones accionables.

### Pregunta 2: Fortalezas de Datlas

**Pregunta:** ¿Cuál es una ventaja clave de Datlas?

**Opciones:**
- ✅ Integra validacion tecnica y de negocio.
- ❌ Evita por completo la necesidad de datos de calidad.
- ❌ Sustituye cualquier proceso de implementacion.

**Respuesta correcta:** Integra validacion tecnica y de negocio.

**Explicacion breve:**
Una fortaleza de Datlas es vincular los resultados analiticos con decisiones reales del negocio.

### Pregunta 3: Limitacion comun

**Pregunta:** ¿Qué limitación puede presentarse al usar Datlas?

**Opciones:**
- ❌ Que no permite iteraciones.
- ✅ Que requiere disciplina documental y madurez de datos.
- ❌ Que solo funciona en proyectos academicos.

**Respuesta correcta:** Que requiere disciplina documental y madurez de datos.

**Explicacion breve:**
Sin procesos claros y datos confiables, la metodologia pierde efectividad.

### Pregunta 4: Diferencia frente a SEMMA

**Pregunta:** ¿Qué diferencia importante existe entre Datlas y SEMMA?

**Opciones:**
- ❌ Datlas elimina por completo la fase de modelado.
- ✅ Datlas integra mejor el contexto de negocio y la comunicación con usuarios.
- ❌ SEMMA está más orientada a colaboración con áreas no técnicas.

**Respuesta correcta:** Datlas integra mejor el contexto de negocio y la comunicación con usuarios.

**Explicación breve:**
SEMMA se centra más en tareas técnicas; Datlas incorpora mayor conexión con necesidades de negocio.

### Pregunta 5: Contexto recomendado

**Pregunta:** ¿En qué contexto suele convenir más Datlas?

**Opciones:**
- ✅ En proyectos medianos con necesidad de resultados accionables y comunicación clara.
- ❌ Solo en macroproyectos con arquitectura de datos masiva.
- ❌ Únicamente en investigación teórica sin aplicación.

**Respuesta correcta:** En proyectos medianos con necesidad de resultados accionables y comunicación clara.

**Explicación breve:**
Datlas funciona especialmente bien cuando se requiere velocidad, claridad y alineación con usuarios finales.

### Pregunta 6: Ventaja inicial de ACO

**Pregunta:** ¿Qué ventaja inicial tiene ACO?

**Opciones:**
- ❌ Menor dependencia del tamaño de población.
- ✅ Fuerte en exploración mediante feromonas.
- ❌ Menor costo computacional por iteración.

**Respuesta correcta:** Fuerte en exploración mediante feromonas.

**Explicación breve:**
ACO destaca al inicio por su capacidad de explorar múltiples rutas y reforzar soluciones prometedoras mediante feromonas.

### Pregunta 7: Explotación prematura en ACO

**Pregunta:** ¿Qué condición puede llevar a explotación prematura en ACO?

**Opciones:**
- ✅ Poca diversidad genética.
- ❌ Mal diseño del refresco de feromonas.
- ❌ Mal ajuste de inercia.

**Respuesta correcta:** Poca diversidad genética.

**Explicación breve:**
Cuando disminuye la diversidad de soluciones candidatas, el algoritmo tiende a explotar pocas rutas y puede converger de forma prematura.

### Pregunta 8: Eficiencia de ACO

**Pregunta:** ¿Qué inconveniente tiene ACO en eficiencia?

**Opciones:**
- ❌ Requiere gran población.
- ✅ Siempre converge lento.
- ❌ Puede ser menos eficiente en casos grandes.

**Respuesta correcta:** Siempre converge lento.

**Explicación breve:**
En la unidad se destaca que ACO puede presentar convergencia lenta, especialmente en etapas tempranas de búsqueda.

### Pregunta 9: Campo de aplicacion

**Pregunta:** ¿En qué campo se utilizan los algoritmos bioinspirados para reducir peso o maximizar rigidez?

**Opciones:**
- ❌ Ingeniería y Diseño.
- ✅ Bioinformática.
- ❌ Telecomunicaciones.

**Respuesta correcta:** Bioinformática.

**Explicación breve:**
En la unidad se presenta Bioinformática como campo de aplicación relevante de algoritmos bioinspirados para este tipo de optimización.

### Pregunta 10: Multiobjetivo

**Pregunta:** ¿Qué ventaja tienen en optimización multiobjetivo?

**Opciones:**
- ✅ No pueden aplicarse a carteras financieras.
- ❌ Permiten equilibrar metas en conflicto.
- ❌ Solo buscan una meta fija.

**Respuesta correcta:** No pueden aplicarse a carteras financieras.

**Explicación breve:**
Según el contenido de la unidad, esta opción se presenta como una limitación en su aplicación al contexto de carteras financieras.

### QUIZ 2 - U1-T2-S4 (APE4)

### Pregunta 11: PSO en espacios continuos

**Pregunta:** ¿En qué tipo de problemas suele destacar PSO?

**Opciones:**
- ✅ En optimización continua y ajuste de parámetros.
- ❌ Solo en clasificación supervisada.
- ❌ Únicamente en minería de texto.

**Respuesta correcta:** En optimización continua y ajuste de parámetros.

**Explicación breve:**
PSO se adapta bien a espacios de búsqueda continuos por su dinámica de partículas.

### Pregunta 12: Diversidad en GA

**Pregunta:** ¿Qué ayuda a GA a evitar estancamiento temprano?

**Opciones:**
- ✅ Mantener diversidad poblacional.
- ❌ Eliminar la mutación por completo.
- ❌ Usar un solo individuo élite en todas las generaciones.

**Respuesta correcta:** Mantener diversidad poblacional.

**Explicación breve:**
La diversidad permite explorar regiones nuevas y reducir el riesgo de óptimos locales.

### Pregunta 13: Feromonas en ACO

**Pregunta:** ¿Qué función cumplen las feromonas en ACO?

**Opciones:**
- ✅ Guiar probabilísticamente la construcción de soluciones.
- ❌ Reemplazar la función objetivo.
- ❌ Eliminar totalmente la aleatoriedad.

**Respuesta correcta:** Guiar probabilísticamente la construcción de soluciones.

**Explicación breve:**
Las feromonas refuerzan rutas prometedoras y orientan decisiones futuras.

### Pregunta 14: Costo computacional

**Pregunta:** ¿Cuál de estos algoritmos puede elevar su costo en problemas grandes por iteración compleja?

**Opciones:**
- ✅ ACO.
- ❌ PSO en todos los casos.
- ❌ Ninguno, todos cuestan igual.

**Respuesta correcta:** ACO.

**Explicación breve:**
La construcción de rutas y actualización de feromonas puede encarecer el proceso en gran escala.

### Pregunta 15: Ajuste de parámetros

**Pregunta:** ¿Qué algoritmo suele ser más sensible al diseño de tasas de cruce y mutación?

**Opciones:**
- ✅ GA.
- ❌ PSO exclusivamente.
- ❌ ACO nunca usa parámetros.

**Respuesta correcta:** GA.

**Explicación breve:**
El desempeño de GA depende fuertemente de cómo se configuren sus operadores evolutivos.

### Pregunta 16: Exploración vs explotación

**Pregunta:** ¿Qué describe mejor el objetivo del equilibrio exploración-explotación?

**Opciones:**
- ✅ Buscar nuevas zonas sin perder refinamiento de buenas soluciones.
- ❌ Mantener siempre la misma solución inicial.
- ❌ Eliminar cualquier componente estocástico.

**Respuesta correcta:** Buscar nuevas zonas sin perder refinamiento de buenas soluciones.

**Explicación breve:**
El equilibrio evita estancamiento y mejora la calidad final de la optimización.

### Pregunta 17: Paralelización

**Pregunta:** ¿Qué característica favorece la paralelización en metaheurísticas poblacionales?

**Opciones:**
- ✅ Evaluación independiente de múltiples candidatos.
- ❌ Necesidad de una sola solución por ciclo.
- ❌ Uso obligatorio de datos secuenciales.

**Respuesta correcta:** Evaluación independiente de múltiples candidatos.

**Explicación breve:**
Individuos, partículas o hormigas pueden evaluarse en paralelo para reducir tiempos.

### Pregunta 18: Aplicación en ruteo

**Pregunta:** ¿Qué algoritmo es especialmente usado en problemas de ruteo tipo TSP?

**Opciones:**
- ✅ ACO.
- ❌ PSO únicamente.
- ❌ Regresión lineal.

**Respuesta correcta:** ACO.

**Explicación breve:**
ACO modela bien la elección de caminos y refuerzo de rutas de alta calidad.

### Pregunta 19: Convergencia prematura

**Pregunta:** ¿Qué consecuencia tiene la convergencia prematura?

**Opciones:**
- ✅ Encontrar soluciones subóptimas por pérdida de exploración.
- ❌ Garantizar el óptimo global.
- ❌ Reducir siempre el tiempo con mejor calidad.

**Respuesta correcta:** Encontrar soluciones subóptimas por pérdida de exploración.

**Explicación breve:**
Cuando se reduce demasiado la diversidad, el algoritmo deja de explorar alternativas valiosas.

### Pregunta 20: Selección de metaheurística

**Pregunta:** ¿Qué criterio es clave para elegir entre PSO, GA y ACO?

**Opciones:**
- ✅ La naturaleza del problema y el costo computacional aceptable.
- ❌ Elegir siempre el algoritmo más popular.
- ❌ Usar el que tenga menos parámetros sin analizar contexto.

**Respuesta correcta:** La naturaleza del problema y el costo computacional aceptable.

**Explicación breve:**
La elección debe considerar tipo de variables, tamaño del problema y recursos disponibles.

## Completar

### Ejercicio 1: Aplicación empresarial

**Instrucción:** Completa la oración con la palabra correcta.

Datlas ayuda a transformar datos dispersos en decisiones __________.

**Respuesta correcta:** operativas

**Explicación breve:**
La metodología está orientada a apoyar acciones concretas en procesos reales.

### Ejercicio 2: Caso de retail

**Instrucción:** Completa la oración con la palabra correcta.

En el caso Sigma Alimentos, Datlas permitió migrar reportes manuales a __________ interactivos.

**Respuesta correcta:** dashboards

**Explicación breve:**
La visualización dinámica aceleró el análisis y la toma de decisiones.

### Ejercicio 3: Fortalezas metodológicas

**Instrucción:** Completa la oración con la palabra correcta.

Una fortaleza de Datlas es su enfoque práctico y su capacidad de __________ entre fases.

**Respuesta correcta:** iteración

**Explicación breve:**
La iteración permite ajustar el proyecto según hallazgos nuevos.

### Ejercicio 4: Limitaciones

**Instrucción:** Completa la oración con la palabra correcta.

Una limitación de Datlas es su menor nivel de __________ formal frente a modelos clásicos.

**Respuesta correcta:** estandarización

**Explicación breve:**
CRISP-DM, por ejemplo, dispone de guías más consolidadas en la práctica profesional.

### Ejercicio 5: Valor generado

**Instrucción:** Completa la oración con la palabra correcta.

El valor de Datlas aumenta cuando existe buena comunicación entre el equipo técnico y el área de __________.

**Respuesta correcta:** negocio

**Explicación breve:**
La alineación técnica-negocio facilita adopción de resultados.

### Ejercicio 6: Contexto de uso

**Instrucción:** Completa la oración con la palabra correcta.

Datlas suele ser conveniente en proyectos de alcance pequeño o __________.

**Respuesta correcta:** mediano

**Explicación breve:**
En estos escenarios puede entregar insights accionables con rapidez.

## Actividades

- Analizar un caso real de negocio y mapearlo con las fases de Datlas.
- Elaborar una tabla comparativa Datlas vs CRISP-DM vs enfoque ad-hoc.
- Definir tres indicadores para medir impacto despues del despliegue.

