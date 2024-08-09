ingreso = input("")
if ingreso.isdigit():
    ingreso = int(ingreso)
    ascii_valor = chr(ingreso)
    print(ascii_valor)
else:
    ascii_valores = ' '.join(str(ord(c)) for c in ingreso)
    print(ascii_valores)