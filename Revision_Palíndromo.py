from collections import deque

def es_palindromo(texto: str) -> bool:
    pila = []
    cola = deque()

    for caracter in texto:
        if caracter.isalnum():  
            caracter_limpio = caracter.lower()
            pila.append(caracter_limpio)
            cola.append(caracter_limpio)
    
    if not pila: 
        print("El texto no contiene caracteres válidos.")
        return False

    while cola:  
        de_la_cola = cola.popleft() 
        
        de_la_pila = pila.pop()   
        
        if de_la_cola != de_la_pila:
            return False
            
    return True

if __name__ == "__main__":
    frases_de_prueba = [
        "Anita lava la tina",
        "A man, a plan, a canal: Panama",
        "oso",
        "racecar",
        "Hola Mundo", 
        "12321"
    ]

    for frase in frases_de_prueba:
        if es_palindromo(frase):
            print(f"  '{frase}' -> Sí es un palíndromo.")
        else:
            print(f"  '{frase}' -> No es un palíndromo.")