##¿Que pasa si llamamos un indice fuera de la lista?

#Si se llega a llamr un índice fuera de la lista, se generará un error de tipo IndexError. Por ejemplo, si se intenta acceder a un índice mayor o igual a la longitud de la lista, se generará un error de este tipo. Ejemplo:

# Lista de tareas
tareas = [6, 'Distribución', 2, 'Diseño', 1, 'Concepción', 7, 'Mantenimiento', 4, 'Producción', 3, 'Planificación', 5, 'Pruebas']

# Intentar acceder a un índice mayor o igual a la longitud de la lista
try:
    print(tareas[14])
except IndexError as e:
    print(f"Error: {e}")

# En este caso, se intenta acceder al índice 14 de la lista 'tareas', que está fuera de los límites de la lista, lo cual genera un error de tipo IndexError. El mensaje de error indica que el índice está fuera de rango.

## Arma un programa que eleve al cuadrado todos los elementos de una lista. Prueba con una lista con todos los numeros pares del 2 al 20.

lista = [2, 4, 6 , 8, 10, 12, 14, 16, 18, 20]
elevados = [x ** 2 for x in lista]
print(elevados)
# Salida esperada: [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

## Crea una tupla de un solo elemento con el número 582.4 y luego muestrala

tupla = (582.4)
print(tupla)

## Muestra que pasa si intentas concatenar una lista de 3 enteros con una tupla de 3 enteros usando +

milista = [1, 2, 3]
mitupla = (4, 5, 6)
resultado = milista + list(mitupla)
print(resultado)

# Al concatenar una lista de 3 enteros con una tupla de 3 enteros usando el operador +, se crea una nueva lista que contiene los elementos de ambas estructuras de datos. En este caso, la lista 'milista' y la tupla 'mitupla' se combinan en una nueva lista que contiene los elementos de ambas estructuras.

## Crea una lista llamada números que contenga los valores del 1 al 15, haz las siguientes operaciones -selecciona los numeros enteros -reemplaza los elementos en indices 5 al 9 por 0s -manten solo los primeros 5 elementos, y muestra la lista resultante -Borra todos los elementos que quedan

numeros = list(range(1, 16))
print("Selecciona los numeros enteros: ")
print([x for x in numeros if isinstance(x, int)])

numeros[5:10] = [0, 0, 0, 0, 0]
print("Reemplaza los elementos en indices 5 al 9 por 0s: ")
print(numeros)

numeros = numeros[:5]
print("Manten solo los primeros 5 elementos: ")
print(numeros)

numeros.clear()
print("Borra todos los elementos que quedan: ")
print(numeros)

# Crea una lista con los numeros del 1 al 15. borra una parte que contenga los primeros 4 elementos, muestra tu resultado. Empezando con el primer elemento, borra cada 2do elemento de la lista

numeros = list(range(1, 16))
numeros = numeros[4:]
print("Borra una parte que contenga los primeros 4 elementos: ")
print(numeros)

numeros = numeros[::2]
print("Borra cada segundo elemento de la lista: ")
print(numeros)

## Arma una comprensión de lista que te devuelva tuplas de todos los numeros del 1 al 6 y sus cubos

tuplas = [(x, x ** 3) for x in range(1, 7)]
print(tuplas)

## Arma una comprensión de lista que te devuelva todos los mutliples de 3 menores a 60

multiplos_de_tres = [x for x in range(1, 60) if x % 3 == 0]
print(multiplos_de_tres)

## Crea una expresion generadora que eleve al cubo los enteros pares en uan lista que contiene 10,3,7,1,9,4

lista = [10,3,7,1,9,4]
generador = (x**3 for x in lista if x % 2 == 0)
print(list(generador))

## Crea una lista con numeros del 1 al 15 y luego crea una nueva lista de los elementos impares crea una nueva lista usando map y lambda para elevar al cuadrado a todos filtra los elementos impares y luego mapealos a sus cuadrados

numeros = list(range(1, 16))
impares = list(filter(lambda x: x % 2 != 0, numeros))
cuadrados_impares = list(map(lambda x: x ** 2, impares))
print(cuadrados_impares)