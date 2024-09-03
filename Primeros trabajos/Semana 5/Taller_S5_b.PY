## Para el siguiente diccionario, crea listas de sus llaves, valores y items - y muestra esas listas

Municipios_poblacion = {"Acatic" : 23175, "Acatlan de Juarez" : 25250, "Ameca" : 60386, "Arandas" : 80609}

llaves = list(Municipios_poblacion.keys())
print("Llaves: ")
print(llaves)

## Usa una comprensión de diccionario para crear un diccionario de los números 4-10 mapeado a sus cuadrados

cuadrados = {x: x ** 2 for x in range(4, 11)}
print("Cuadrados: ")
print(cuadrados)

## Asigna la siguiente caden a una variable texto y luego dividela usando el método split y crea un set de los resultados. Muestra las palabrás únicas en orden sorted. 'Un dragon tragon trago carbon y quedo panzon, ah que dragon tan tragon"

texto = "Un dragon tragon trago carbon y quedo panzon, ah que dragon tan tragon"
palabras = set(texto.split())
palabras_unicas = sorted(palabras)
print("Palabras únicas: ")
print(palabras_unicas)