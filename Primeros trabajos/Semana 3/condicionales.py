# Determinar la cantidad de dinero que recibira un trabajador por concepto de horas extras trabajadas en una empresa, sabiendo que cuando las horas de trabajo exceden de 40, el resto se consideran horas extras y que estas se pagan al doble de una hora normal cuando no exceden de 8; si las horas extras exceden de 8 se pagan las primeras 8 al doble de lo que se paga una hora normal y el resto al triple.

horas_trabajadas = int(input("Ingrese el numero de horas trabajadas: "))
pago_por_hora = float(input("Ingrese el pago por hora: "))
horas_extras = 0
for i in range(horas_trabajadas):
    if i > 40:
        horas_extras += 1
pago_horas_extras = 0
if horas_extras <= 8:
    pago_horas_extras = horas_extras * pago_por_hora * 2
else:
    pago_horas_extras = 8 * pago_por_hora * 2 + (horas_extras - 8) * pago_por_hora * 3
print("El pago por horas extras es: ", pago_horas_extras)


# En una fabrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compre. Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; si el número de computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de descuento; y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $3.500.000.

numero_computadoras = int(input("Ingrese el numero de computadoras: "))
precio_computadora = 3500000
total_compra = numero_computadoras * precio_computadora
descuento = 0
if numero_computadoras < 5:
    descuento = total_compra * 0.1
elif numero_computadoras < 10:
    descuento = total_compra * 0.2
else:
    descuento = total_compra * 0.4
total_compra -= descuento
print("El total de la compra es: ", total_compra)