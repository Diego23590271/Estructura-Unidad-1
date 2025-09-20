# 1) Mostrar menú de patrones de filas a imprimir.
print("=== Generador de filas (sin funciones) ===")
print("Elige un patrón:")
print("  1) Triángulo izquierdo de asteriscos")
print("  2) Filas numéricas (1 12 123 ...)")
print("  3) Cuadrado N x N de asteriscos")
print("  4) Pirámide centrada de asteriscos")
print("  5) Escalera con un texto (repite un texto por fila)")

# 2) Leer opción del usuario.
opcion = input("Opción (1-5): ")

# 3) Leer el número de filas (N). Validación simple para que sea entero y > 0.
entrada = input("Número de filas (N): ")
# 3.1- Convertir a entero si es posible; si falla, usar N=1.
if entrada.isdigit():
    N = int(entrada)
    if N <= 0:
        N = 1
else:
    N = 1

# 4) Si la opción es 5 (texto), pedir el texto ahora (sin funciones).
texto = ""
if opcion == "5":
    texto = input("Escribe el texto a repetir: ")

# 5) Según la opción, imprimir el patrón correspondiente SIN usar funciones.

# 5.1- Triángulo izquierdo de asteriscos
if opcion == "1":
    i = 1
    while i <= N:
        print("*" * i)
        i += 1

# 5.2- Filas numéricas (1, 12, 123, ..., hasta N)
elif opcion == "2":
    i = 1
    while i <= N:
        # Construir la cadena "123...i" sin funciones propias: usar bucle
        j = 1
        linea = ""
        while j <= i:
            linea += str(j)
            j += 1
        print(linea)
        i += 1

# 5.3- Cuadrado N x N de asteriscos
elif opcion == "3":
    fila = 1
    while fila <= N:
        print("*" * N)
        fila += 1

# 5.4- Pirámide centrada de asteriscos
elif opcion == "4":
    i = 1
    while i <= N:
        espacios = " " * (N - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)
        i += 1

# 5.5- Escalera con un texto (repite el texto i veces por fila)
elif opcion == "5":
    i = 1
    while i <= N:
        j = 1
        linea = ""
        while j <= i:
            if j > 1:
                linea += " "
            linea += texto
            j += 1
        print(linea)
        i += 1

# 5.6- Si la opción no es válida, mostrar un mensaje.
else:
    print("Opción no válida. Ejecuta de nuevo el programa y elige 1-5.")
# ================== FIN DEL PROGRAMA ==================
