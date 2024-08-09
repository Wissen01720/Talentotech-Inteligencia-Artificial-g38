#Creemos una variable w que valga 39. Python reconoce a la variable w como un entero.
int = w = 39

#Calcula la suma de 10.8, 12.2 y 0.2, guardala en una variable llamada b, y muestra la variable

b = 10.8 + 12.2 + 0.2
print(b)

#Aritmetica Multiplicación Realiza un 7 * 4

print(7 * 4)

# División Verdadera. 
# Divide 8/5

print(8/5)

# División de piso. 
# Divide 20//6 - verás como te da un rsultado entero

print(20//6)

#Restante. 
#Ahora obten el restante de dividir 26 / 8 usando el operador %

print(26 % 8)

#Agrupación con parentesis
#Revisa que python respeta la jerarquia de operaciones

print(4 * 5 - (7 + 3))

# Por tu cuenta
# Evalua la expresión 3*(4-5) con y sin parentesis. Son los paréntesis redundantes?

print(3*(4-5))
print(3*4-5)

# La función Print
# ejecuta el siguiente snippet print(“Hoy aprenderé a usar la función print”)

print(“Hoy aprenderé a usar la función print”)
      
# Print(“Hoy aprenderé a usar la función print”)

print("Hoy aprenderé a usar la función print")
      
#Por ejemplo, para declarar el arreglo Hoy aprenderé a usar la función ‘print’

print("Hoy aprenderé a usar la función "print"") #Error de sintaxis

# Esto se resuelve utilizando dobles comillas

print("Hoy aprenderé a usar la función print") #Correcto

# Otras opciones para insertar texto el prompt de Anaconda son print(‘Hoy aprenderé’,’a usar’, ‘la función print’) print(‘Hoy aprenderé\n a usar\n la función print’)

print("Hoy aprenderé","a usar", "la función print")

print("Hoy aprenderé\n a usar\n la función print")
      
print(‘También aprenderé a dividir \

…: líneas de texto cuando las expresiones \

…: sean demasiado largas’)
    #Los errores presentes en los prints anteriores son de sintaxis, ya que no se están utilizando las comillas correctas para imprimir texto.
    #Si se quiere resolver esto se puede definir una funcion con el texto y postoeriormente llamarla con print.

print("""También aprenderé a dividir \

…: líneas de texto cuando las expresiones \

…: sean demasiado largas""") # tambien podemos hacer uso de las triples comillas para imprimir texto largo

#Cuando requieras utilizar comillas dobles y sencillas en algún enunciado, por ejemplo

#Aprender ‘Python’, es realmente “sencillo” Es posible hacerlo utilizando triples comillas

print("Aprender ‘Python’, es realmente “sencillo”")

#Con Python, puedes asignar a una variable un arreglo de caracteres arreglo1=‘Hoy aprenderé a usar la función print’

arreglo1= "Hoy aprenderé a usar la función print" 
print(arreglo1)

print(arreglo1[4:15])

print(len(arreglo1))

#Con estas herramientas, ya puedes mostrar los resultados de los cálculos en una forma más amigable Arma un programa que divida 2 variables y devuelva "w elevado a la z da por resultado y"

w = 5
z = 16
y = w / z

print(f"{w}, elebado a la {z} da por resultado {y:.2f}")

#Input que solicita al usuario la información específica que debe ingresar al programa nombre=input(‘¿Cuál es tu nombre?’)

nombre = input("¿Cuál es tu nombre?")
barrio = input("¿Cuántos años tienes?")
ciudad = input("Ciudad de residencia")
print(f"Me llamo {nombre}, tengo {edad} años y vivo en {ciudad}")

#Por default, Python guarda las entradas que recibe del comando input como un arreglo. Revise el type en cuestión

print(type(nombre))
print(type(barrio))
print(type(ciudad))

#Arma un programa que te pida 2 números y los sume

numero1 = int(input("Ingresa un número"))
numero2 = int(input("Ingresa otro número"))
suma = numero1 + numero2
print(f"La suma de los números es {suma}")

#Usa float() para convertir "6.2" (una cadena) a un valor flotante

numero = float("6.2")
print(type(numero))

#Ejecuta el siguiente script. Se pude ejecutar desde Consola de forma Local en el PC

print('Ingresa tu edad y la de tu mejor amigo, para decirte la relación qué hay entre ellas ')
#Lee la primera edad
edad1=int(input('Ingresa tu edad: '))
edad2=int(input('Ingresa la edad de tu mejor amigo: '))


if edad1==edad2:
    print(edad1,'es igual',edad2,'\n Tu amigo y tú, tienen la misma edad.')
if edad1 !=edad2:
    print(edad1,' es diferente de',edad2,'\n Tu amigo y tú tienen edades diferentes.')
if edad1 < edad2:
    print(edad1,' es menor que',edad2,'\n Tu amigo es mayor que tú.')
if edad1 > edad2:
    print(edad1,' es mayor que',edad2,'\n Tu amigo es menor que tú.')
if edad1 <= edad2:
    print(edad1,' es menor o igual a',edad2,'\n Tu amigo tiene al menos, tu edad.')
if edad1 > edad2:
    print(edad1,' es mayor que',edad2,'\n Tu amigo tiene a lo más, tu edad.')

#Solución de la actividad anterior
edad1 = int(input("Ingresa tu edad: "))
edad2 = int(input("Ingresa la edad de tu mejor amigo: "))

if edad1 == edad2:
    print(f"{edad1} es igual a {edad2}. Tu amigo y tú tienen la misma edad.")
if edad1 != edad2:
    print(f"{edad1} es diferente de {edad2}. Tu amigo y tú tienen edades diferentes.")
if edad1 < edad2:
    print(f"{edad1} es menor que {edad2}. Tu amigo es mayor que tú.")
if edad1 > edad2:
    print(f"{edad1} es mayor que {edad2}. Tu amigo es menor que tú.")
if edad1 <= edad2:
    print(f"{edad1} es menor o igual a {edad2}. Tu amigo tiene al menos, tu edad.")
if edad1 >= edad2:
    print(f"{edad1} es mayor o igual a {edad2}. Tu amigo tiene a lo más, tu edad.")