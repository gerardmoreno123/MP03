
'''
Realitza els següents programes i lliura el codi font:

Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. 
Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.
'''

numinput = input("Escriu 4 numeros separats amb un espai: ")
print(int(numinput[0])+int(numinput[2])+int(numinput[4])+int(numinput[6]))

'''
Consulta els mètodes "built-in" que teniu disponibles per a cadenes i crea un programa que a partir d'una frase donada per l'usuari calculi:
Número de caràcters.
Número de paraules.
Frase  amb totes les paraules en majúscula.
Frase  amb totes les paraules en minúscula.
Preguntat un caràcter a l'usuari retorni la posició de la primera coincidència trobada a la frase.
Preguntat un caràcter a l'usuari retorni la posició de la darrera coincidència trobada a la frase.
Preguntat un caràcter a l'usuari retorni el número de coincidències trobades a la frase.
Mostri el número de vocals del text (has d'optimitzar al màxim aquest codi!!).
Modifica el primer programa per a que abans de donar el resultat mostri si és cert que la cadena només conté números.
'''

#Sense preguntar a l'usuari --> userinput = str('Hola que tal. Tinc 54 Anys')
#Pregunta la frase al usuari
userinput = input('Escriu una frase: ')

#Calcul numero de caracters
caracters = len(userinput)
print("Caracters: ",caracters)

#Calcul numero de paraules
paraules = len(userinput.split())
print("Paraules: ",paraules)

#Posar la frase en majuscula
majuscula = (userinput.upper())
print("Tot en majuscules: ",majuscula)

#Posar  la frase en miniscula
miniscula =(userinput.lower())
print("Tot en minuscules: ",miniscula)

#Buscar el primer caracter de la frase
caracter_inicial = input("Digues un caracter: ")
print("El primer caracter es troba en la posicio: ",userinput.find(caracter_inicial))

#Buscar el ultim caracter de la frase
caracter_final = input("Digues un caracter: ")
print("El ultim caracter es troba en la posicio: ",userinput.rfind(caracter_final))

#Calcular el total de caracters de la frase
coincidencia = input("Digues un caracter: ")
print("El total de coincidencies es: ",userinput.count(coincidencia))

#Posar la frase en miniscula i contar el total de vocals
vocal_minuscula = (userinput.lower())
#vocals_total = (vocal_minuscula.count('a')+vocal_minuscula.count('e')+vocal_minuscula.count('i')+vocal_minuscula.count('o')+vocal_minuscula.count('u'))
print("Les vocals totals son: ",vocal_minuscula.count('a')+vocal_minuscula.count('e')+vocal_minuscula.count('i')+vocal_minuscula.count('o')+vocal_minuscula.count('u'))

#Mostrar si el input introduit es numeric
numinput = input("Escriu 4 numeros seguits: ")
print(numinput.isnumeric())
