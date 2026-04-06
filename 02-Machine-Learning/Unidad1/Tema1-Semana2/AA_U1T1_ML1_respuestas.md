# AA U1T1 ML1 - Respuestas (version natural)

## 1) Que es el aprendizaje automatico y en que se diferencia de la programacion tradicional
El aprendizaje automatico (Machine Learning) es una forma de crear sistemas que aprenden a partir de datos. En lugar de programar todas las reglas una por una, se entrena un modelo con ejemplos para que identifique patrones y pueda predecir o tomar decisiones.

La diferencia principal con la programacion tradicional es esta:
- Programacion tradicional: el programador define las reglas y la computadora las ejecuta.
- Machine Learning: el modelo aprende las reglas desde los datos de entrenamiento.

## 2) Clasificacion de casos
### a) Un sistema que recomienda peliculas en Netflix
Tipo: Aprendizaje supervisado (en muchos sistemas reales se combina con enfoques hibridos).

Justificacion: el sistema usa historiales de usuarios (vistas, valoraciones, clics) para estimar que contenido podria gustar.

### b) Un robot que aprende a caminar evitando obstaculos mediante ensayo y error
Tipo: Aprendizaje por refuerzo.

Justificacion: el robot prueba acciones, recibe recompensa o castigo y ajusta su estrategia para mejorar con el tiempo.

### c) Un algoritmo que agrupa clientes segun patrones de compra sin etiquetas previas
Tipo: Aprendizaje no supervisado.

Justificacion: no existen etiquetas de salida; el objetivo es descubrir grupos naturales en los datos (clustering).

## 3) Tres aplicaciones reales de ML en ingenieria o ciencias aplicadas
1. Mantenimiento predictivo en industria: anticipar fallas de equipos a partir de sensores.
2. Deteccion automatica de defectos en manufactura: clasificar piezas buenas y defectuosas con vision computacional.
3. Prediccion de demanda energetica: mejorar planificacion y uso eficiente de recursos.

## 4) Dos desafios eticos o tecnicos del uso de ML
1. Sesgo en los datos: si el conjunto de entrenamiento no representa bien la realidad, el modelo puede producir decisiones injustas.
2. Falta de interpretabilidad: algunos modelos son dificiles de explicar, lo cual complica su uso en areas sensibles (salud, justicia, finanzas).

## 5) Calcular X x w e interpretar el resultado
Datos:

X = [[1, 2, 3],
     [4, 5, 6]]

w = [[0.2],
     [0.5],
     [0.3]]

Calculo:
- Primera fila: 1(0.2) + 2(0.5) + 3(0.3) = 0.2 + 1.0 + 0.9 = 2.1
- Segunda fila: 4(0.2) + 5(0.5) + 6(0.3) = 0.8 + 2.5 + 1.8 = 5.1

Resultado:

X x w = [[2.1],
         [5.1]]

Interpretacion:
Cada salida es una combinacion lineal de las variables de entrada. Los pesos indican que tanto aporta cada caracteristica al resultado final.

## 6) Probabilidad con dos sensores independientes
Datos:
- P(A) = 0.88
- P(B) = 0.70
- A y B son independientes

### a) P(A interseccion B)
P(A interseccion B) = P(A) * P(B) = 0.88 * 0.70 = 0.616

### b) En el documento parece repetirse la interseccion. Si se interpreta como union:
P(A union B) = P(A) + P(B) - P(A interseccion B)

P(A union B) = 0.88 + 0.70 - 0.616 = 0.964

Nota: si el literal b realmente queria otra vez P(A interseccion B), entonces el valor vuelve a ser 0.616.

### c) Interpretacion en vision computacional
- P(A interseccion B) = 0.616: probabilidad de que ambos sensores detecten el objeto al mismo tiempo (mayor confiabilidad conjunta).
- P(A union B) = 0.964: probabilidad de que al menos uno detecte el objeto (alta cobertura del sistema).

## 7) Papel de librerias en Python
### a) NumPy
Sirve para trabajar con arreglos y operaciones numericas de forma eficiente.

### b) Pandas
Permite cargar, limpiar y analizar datos tabulares con DataFrame.

### c) scikit-learn
Se usa para entrenar y evaluar modelos de ML clasico (clasificacion, regresion y clustering).

### d) Matplotlib
Se utiliza para visualizar datos y resultados mediante graficos.

## 8) Codigo en Python para promedio de edades con NumPy
```python
import numpy as np

edades = np.array([18, 21, 20, 19, 22, 24, 23, 20, 21, 25])
promedio = np.mean(edades)

print("Edades:", edades)
print("Promedio de edades:", promedio)
```

Salida esperada:
- Promedio de edades = 21.3

## Bibliografia
1. Benitez, R., Escudero, G., Kanaan, S., y Rodo, D. M. (2018). Inteligencia artificial avanzada. Editorial UOC.
2. Liz Marzan, E. (2022). Apuntes de algebra lineal. Universidade de Vigo. https://www.dma.uvigo.es/~eliz/pdf/apuntes-2022.pdf
3. Rengifo, E. (2023). Estadistica y probabilidad (1a ed. corregida). ResearchGate. https://doi.org/10.13140/RG.2.2.35392.05122
4. Alpaydin, E. (2021). Machine Learning (4th ed.). MIT Press.
5. Bishop, C. M. (2006). Pattern Recognition and Machine Learning. Springer.

## Recomendaciones de entrega
1. Pasa estas respuestas a mano en hojas A4, como pide la actividad.
2. En las preguntas 5 y 6 muestra todo el procedimiento matematico.
3. Marca cada respuesta final en un recuadro rojo.
4. Ejecuta el codigo, toma captura del script y de la salida.
5. Escanea a PDF y nombra el archivo: Apellido_Nombre_Grupo_X.
