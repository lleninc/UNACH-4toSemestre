# AA1CDIA - Metodos Numericos y Problemas Complejos

## Apartado A: Conversion entre sistemas numericos

### 1) Decimal a binario (procedimiento manual)

#### a) 28_10
Divisiones sucesivas entre 2:
- 28 / 2 = 14, residuo 0
- 14 / 2 = 7, residuo 0
- 7 / 2 = 3, residuo 1
- 3 / 2 = 1, residuo 1
- 1 / 2 = 0, residuo 1

Leyendo residuos de abajo hacia arriba:
- 28_10 = 11100_2

#### b) 64_10
- 64 / 2 = 32, residuo 0
- 32 / 2 = 16, residuo 0
- 16 / 2 = 8, residuo 0
- 8 / 2 = 4, residuo 0
- 4 / 2 = 2, residuo 0
- 2 / 2 = 1, residuo 0
- 1 / 2 = 0, residuo 1

Leyendo residuos de abajo hacia arriba:
- 64_10 = 1000000_2

#### c) 91_10
- 91 / 2 = 45, residuo 1
- 45 / 2 = 22, residuo 1
- 22 / 2 = 11, residuo 0
- 11 / 2 = 5, residuo 1
- 5 / 2 = 2, residuo 1
- 2 / 2 = 1, residuo 0
- 1 / 2 = 0, residuo 1

Leyendo residuos de abajo hacia arriba:
- 91_10 = 1011011_2

---

### 2) Binario a decimal

#### a) 110101_2
= 1*2^5 + 1*2^4 + 0*2^3 + 1*2^2 + 0*2^1 + 1*2^0
= 32 + 16 + 0 + 4 + 0 + 1 = 53

- 110101_2 = 53_10

#### b) 101110_2
= 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 0*2^0
= 32 + 0 + 8 + 4 + 2 + 0 = 46

- 101110_2 = 46_10

#### c) 111000_2
= 1*2^5 + 1*2^4 + 1*2^3 + 0*2^2 + 0*2^1 + 0*2^0
= 32 + 16 + 8 + 0 + 0 + 0 = 56

- 111000_2 = 56_10

---

### 3) Decimal fraccionario a binario

#### a) 0.625_10
Multiplicaciones por 2:
- 0.625*2 = 1.25 -> bit 1
- 0.25*2 = 0.5 -> bit 0
- 0.5*2 = 1.0 -> bit 1

- 0.625_10 = 0.101_2

#### b) 0.4375_10
- 0.4375*2 = 0.875 -> bit 0
- 0.875*2 = 1.75 -> bit 1
- 0.75*2 = 1.5 -> bit 1
- 0.5*2 = 1.0 -> bit 1

- 0.4375_10 = 0.0111_2

#### c) 0.8125_10
- 0.8125*2 = 1.625 -> bit 1
- 0.625*2 = 1.25 -> bit 1
- 0.25*2 = 0.5 -> bit 0
- 0.5*2 = 1.0 -> bit 1

- 0.8125_10 = 0.1101_2

---

### 4) Binario fraccionario a decimal

#### a) 0.1011_2
= 1*(1/2) + 0*(1/4) + 1*(1/8) + 1*(1/16)
= 0.5 + 0 + 0.125 + 0.0625 = 0.6875

- 0.1011_2 = 0.6875_10

#### b) 0.0101_2
= 0*(1/2) + 1*(1/4) + 0*(1/8) + 1*(1/16)
= 0 + 0.25 + 0 + 0.0625 = 0.3125

- 0.0101_2 = 0.3125_10

#### c) 0.1110_2
= 1*(1/2) + 1*(1/4) + 1*(1/8) + 0*(1/16)
= 0.5 + 0.25 + 0.125 + 0 = 0.875

- 0.1110_2 = 0.875_10


## Apartado B: Representacion numerica en el computador

### 1) Binario con signo (8 bits, magnitud con signo)

Regla usada:
- Primer bit: signo (0 positivo, 1 negativo)
- 7 bits restantes: magnitud en binario

a) +7  -> 00000111
b) -12 -> 10001100
c) -3  -> 10000011
d) +20 -> 00010100
e) +5  -> 00000101

### 2) Tabla estandar de punto flotante (IEEE 754)

| Precision | Bits de signo | Bits de exponente | Bits de mantisa |
|---|---:|---:|---:|
| Simple (32 bits) | 1 | 8 | 23 |
| Doble (64 bits)  | 1 | 11 | 52 |


## Apartado C: Programacion y conversion numerica en Python

Programa para convertir un entero decimal a binario mediante divisiones sucesivas:

```python
def decimal_a_binario(n):
    if n == 0:
        return "0"

    residuos = []
    while n > 0:
        residuos.append(str(n % 2))
        n //= 2

    return "".join(reversed(residuos))

# Ejemplo de uso
numero = int(input("Ingrese un numero decimal entero: "))
print("Binario:", decimal_a_binario(numero))
```

Ejemplo de prueba:
- Entrada: 91
- Salida: 1011011


## Nota final para tu entrega a mano
- Copia los procedimientos completos en hoja cuadriculada.
- Encierra cada respuesta final en recuadro de color (como pide la guia).
- Para el apartado C, adjunta captura del codigo y del resultado en ejecucion.
