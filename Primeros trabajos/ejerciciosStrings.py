# EJERCICIO NUMERO 1
texto_principal = input("Introduce un texto: ")
sub_texto = input("Introduce un subtexto: ")
print(texto_principal.startswith(sub_texto))

# EJERCICIO NUMERO 2
cadena = input("Introduce una cadena de texto: ")
caracter = input("Introduce un caracter: ")
if len(caracter) != 1:
    print("Error: debe ingresar un solo caracter.")
else:
    print(f"El caracter '{caracter}' aparece {cadena.count(caracter)} veces en la cadena de texto.")

# EJERCICIO NUMERO 3
frase = input("Introduce una frase: ")
palabras = frase.split()
print(f"La frase tiene {len(palabras)} palabras.")

# EJERCICIO NUMERO 4

cadena = input("Introduce una cadena de texto: ")
caracter1 = input("Introduce un primer caracter: ")
caracter2 = input("Introduce un segundo caracter: ")
if len(caracter1) != 1 or len(caracter2) != 1:
    print("Error: debe ingresar un solo caracter.")
else:
    cadena_nueva = cadena.replace(caracter1, caracter2)
    print(f"La cadena de texto modificada es: {cadena_nueva}")


# EJERCICIO MANEJO DE STRINGS

import re

def pal_palindroma(frase):
    frase_limpia = re.sub(r'[^a-zA-Z]', '', frase).lower()
    return frase_limpia == frase_limpia[::-1]

frase = input("Introduce una frase: ")

for frase in frase:
    if pal_palindroma(frase):
        print(f"La frase '{frase}' es palíndroma.")
    else:
        print(f"La frase '{frase}' no es palíndroma.")