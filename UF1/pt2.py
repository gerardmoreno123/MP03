
'''
Realitza els següents programes i lliura el codi font:

Crea un programa que a partir d'una cadena de 4 caràcters (numèrics) preguntada a l'usuari, (com "123456") imprimeixi la suma dels números que la formen. 
Teniu en compte que només s'ha d'utilitzar un input, estem treballant les cadenes.
'''
#numinput = input("Escriu 4 numeros: ")
#print(int(numinput[0])+int(numinput[2])+int(numinput[4])+int(numinput[6]))

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

#userinput = input('Escriu una frase: ')
userinput = str('Hola que tal. Tinc 54 anys')
caracters = len(userinput)
paraules = len(userinput.split())
majuscula = (userinput.upper())
miniscula =(userinput.lower())
pos_inicial = (userinput)
pos_final = (userinput)
coincidencia = (userinput)
vocals_total = (userinput.count('a')+userinput.count('e')+userinput.count('i')+userinput.count('o')+userinput.count('u'))

numinput = input("Escriu 4 numeros: ")
print(int(numinput[0])+int(numinput[2])+int(numinput[4])+int(numinput[6]))
if numinput : 
    print("tot mal")