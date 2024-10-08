# Define una función que calcule la raiz cubica de un numero dado

def raiz_cubica(numero):
    return numero**(1/3)

print(raiz_cubica(38))

# Llama la función max con la lista 15,82,13,55 como argumento, y luego la min con la palabara amarillo como argumento

print(max([15,82,13,55]))
print(min("amarillo"))

# Si queremos obligar a que random siempre nos de los mismos resultados, podemos usar seed. Arma una semilla de 25 y ejecuta el código 2 veces, checa como se repita (seed necesita repetirse 2 veces tmb)

import random
random.seed(25)
print(random.random())
random.seed(25)
print(random.random())

# Usa un bucle for, randrange y una expresión condicional para simular 20 tiros de moneda, mosrando A para águila y S para Sello

for i in range(20):
    if random.randrange(2) == 0:
        print("A", end=" ")
    else:
        print("S", end=" ")

# Funciones sin parámetros y múltiples parámetros def raizcuadra (numero): """Esta función saca la raiz cuadra de un número""" return numero ** (1/2)Se acuerdan de la primer funcion que hicimos? Que pasa si la corremos sin parametro?

def raizcuadra(numero):
    return numero**(1/2)

print(raizcuadra())

# Ahora, que pasa si le damos más de un parámetro?

def raizcuadra(numero1, numero2):
    return numero1**(1/2), numero2**(1/2)

print(raizcuadra(25, 36))

# Arma una función que reciba una cantidad arbitraria de argumentos y calcule el producto de multiplicarlos todos entre ellos

def productos(*argumentos):
    producto = 1
    for i in argumentos:
        producto *= i
    return producto

print(productos(2, 3, 4, 5))