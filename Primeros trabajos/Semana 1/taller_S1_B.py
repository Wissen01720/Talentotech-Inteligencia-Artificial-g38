#Calcular el área de un círculo con un radio dado. Utiliza la fórmula A = πr^2

r = 6
pi = 3.14159
A = pi * r**2
print(A)

#Convertir una temperatura en grados Celsius a Fahrenheit (F = C * 9/5 + 32)

temperatura = int(input("Introduce la temperatura en grados Celsius: "))
F = temperatura * 9/5 + 32
print(F + "°F")

#Crear una calculadora de propina. Dado el total de la cuenta y el porcentaje de propina deseado, calcular el monto de propina y el total final.

total = float(input("Introduce el total de la cuenta: "))
propina = float(input("Introduce el porcentaje de propina deseado: "))
monto_propina = total * propina / 100
total_final = total + monto_propina
print("El monto de la propina es: ", monto_propina)

#Calcular el precio final de un producto después de aplicar un descuento. Se proporcionan el precio original y el porcentaje de descuento.

precio_original = float(input("Introduce el precio original del producto: "))
descuento = float(input("Introduce el porcentaje de descuento: "))
total_descuento = precio_original * descuento / 100
print("El total de descuento es: ", total_descuento)

#Determinar la edad de una persona dados su año de nacimiento y el año actual.

anno_nacimiento = int(input("Ingrese su año de nacimiento: "))
anno_actual = int(input("Ingrese el año actual: "))
edad = anno_actual - anno_nacimiento
print("Su edad es: ", edad)

#Calcular la velocidad media de un objeto. Se dan la distancia recorrida y el tiempo empleado.

distancia = float(input("Introduce la distancia recorrida: "))
tiempo = float(input("Introduce el tiempo empleado: "))
velocidad_media = distancia / tiempo
print("La velocidad media es: ", velocidad_media)

#Crear una calculadora de índice de masa corporal (IMC). Se proporciona el peso en kilogramos y la altura en metros.

peso = float(input("Introduce tu peso en kilogramos: "))
altura = float(input("Introduce tu altura en metros: "))
IMC = peso / altura**2
print("Tu índice de masa corporal es: ", IMC)

#Calcular la suma de los primeros n números naturales, donde el valor de n se proporciona como entrada.

n = int(input("Introduce un número: "))
suma = n * (n + 1) / 2
print("La suma de los primeros números naturales es: ", suma)

#Calcular la raíz cuadrada de un número dado. Utiliza la función sqrt del módulo math

numero = float(input("Introduce un número: "))
import math
raiz = math.sqrt(numero)
print("La raíz cuadrada de ", numero, " es: ", raiz)

#Calcular el monto final después de ciertos años utilizando la fórmula del interés simple: MF = P(1 + tasaInteres * tiempo)

p = float(input("Introduce el monto principal: "))
tasaInteres = float(input("Introduce la tasa de interés: "))
tiempo = float(input("Introduce el tiempo en años: "))

MF = p * (1 + tasaInteres * tiempo)
print("El monto final después de ", tiempo, " años es: ", MF)