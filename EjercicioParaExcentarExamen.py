import string
ALFABETO = string.ascii_uppercase # Alfabeto en mayúsculas

def rotar_alfabeto(alfabeto: str, pasos: int) -> str:
	""" Rota el alfabeto una cierta cantidad de pasos (como un rotor)."""
	pasos = pasos % len(alfabeto)
	return alfabeto[pasos:] + alfabeto[:pasos]


def rotor(c, pasos):
	""" Aplica un rotor a un caracter. """
	if c not in ALFABETO:
		return c
	idx = ALFABETO.index(c)
	alfabeto_rotado = rotar_alfabeto(ALFABETO, pasos)
	return alfabeto_rotado[idx]


def rotor_inverso(c, pasos):
	""" Aplica el rotor en sentido inverso (para descifrar)."""
	if c not in ALFABETO:
		return c
	alfabeto_rotado = rotar_alfabeto(ALFABETO, pasos)
	idx = alfabeto_rotado.index(c)
	return ALFABETO[idx]

def enigma_cifrar(texto: str, pasos: list) -> str:
	""" Cifra un texto usando una versión simplificada de Enigma con 3 rotores. """
	resultado = ""
	contador = 0
    
	for c in texto.upper():
		if c not in ALFABETO:
			resultado += c
			continue
		# Los rotores cambian de posición en cada paso
		r1 = (pasos[0] + contador) % 26
		r2 = (pasos[1] + contador // 26) % 26
		r3 = (pasos[2] + contador // (26*26)) % 26
		# Aqui Pasa por los tres rotores
		c1 = rotor(c, r1)
		c2 = rotor(c1, r2)
		c3 = rotor(c2, r3)
        
		resultado += c3
		contador += 1
    
	return resultado


def enigma_descifrar(texto: str, pasos: list) -> str:
	""" Descifra un texto cifrado con la misma configuración de Enigma. """
	resultado = ""
	contador = 0
    
	for c in texto.upper():
		if c not in ALFABETO:
			resultado += c
			continue
        
		# Los rotores avanzan igual que al cifrar
		r1 = (pasos[0] + contador) % 26
		r2 = (pasos[1] + contador // 26) % 26
		r3 = (pasos[2] + contador // (26*26)) % 26
		# En orden nverso de los rotores
		c1 = rotor_inverso(c, r3)
		c2 = rotor_inverso(c1, r2)
		c3 = rotor_inverso(c2, r1)
        
		resultado += c3
		contador += 1
    
	return resultado

def main():
	mensaje = "Basquebol"
	pasos_iniciales = [3, 1, 7]  # posiciones iniciales
    
	cifrado = enigma_cifrar(mensaje, pasos_iniciales)
	descifrado = enigma_descifrar(cifrado, pasos_iniciales)
    
	print("=== MÁQUINA ENIGMA===")
	print("Mensaje original: ", mensaje)
	print("Mensaje cifrado:  ", cifrado)
	print("Mensaje descifrado:", descifrado)

if __name__ == "__main__":
    main()
