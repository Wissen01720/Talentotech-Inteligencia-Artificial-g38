def identificar_tipo(valor):
    print(f"Valor ingresado: {valor}")
    print(f"Tipo de dato: {type(valor).__name__}")
    print()

# Lista de valores a verificar
valores = [
    "Hola Mundo",
    [1, 10, 100],
    -25,
    1.167,
    ["Hola", "Mundo"],
    ' ',
    True,
    {"Uno": "uno", "Dos": "dos"}
]

# Iterar sobre cada valor y mostrar su tipo
for valor in valores:
    identificar_tipo(valor)