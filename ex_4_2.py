contraseña_correcta="iloveyou123"
contraseña=input("ingresa la contraseña: ")
contador=1
while (contraseña!=contraseña_correcta and contador<=3):
    contraseña=input("ingresa la contraseña de nuevo: ")
    contador=contador + 1
if contador<=3:
     print ("Contraseña correcta")
     print ("Jelooouuuu")  
else:
        print ("Se autodestruirá en 5 segundos")

print ("Llegó al numero de intentos: ", contador)