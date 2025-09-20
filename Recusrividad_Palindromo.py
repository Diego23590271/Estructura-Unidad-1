def es_palindromo(s: str) -> bool:
    """
    Verifica recursivamente si s es palíndromo (exacto; sensible
    a espacios y mayúsculas).
    """
    if len(s) <= 1:  # Caso base: cadena vacía o de un solo carácter
        return True
    if s[0] != s[-1]:  # Comparación directa
        return False
    return es_palindromo(s[1:-1])  # Paso recursivo


def es_palindromo_normalizado(s: str) -> bool:
    """
    Variante que ignora espacios y mayúsculas.
    """
    t = "".join(ch.lower() for ch in s if not ch.isspace())
    return es_palindromo(t)


# Pruebas
assert es_palindromo("reconocer") is True
assert es_palindromo("python") is False
assert es_palindromo("") is True
assert es_palindromo("a") is True
assert es_palindromo_normalizado("Anita lava la tina") is True

print("Todas las pruebas pasaron correctamente")

