"""
BINARIO A DECIMAL -> NO DETERMINÍSTICO
Crea un programa que se encargue de transformar un número binario a decimal sin utilizar funciones propios que lo hagan directamente

Determinar qué operaciones se emplean y su costo relativo:
Binario

Determinar conjuntos de datos:
Si es el último valor ingresado se realiza con potencia de 2

Análisis a priori:
Se agarra el último carácter y se eleva, todo ello en un tiempo constante que sucede.


Análisis a posteriori:
El tiempo conforme se va a ir aumentando a medida que la cantidad sea más grande.
"""
class Pila:
    def __init__(self):
        self.items = []

    def push(self, dato):
        self.items.append(dato)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0


def binario_a_decimal(binario):
    pila = Pila()

    for digito in binario:
        if digito in '01':
            pila.push(int(digito))
        else:
            return "Error: El string contiene caracteres no binarios."

    decimal = 0
    potencia = 0

    while not pila.is_empty():
        valor = pila.pop()
        decimal += valor * (2 ** potencia)
        potencia += 1

    return decimal

binario1 = "1011"
print(f"Binario: {binario1}")
print(f"Decimal: {binario_a_decimal(binario1)}")

print("-" * 20)

binario2 = "110101"
print(f"Binario: {binario2}")
print(f"Decimal: {binario_a_decimal(binario2)}")

print("-" * 20)

binario_invalido = "1021"
print(f"Binario: {binario_invalido}")
print(f"Decimal: {binario_a_decimal(binario_invalido)}")