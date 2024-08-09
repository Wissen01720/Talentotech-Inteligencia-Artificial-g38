# Realiza un programa que pida al usuario cuantos números quiere introducir. Luego lee todos los números que se han introducido y se realiza una operación de media aritmética

print("¿Cuantos numeros desea ingresar?")
cantidad = int(input())
multiplicacion = 1
suma = 0
for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    suma += numero
    multiplicacion *= numero
print("La suma de los numeros es: ", suma)
print("La multiplicacion de los numeros es: ", multiplicacion)
print("La media de los numeros es: ", suma/cantidad)