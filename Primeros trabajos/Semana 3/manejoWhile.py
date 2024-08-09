# Realiza un programa que pida al usuario un número entero del 0 al 9, y que mientras el número no sea correcto se repita el proceso. Luego debe comprobar si el número se encuentra en la lista de números y notificarlo.Sugerencia: La sintaxis "valor in lista" permite comprobar fácilmente si un valor se encuentra en una lista (devuelve True o False)

mumero = int(input("Ingrese un número del 0 al 9: "))
while mumero < 0 or mumero > 9:
    mumero = int(input("Ingrese un número del 0 al 9: "))
lista = [1, 3, 6, 9]
if mumero in lista:
    print("El número se encuentra en la lista")
else:
    print("El número no se encuentra en la lista")