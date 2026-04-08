# 03-Metaheuristicas - U1 T1 S2

## Objetivo de la semana
Reconocer cómo se clasifican los algoritmos bioinspirados y qué los hace diferentes frente a otras metaheurísticas.

---

## 1.3 Clasificación general de los algoritmos bioinspirados

La clasificación general del tema agrupa los algoritmos bioinspirados según el fenómeno natural en el que se inspiran.

**Algoritmos evolutivos:**
- Se basan en la selección natural y la genética.
- Trabajan con una población de soluciones que evoluciona mediante selección, cruce y mutación.

**Algoritmos de enjambre:**
- Se inspiran en el comportamiento colectivo de hormigas, aves, peces y otros animales sociales.
- Ejemplos: PSO, ACO y variantes modernas como lobos grises, ballenas, Harris Hawks y Moth-flame.

**Algoritmos físicos:**
- Modelan fenómenos como enfriamiento de metales, propagación de calor o dinámica de partículas.
- Un ejemplo clásico es el Recocido Simulado.

**Algoritmos ecológicos:**
- Se inspiran en competencia, cooperación y simbiosis entre especies.
- Simulan ecosistemas donde las entidades compiten o cooperan para mejorar soluciones.

---

## 1.4 Características comunes y diferenciadoras frente a otras metaheurísticas

Los algoritmos bioinspirados comparten varias propiedades importantes:

**Características comunes:**
- Resuelven problemas muy complejos sin requerir conocer a fondo su estructura matemática.
- Exploran el espacio de soluciones de forma diversificada.
- Son adaptables a distintas condiciones del problema.
- Pueden paralelizarse con eficiencia en entornos distribuidos o de alto rendimiento.

**Diferencias frente a otras metaheurísticas:**
- Su analogía con la naturaleza los hace más intuitivos y fáciles de interpretar.
- No operan con reglas fijas como muchas heurísticas tradicionales.
- Exploran de forma dinámica, imitando procesos evolutivos o de comportamiento colectivo.

**Comparación esencial:**
- Los algoritmos bioinspirados están basados en fenómenos naturales.
- Otras metaheurísticas pueden basarse más en reglas matemáticas o heurísticas diseñadas directamente por el ser humano.

## Conceptos clave
- Clasificación por origen natural
- Evolución
- Enjambre
- Sistemas físicos
- Sistemas ecológicos
- Adaptabilidad
- Paralelización

## Resumen breve
La clasificación de los algoritmos bioinspirados ayuda a entender qué fenómeno natural los inspira. Sus características más fuertes son la adaptabilidad, la exploración del espacio de soluciones y la capacidad de resolver problemas complejos con una interpretación intuitiva.

## Dudas para investigar
- ¿Qué ventaja práctica tiene usar un algoritmo de enjambre sobre uno evolutivo?
- ¿Cuándo conviene un algoritmo físico en lugar de uno ecológico?
- ¿Qué tan importante es la paralelización en problemas grandes?

## Ejercicios realizados
- Clasificación de ejemplos como PSO, ACO y Recocido Simulado.

## Quiz

### Pregunta 1: Ventaja general de los algoritmos bioinspirados

**Pregunta:** ¿Qué ventaja general tienen los algoritmos bioinspirados?

**Opciones:**
- ❌ Solo se aplican en problemas simples.
- ❌ Dependen de reglas fijas invariables.
- ✅ Se adaptan dinámicamente al problema.

**Respuesta correcta:** Se adaptan dinámicamente al problema.

**Explicación breve:**
Los algoritmos bioinspirados ajustan su búsqueda según el comportamiento del problema, lo que les permite explorar y explotar mejor el espacio de soluciones.

### Pregunta 2: Ventaja en aplicabilidad

**Pregunta:** ¿Qué ventaja tienen en aplicabilidad?

**Opciones:**
- ✅ Pueden usarse en ingeniería, logística, robótica e IA.
- ❌ No pueden aplicarse en bioinformática.
- ❌ Solo sirven en problemas matemáticos muy específicos.

**Respuesta correcta:** Pueden usarse en ingeniería, logística, robótica e IA.

**Explicación breve:**
Su flexibilidad les permite adaptarse a distintos tipos de problemas reales, por eso se usan en muchas áreas de aplicación.

### Pregunta 3: Características de los algoritmos evolutivos

**Pregunta:** ¿Qué caracteriza a los algoritmos evolutivos?

**Opciones:**
- ✅ Usan selección, cruce y mutación inspirados en la genética.
- ❌ Dependen únicamente de fórmulas algebraicas exactas.
- ❌ Trabajan siempre con una sola solución.

**Respuesta correcta:** Usan selección, cruce y mutación inspirados en la genética.

**Explicación breve:**
Los algoritmos evolutivos manejan una población de soluciones y aplican operadores como selección, cruce y mutación para mejorarla de forma iterativa.

### Pregunta 4: Ejemplo de algoritmo físico

**Pregunta:** ¿Cuál es un ejemplo de algoritmo físico?

