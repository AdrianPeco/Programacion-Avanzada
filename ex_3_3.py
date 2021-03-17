#Edad de un perro en años humanos
def calcular_edad_perro(edad_persona):
    if edad_persona <= 2:
        return edad_persona*10.5 
    else:
        return 21 + (edad_persona - 2)*4
edad_persona = int(input('Inserte la edad de la persona:'))
if edad_persona > 0:
    total = calcular_edad_perro(edad_persona)
    print(f'La edad del perro en años humano seria:{total}')