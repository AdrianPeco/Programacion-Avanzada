def main():
   l1 = float(input("Introduzca la medida:"))
   if(l1==1 or l1<=2):
       print ("\n Pequeño")
   elif(l1==3 or l1<=4):
       print ("\n Mediano")
   elif (l1==5 or l1<=6):
       print ("\n Grande")
   elif (l1==6.5 or l1<=8.5):
       print ("\n Muy grande")

if __name__ == '__main__':
   main()