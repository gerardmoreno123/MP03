'''
Crea un programa que demani una cadena de 4 caràcters (numèrics) a l'usuari, (com "1234") 
els emmagatzemi a una llista convertits en enters i imprimeixi la suma dels números que la formen. Heu d'utilitzar una funció interna per a fer la suma.
https://www.w3schools.com/python/python_ref_functions.asp
Demana a l'usuari un número i afegeix-lo al final de la llista amb un mètode de llista.
Ara elimina aquest número de la llista amb un mètode de llista.
Ordena la llista amb un mètode de llista.
Mostra el seu número màxim i el seu mínim, extrets amb funcions internes.
Calcula la mitjana aritmètica de la llista a partir de les funcions internes sum() i len().
'''

#Crear una llista apartir de un input
cadena_usuari = input("Digues 4 numeros: ")
llista_usuari = [int(cadena_usuari[0]),int(cadena_usuari[1]),int(cadena_usuari[2]),int(cadena_usuari[3])]
suma = sum(llista_usuari)
print("La teva cadena de numeros es",cadena_usuari[0:],"\nLa suma de la teva cadena es: ",suma)

#Afegir un numero al final de la llista
numero_final = input("Digues 1 numero per afegir al final de la cadena: ")
llista_usuari.append(numero_final)
print("Añadiendo numero en 3,2,1:",llista_usuari)

#Eliminar el numero preguntat en l'anterior part
llista_usuari.remove(numero_final)
print("Destruyendo numero en 3,2,1:",llista_usuari)

#Ordena llista
llista_usuari.sort()
print("Ordenando numeros en 3,2,1:",llista_usuari)

#Mostra min y max numeros de la llista
print("Mostrando numero maximo en 3,2,1:",max(llista_usuari),"\nMostrando numero minimo en 3,2,1:",min(llista_usuari))

#Calcula mitjana
print("Calculando media en 3,2,1:",sum(llista_usuari)/len(llista_usuari))