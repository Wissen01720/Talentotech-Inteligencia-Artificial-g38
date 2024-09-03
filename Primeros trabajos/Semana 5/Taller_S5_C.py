## Define una función que calcule la raiz cubica de un numero dado

numero = float(input())
def raiz_cubica(numero):
    return numero ** (1/3)
print(raiz_cubica(numero))

## Llama la función max con la lista 15,82,13,55 como argumento, yluego la min con la palabara amarillo como argumento

print(max([15, 82, 13, 55]))
print(min("amarillo"))

## Si queremos obligar a que random siempre nos de los mismos resultados, podemos usar seed. Arma una semilla de 25 y ejecuta el código 2 veces, checa como se repita (seed necesita repetirse 2 veces tmb)

import random as r 
r.seed(25)
print(r.random())
r.seed(25)
print(r.random())

## Usa un bucle for, randrange y una expresión condicional para simular 20 tiros de moneda, mosrando A para águila y S para Sello

for i in range(20):
    if r.randrange(2) == 0:
        print("A", end=" ")
    else:
        print("S", end=" ")
print()

## def raizcuadra(numero): """Esta función saca la raiz cuadra de un número""" return numero ** (1/2)Se acuerdan de la primer funcion que hicimos? Que pasa si la corremos sin parametro?

def raizcuadra(numero):
    return numero ** (1/2)
print(raizcuadra(25))
print(raizcuadra())

# Lo que sucede es que la función arroja un error de tipo TypeError, ya que se espera que se proporcione un argumento al llamar a la función, pero no se proporciona ninguno. Para evitar este error, se puede modificar la función para que tenga un valor predeterminado para el parámetro, de modo que si no se proporciona ningún argumento, se utilice el valor predeterminado.

## Arma una función que reciba una cantidad arbitraria de argumentos y calcule el producto de multiplicarlos todos entre ellos

def producto(*args):
    resultado = 1
    for arg in args:
        resultado *= arg
    return resultado
print(producto(2, 3, 4))
print(producto(5, 6, 7, 8))