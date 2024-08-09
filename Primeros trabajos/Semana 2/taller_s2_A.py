# CADENAS

# Dale formato a 3.141592 a 3 decimales como cadena usando f'

pi = 3.141592
pi_cadena = f'{pi:.3f}'
print(pi_cadena)

# Usa el tipo c para mostrar los caracteres que pertenecen a 58,45,41

caracteres = [58, 45, 41]
caracteres_cadena = ''.join(chr(c) for c in caracteres)
print(caracteres_cadena)

# Muestra el nombre "Daniel" en 3 filas diferentes alineados a la derecha, centro e izquierda en un campo de 10 caracteres. Encierra cada fila de resultado en brackets

nombre = 'Daniel'
nombre_derecha = f'{nombre:>10}'
nombre_centro = f'{nombre:^10}'
nombre_izquierda = f'{nombre:<10}'
print(f'[{nombre_derecha}]')
print(f'[{nombre_centro}]')
print(f'[{nombre_izquierda}]')

# Imprime los valores 11483.528 y -4581.4413 cada uno precedido por su signo, en campos de 10 caracteres con separadores de miles, y su punto decimal alineado a 2 puntos de precisión.

valor1 = 11483.528
valor2 = -4581.4413
valor1_cadena = f'{valor1:+10,.2f}'
valor2_cadena = f'{valor2:+10,.2f}'

print(valor1_cadena)
print(valor2_cadena)

# Usa los métodos en esta sección para limpiar la siguiente oración name = " Clark Kent "

nombre = " Clark Kent "
nombre_limpio = nombre.strip()
print(nombre_limpio)

# Crea un bucle for que ubica y muestra cada palabra que comienza con "d" en "Por desenredar el enredo aque ayer enrede, hoy enredo el desenredo que desenredé ayer"

frase = "Por desenredar el enredo aque ayer enrede, hoy enredo el desenredo que desenredé ayer"
palabras = frase.split()
for palabra in palabras:
    if palabra.lower().startswith('d'):
        print(palabra)

#Suponte que tienes la cadena "14 + 8" Usa una expresión regular para romper la cadena en 3 grupos representando los 2 operandos y el operador, luego muestra los grupos

import re

cadena = "14 + 8"

patron = r'(\d+)\s*([+\-*/])\s*(\d+)'

resultado = re.match(patron, cadena)

if resultado:
    operando1 = resultado.group(1)
    operador = resultado.group(2)
    operando2 = resultado.group(3)

    print(f'Operando 1: {operando1}')
    print(f'Operador: {operador}')
    print(f'Operando 2: {operando2}')

else:
    print('No se encontró una coincidencia')