# Cambia la fecha de nacimiento al 2002 del primer codigo

anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
edad = 2002 - anio_nacimiento

if edad >= 25:
    print("Posible cliente")
else:
    print("No es posible cliente")

# Usa for para calcular el consumo promedio de los siguientes clientes [130,85,210,45,153,78.5,264.5,94] Esta lista te muestra el consumo de cada cliente

clientes = [130,85,210,45,153,78.5,264.5,94]
consumo_total = 0
for consumo in clientes:
    consumo_total += consumo
consumo_promedio = consumo_total / len(clientes)
print("El consumo promedio es: ", consumo_promedio)

# Usa for para calcular el interes compuesto de una persona que invierte $10,000 en una cuenta que rinde el 8% de intereses. Supon que la persona reinvierte los intereses. Calcula la cantida del dinero al final de 10 años

inversion = 10000
interes = 0.08
anos = 10

for i in range(anos):
    inversion += inversion * interes
print("El dinero al final de 10 años es: ", inversion)

# En una tienda de autoservicio hay un promotor en la sección de productos lácteos. La empresa para la que trabaja, le otorga un premio económico si rebasa $200 de ventas (venta meta) por cliente. La empresa cuenta con un registro en donde están marcadas las ventas de 8 clientes que adquirieron algunos de los productos de la marca. Por cada cliente que rebasó la cantidad meta se escribe 1, y si no la rebasa se escribe 2. Si número de clientes que rebasan la venta meta es más de la mitad, se le otorga el premio al promotor. Se requiere de un programa que señale si al promotor se le debe asignar el premio económico.

ventas = [1,2,1,1,2,1,1,1]
clientes_que_rebasaron = 0
for venta in ventas:
    if venta == 1:
        clientes_que_rebasaron += 1
if clientes_que_rebasaron > len(ventas) / 2:
    print("Se le otorga el premio al promotor")
else:
    print("No se le otorga el premio al promotor")