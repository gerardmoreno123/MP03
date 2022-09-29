#Crea un programa que a partir de dos números et calculi la mitjana aritmètica

numero1 = float(input("Donam un numero:"))
numero2 = 5
mitjana = (numero1 + numero2)/2
print("El primer numero es",numero1,"i el segon numero es",numero2,"la mitjana aritmètica sira",mitjana)

#Crea un programa que a partir d'un pes i una altura et calculi l'índex de massa corporal. MassaCorporal = peso (kg)/ [estatura (m)]2.

pes = float(input("Quin es el teu pes(kg)? "))
altura = float(input("Quina es la teva altura(metros)? "))
massacorporal = (pes/altura**2)
print (massacorporal)

#Crea un programa que a partir d'una temperatura en Celsius et calculi la temperatura en Fahrenheid.

temp = float(input("Introdueix una temperatura en Celsius:"))
fahrenheid = ((temp * 9/5)+32)
print("La teva temperatura en Fahrenheid es:",fahrenheid)

#Crea un programa que a partir d'una hora i uns minuts els calculi en segons.

hora = int(input("Digues la hora:"))
minut = int(input("Digues los minuts:"))
segons = ((hora*3600)+(minut*60))
print("El teu temps en segons es",segons)