**Opciones:**
- ❌ Optimización por Colonia de Hormigas.
- ❌ Optimización por Enjambre de Partículas.
- ✅ Recocido Simulado.

**Respuesta correcta:** Recocido Simulado.

**Explicación breve:**
El Recocido Simulado se inspira en el proceso físico de enfriamiento de metales y es un ejemplo clásico de algoritmo basado en fenómenos físicos.

### Pregunta 5: Características de los algoritmos de enjambre

**Pregunta:** ¿Qué caracteriza a los algoritmos de enjambre?

**Opciones:**
- ❌ La resolución de problemas solo con ecuaciones lineales.
- ✅ El comportamiento colectivo inspirado en animales sociales.
- ❌ El trabajo individual de una sola partícula.

**Respuesta correcta:** El comportamiento colectivo inspirado en animales sociales.

**Explicación breve:**
Los algoritmos de enjambre se inspiran en la cooperación de insectos, aves o peces para resolver problemas de forma distribuida y coordinada.

## Completar

### Ejercicio 1: Algoritmos evolutivos

**Instrucción:** Completa la oración con la palabra correcta.

Los algoritmos __________ se inspiran en la selección natural y la genética, aplicando operadores como selección, cruce y mutación.

**Respuesta correcta:** evolutivos

**Explicación breve:**
Los algoritmos evolutivos toman ideas de la evolución biológica para mejorar una población de soluciones de manera iterativa.

### Ejercicio 2: Optimización por Enjambre de Partículas

**Instrucción:** Completa la oración con la palabra correcta.

La Optimización por Enjambre de Partículas ____________ se inspira en el comportamiento colectivo de las aves.

**Respuesta correcta:** PSO

**Explicación breve:**
PSO significa Particle Swarm Optimization y toma inspiración del movimiento grupal de aves y peces para buscar soluciones.

### Ejercicio 3: Recocido Simulado

**Instrucción:** Completa la oración con la palabra correcta.

El algoritmo de ____ Simulado modela el proceso metalúrgico de calentamiento y enfriamiento para encontrar soluciones óptimas.

**Respuesta correcta:** Recocido

**Explicación breve:**
El Recocido Simulado se inspira en el enfriamiento controlado de metales para explorar el espacio de soluciones y evitar quedar atrapado en óptimos locales.

### Ejercicio 4: Algoritmos ecológicos

**Instrucción:** Completa la oración con la palabra correcta.

Los algoritmos _______ toman como referencia interacciones entre especies como competencia y cooperación en ecosistemas.

**Respuesta correcta:** ecológicos

**Explicación breve:**
Los algoritmos ecológicos imitan dinámicas de ecosistemas para modelar cooperación, competencia y adaptación entre soluciones.

### Ejercicio 5: Conocimiento previo del problema

**Instrucción:** Completa la oración con la palabra correcta.

Una característica común de los algoritmos bioinspirados es que no requieren un conocimiento previo de la __________ matemática del problema.

**Respuesta correcta:** estructura

**Explicación breve:**
Estos algoritmos pueden trabajar sin modelar completamente la estructura matemática del problema, lo que los hace útiles en escenarios complejos.

### Ejercicio 6: Exploración y explotación

**Instrucción:** Completa la oración con la palabra correcta.

Los algoritmos bioinspirados equilibran la exploración global y la explotación local mediante mecanismos __________.

**Respuesta correcta:** estocásticos

**Explicación breve:**
Los mecanismos adaptativos permiten ajustar la búsqueda según el estado del proceso, favoreciendo tanto la exploración amplia como el refinamiento local.

### Ejercicio 7: Poblaciones de soluciones

**Instrucción:** Completa la oración con la palabra correcta.

A diferencia de las heurísticas tradicionales, los algoritmos bioinspirados mantienen poblaciones de soluciones para garantizar la ______ en la búsqueda.

**Respuesta correcta:** diversidad

**Explicación breve:**
Trabajar con poblaciones permite mantener diversidad de candidatos, evitando la convergencia temprana y mejorando la exploración del espacio de soluciones.

### Ejercicio 8: Interpretación de los algoritmos

**Instrucción:** Completa la oración con la palabra correcta.

Los algoritmos bioinspirados son fácilmente __________, ya que imitan fenómenos de la naturaleza como evolución y ecología.

**Respuesta correcta:** intuitivos

**Explicación breve:**
Al estar basados en analogías naturales, su lógica de búsqueda suele resultar más intuitiva y sencilla de comprender.

### Ejercicio 9: Paralelización

**Instrucción:** Completa la oración con la palabra correcta.

Una ventaja de los algoritmos bioinspirados es que pueden ejecutarse en entornos de computación ____________ gracias a su diseño paralelizable.

**Respuesta correcta:** distribuida

**Explicación breve:**
Muchos algoritmos bioinspirados operan con múltiples soluciones en paralelo, lo que facilita su implementación en arquitecturas distribuidas o de alto rendimiento.

