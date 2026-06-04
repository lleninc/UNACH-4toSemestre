# EFT1 - Evaluación de la fundamentación teórica del primer parcial

## 1) Serie de potencias para \(\sqrt{1+x}\) con \(x=0.6\)

La expansión usada es:

\[
\sqrt{1+x} \approx 1 + \frac{1}{2}x - \frac{1}{8}x^2 + \frac{1}{16}x^3 - \frac{5}{128}x^4 + \cdots
\]

Para \(x=0.6\), el valor exacto es:

\[
\sqrt{1.6} = 1.26491
\]

| Número de términos | Valor aproximado | Error absoluto | Error relativo porcentual |
|---|---:|---:|---:|
| 1 | 1.00000 | 0.26491 | 20.94306 |
| 2 | 1.30000 | 0.03509 | 2.77402 |
| 3 | 1.25500 | 0.00991 | 0.78354 |
| 4 | 1.26850 | 0.00359 | 0.28373 |

## 2) Método de Newton-Raphson

Se desea encontrar las raíces de:

\[
f(x)=e^x-x^2-2
\]

Derivando:

\[
f'(x)=e^x-2x
\]

La fórmula iterativa es:

\[
x_{n+1}=x_n-\frac{e^{x_n}-x_n^2-2}{e^{x_n}-2x_n}
\]

Tomando como valor inicial \(x_0=1.00000\), se obtienen 4 iteraciones:

| Iteración | \(x_n\) |
|---|---:|
| 0 | 1.00000 |
| 1 | 1.39221 |
| 2 | 1.32323 |
| 3 | 1.31909 |
| 4 | 1.31907 |

Por lo tanto, la raíz aproximada es:

\[
x \approx 1.31907
\]

## 3) Método de Jacobi

Sistema:

\[
18x_1+3x_2+2x_3=29
\]

\[
2x_1+16x_2+x_3=25
\]

\[
3x_1+2x_2+20x_3=46
\]

Con valores iniciales:

\[
x_1^{(0)}=0,\quad x_2^{(0)}=0,\quad x_3^{(0)}=0
\]

Despejando:

\[
x_1=\frac{29-3x_2-2x_3}{18}
\]

\[
x_2=\frac{25-2x_1-x_3}{16}
\]

\[
x_3=\frac{46-3x_1-2x_2}{20}
\]

Resultados de dos iteraciones:

| Iteración | \(x_1\) | \(x_2\) | \(x_3\) |
|---|---:|---:|---:|
| 0 | 0.00000 | 0.00000 | 0.00000 |
| 1 | 1.61111 | 1.56250 | 2.30000 |
| 2 | 1.09514 | 1.21736 | 1.90208 |

## Conclusión

La serie de potencias aproxima el valor de \(\sqrt{1.6}\) con error cada vez menor al aumentar el número de términos. En Newton-Raphson, con \(x_0=1\), la solución converge rápidamente a una raíz aproximada de \(1.31907\). Finalmente, el método de Jacobi produce una secuencia iterativa para el sistema lineal dado, mostrando una aproximación progresiva en dos iteraciones.