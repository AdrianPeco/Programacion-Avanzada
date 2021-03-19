a=int (input("ingresa el primer valor"))
b=int (input("ingresa el segundo valor"))
while(a>b):
    print("El segundo valor es menor, vuelve a intentarlo")
    b=int(input("ingresa el segundo valor"))
print("Los numeros son diferentes")
def main():
    print("Cada vez más grande")
    primero = int(input("Escribe un numero"))
    segundo = int(input("Escribe un valor más grande que {primero}"))
    while segundo > primero:
     primero = segundo
     segundo = int(input(f"Escribe un numero mayor que {primero}: "))
    print ()
    print(f"{segundo}no es mayor que {primero}")
    