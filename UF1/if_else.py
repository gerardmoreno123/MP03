'''
x=int(input("Escriu un numero:"))

if (x>0):
    print(x,"Es positiu")
elif (x<0):
    print(x,"Es negatiu")
else:
    print(x,"Es igual")

num=36
candidat= int(input("Escull un numero entre 0 i 100:"))

if (candidat>100 or candidat<0):
    print("Fora del rang")
elif  (candidat<num):
    print("Tas quedat curt")
elif (candidat>num):
    print(" Tas pasat")
else:
    print("Correcte")
'''

print("1:Mitjana aritmètica \n 2:Massa Corporal \n 3:Fahrenheid \n 4:Segons")
menu= int(input("Tria 1 d'aquestes opcions: "))

if menu==1:
    numero1 = float(input("Donam un numero:"))
    numero2 = 5
    mitjana = (numero1 + numero2)/2
    print("El primer numero es",numero1,"i el segon numero es",numero2,"la mitjana aritmètica sira",mitjana)
elif menu==2:
    pes = float(input("Quin es el teu pes(kg)? "))
    altura = float(input("Quina es la teva altura(metros)? "))
    massacorporal = (pes/altura**2)
    print (massacorporal)
elif menu==3:
    temp = float(input("Introdueix una temperatura en Celsius:"))
    fahrenheid = ((temp * 9/5)+32)
    print("La teva temperatura en Fahrenheid es:",fahrenheid)
elif menu==4:
    hora = int(input("Digues la hora:"))
    minut = int(input("Digues los minuts:"))
    segons = ((hora*3600)+(minut*60))
    print("El teu temps en segons es",segons)
else:
    print("Opcio incorrecta")

