# 02-Machine-Learning - U2 T2 S4

## Notas de clase

## Tema 2. Modelos avanzados de clasificación y regresión

### 2.3. Interpretación y análisis de errores

- Entrenar un modelo no es suficiente; también hay que entender por qué se equivoca.
- El análisis de errores ayuda a detectar limitaciones del modelo, sesgos en los datos y oportunidades de mejora.
- En clasificación, los errores más importantes son:
	- **Falsos positivos (FP)**: el modelo predice positivo, pero la clase real es negativa.
	- **Falsos negativos (FN)**: el modelo predice negativo, pero la clase real es positiva.
- En regresión, los errores suelen analizarse con:
	- **MSE** (error cuadrático medio).
	- **MAE** (error absoluto medio).
	- Gráficos de residuos para detectar patrones sistemáticos.
- Interpretación clave:
	- Errores sistemáticos pueden indicar sesgo o un modelo demasiado simple.
	- Errores muy dispersos o aleatorios y altos pueden reflejar varianza alta y sobreajuste.
	- En problemas desbalanceados, una alta accuracy puede ser engañosa.

### 2.4. Aplicaciones prácticas en datasets reales

- El trabajo con datasets reales introduce ruido, valores faltantes y desbalance de clases.
- Casos de uso mencionados:
	- **Spam / detección de correo malicioso**: útil para estudiar desbalance y métricas como ROC-AUC.
	- **Salud / Heart Disease**: los falsos negativos son críticos porque pueden ocultar un diagnóstico real.
	- **Imágenes / MNIST o Fashion-MNIST**: permiten estudiar confusiones entre clases visualmente similares.
	- **Regresión / House Prices**: los residuos ayudan a ver si el modelo subestima precios altos o sigue un sesgo hacia el promedio.
- Usar datos reales conecta la teoría con aplicaciones en salud, finanzas y seguridad digital.
- El error no solo indica fallos: también revela cómo mejorar el modelo y qué límites tiene.

## Quiz

## Actividades

