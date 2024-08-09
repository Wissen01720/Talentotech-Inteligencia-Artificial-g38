# Dado un número entero positivo, mostrar su factorial. El factorial de un numero se obtiene multiplicando todos los numeros enteros positivos que hay entre el 1 y ese numero.

numero = int(input("Ingrese un numero: "))
factorial = 1
for i in range(1, numero + 1):
    factorial *= i
print("El factorial de ", numero, " es: ", factorial)

# Solicitar al usuario que ingrese una frase y luego mostrar la cantidad de vocales que tiene la frase.

frase = input("Ingrese una frase: ")
vocales = 0
for letra in frase:
    if letra in "aeiouAEIOU":
        vocales += 1
print("La cantidad de vocales en la frase es: ", vocales)

# Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada. En cada iteración, solicitar al usuario que ingrese un numero. Al finalizar, mostra la suma de todos los numeros ingresados.

cantidad = int(input("Ingrese la cantidad de numeros a sumar: "))
suma = 0
for i in range(cantidad):
    numero = int(input("Ingrese un numero: "))
    suma += numero
print("La suma de los numeros ingresados es: ", suma)

