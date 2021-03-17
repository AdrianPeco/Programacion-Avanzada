numero_elegido = input("Escribe un número: ")
numero = float(numero_elegido)
if numero == 0:
    print("Cero")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")