# Realizar un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:Mostrar una suma de los dos números, Mostrar una resta de los dos números (el primero menos el segundo), Mostrar una multiplicación de los dos números, En caso de no introducir una opción válida, el programa informará que la opción no es correcta.

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
print("¿Qué desea hacer?")
print("1. Sumar los numeros")
print("2. Restar los numeros")
print("3. Multiplicar los numeros")
opcion = int(input("Ingrese la opcion: "))

if opcion == 1:
    print("La suma de los numeros es: ", numero1 + numero2)
elif opcion == 2:
    print("La resta de los numeros es: ", numero1 - numero2)
elif opcion == 3:
    print("La multiplicacion de los numeros es: ", numero1 * numero2)
else:
    print("Opcion no valida")