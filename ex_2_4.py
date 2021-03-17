#Segundos a dias, horas, minutos y segundos
print('Un minuto tiene',60,'segundos')
print('Una hora tiene',60*60,'segundos')
print('Un día tiene',60*60*24,'segundos')
print('_'*28+'\n')
while True:
  x =int(input('Número de segundos: ') or 5000000)
  if x>5000000:
    print("Introduzca un valor hasta dos millones.")
  else:
    break
d=x//86400
resto1=x%86400
h=resto1//3600
resto2=resto1%3600
m=resto2//60
s=resto2%60
print( '%d días, %d horas, %d minutos, %d segundos' % \
  (d, h, m, s))