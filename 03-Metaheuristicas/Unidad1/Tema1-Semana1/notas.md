# 03-Metaheuristicas - U1 T1 S1

## Objetivo de la semana
Comprender qué son los algoritmos bioinspirados, por qué surgieron y cuáles son sus bases naturales para resolver problemas complejos.

---

## 1.1 ¿Qué son los algoritmos bioinspirados?

Los algoritmos bioinspirados son técnicas de optimización que imitan procesos naturales para encontrar soluciones de alta calidad en problemas difíciles. En lugar de seguir un procedimiento exacto rígido, exploran múltiples alternativas y ajustan su comportamiento de manera adaptativa.

**Motivaciones principales:**
- Resolver problemas donde los métodos exactos son muy costosos.
- Modelar estrategias eficientes observadas en la naturaleza.
- Lograr soluciones aproximadas útiles en tiempos razonables.

**Ejemplo representativo:**
La optimización por enjambre de partículas (PSO) se inspira en el movimiento coordinado de aves para explorar el espacio de búsqueda.

---

## 1.2 Bases conceptuales inspiradas en sistemas naturales

La base de estos algoritmos proviene de observar fenómenos naturales robustos y trasladar su lógica al cómputo.

**Inspiración biológica:**
- Evolución natural: selección, recombinación y mutación.
- Comportamiento colectivo: hormigas, abejas, aves y peces.

**Inspiración física:**
- Recocido Simulado: proceso de enfriamiento controlado para escapar de óptimos locales.

**Inspiración ecológica:**
- Competencia, cooperación y equilibrio entre especies para mantener diversidad.

**Idea central del tema:**
La naturaleza aporta mecanismos adaptativos y eficientes que pueden convertirse en estrategias de búsqueda computacional.

## Conceptos clave
- Optimización bioinspirada
- Población de soluciones
- Selección, cruce y mutación
- Comportamiento colectivo
- Estigmergia
- Recocido Simulado
- Adaptación

## Resumen breve
Los algoritmos bioinspirados aprovechan principios de biología, física y ecología para resolver problemas complejos con estrategias adaptativas. Su ventaja está en equilibrar exploración y explotación para encontrar soluciones útiles sin exigir modelos exactos del problema.

## Dudas para investigar
- ¿Por qué GA y PSO son de los algoritmos más usados en optimización?
- ¿Qué relación existe entre estigmergia y cooperación en ACO?
- ¿Cómo evaluar robustez y estabilidad en una metaheurística?

## Ejercicios realizados
- Identificación de fuentes de inspiración natural en GA, PSO, ACO y Recocido Simulado.
- Clasificación de ejemplos por base biológica, física o ecológica.

## Quiz

### Pregunta 1: Definición general

**Pregunta:** ¿Qué caracteriza a un algoritmo bioinspirado?

**Opciones:**
- ❌ Que siempre entrega la solución exacta del problema.
- ✅ Que toma ideas de procesos naturales para optimizar.
- ❌ Que solo sirve para problemas biológicos.

**Respuesta correcta:** Que toma ideas de procesos naturales para optimizar.

**Explicación breve:**
Su esencia es traducir comportamientos naturales a mecanismos computacionales de búsqueda.

### Pregunta 2: ACO y naturaleza

**Pregunta:** ¿Qué comportamiento inspira el algoritmo ACO?

**Opciones:**
- ✅ La búsqueda de alimento mediante feromonas.
- ❌ La metamorfosis de insectos.
- ❌ El vuelo individual sin cooperación.

**Respuesta correcta:** La búsqueda de alimento mediante feromonas.

**Explicación breve:**
ACO usa rastros de feromonas como memoria colectiva para construir rutas eficientes.

### Pregunta 3: Beneficio práctico

**Pregunta:** ¿Cuál es un beneficio típico de los algoritmos bioinspirados?

**Opciones:**
- ❌ Requieren modelos matemáticos exactos del problema.
- ✅ Obtienen soluciones aproximadas buenas en problemas complejos.
- ❌ Solo funcionan con datos pequeños.

**Respuesta correcta:** Obtienen soluciones aproximadas buenas en problemas complejos.

**Explicación breve:**
Son útiles cuando el espacio de soluciones es grande o no lineal.

### Pregunta 4: Inspiración de PSO

**Pregunta:** ¿En qué fenómeno se inspira PSO?

**Opciones:**
- ❌ En la fermentación bacteriana.
- ✅ En el movimiento colectivo de aves o peces.
- ❌ En el templado de metales.

**Respuesta correcta:** En el movimiento colectivo de aves o peces.

**Explicación breve:**
PSO modela cooperación social y aprendizaje individual para moverse hacia mejores posiciones.

### Pregunta 5: Fuente no única

**Pregunta:** ¿La biología es la única fuente de inspiración bioinspirada?

**Opciones:**
- ❌ Sí, exclusivamente.
- ✅ No, también hay inspiración física y ecológica.
- ❌ Solo existe inspiración ecológica.

**Respuesta correcta:** No, también hay inspiración física y ecológica.

**Explicación breve:**
Además de la biología, se usan modelos físicos y ecológicos para diseñar metaheurísticas.

## Completar

### Ejercicio 1: Naturaleza y cómputo

**Instrucción:** Completa la oración con la palabra correcta.

Los algoritmos bioinspirados trasladan principios de la __________ al diseño de estrategias de optimización.

**Respuesta correcta:** naturaleza

**Explicación breve:**
La observación de sistemas naturales es el punto de partida de estas técnicas.

### Ejercicio 2: Estrategia evolutiva

**Instrucción:** Completa la oración con la palabra correcta.

En algoritmos evolutivos, una población mejora mediante selección, cruce y __________.

**Respuesta correcta:** mutación

**Explicación breve:**
La mutación introduce variabilidad para evitar convergencia prematura.

### Ejercicio 3: ACO

**Instrucción:** Completa la oración con la palabra correcta.

ACO utiliza rastros de __________ para reforzar rutas prometedoras.

**Respuesta correcta:** feromonas

**Explicación breve:**
Las feromonas permiten comunicación indirecta entre agentes.

### Ejercicio 4: PSO

**Instrucción:** Completa la oración con la palabra correcta.

PSO se inspira en la dinámica de __________ que buscan alimento en grupo.

**Respuesta correcta:** aves

**Explicación breve:**
El movimiento colectivo guía la búsqueda de soluciones mejores.

### Ejercicio 5: Recocido Simulado

**Instrucción:** Completa la oración con la palabra correcta.

El Recocido Simulado toma su analogía principal de un proceso __________.

**Respuesta correcta:** físico

**Explicación breve:**
Se basa en enfriamiento gradual para escapar de óptimos locales.

### Ejercicio 6: Objetivo general

**Instrucción:** Completa la oración con la palabra correcta.

Las metaheurísticas bioinspiradas buscan soluciones de alta __________ en problemas complejos.

**Respuesta correcta:** calidad

**Explicación breve:**
No siempre garantizan exactitud, pero sí resultados robustos y útiles.
