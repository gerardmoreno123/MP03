'''
Tasca1:
Escriu un programa que sol·liciti una puntuació entre 0 i 10. Si la puntuació és fora d'aquest rang, mostra un missatge d'error. Si la puntuació està entre 0 i 10, mostra la qualificació usant la taula següent:
Puntuació Qualificació
>= 9 Excel·lent
>= 8 Notable
>= 7 Bé
>= 5 Suficient
< 5 Insuficient
Bateria de proves:
Introduïu puntuació: 9.5 -> Excel·lent
Introduïu puntuació: perfecte -> Puntuació incorrecta
Introduïu puntuació: 11 Puntuació -> Incorrecta
Introduïu puntuació: 7.5 -> Bé
Introduïu puntuació: 0.5 -> Insuficient
'''

try:
    nota = float(input("Digues una puntuació entre 0 i 10: "))
    if (nota >10 or nota < 0):
        print("Fora del rang")
    elif (nota >= 9):
        print("Exel·lent")
    elif (nota >= 8):
        print("Notable")
    elif (nota >= 7):
        print("Bé")
    elif (nota >= 5):
        print("Suficient")
    elif (nota < 5):
        print("Insuficient")
    else:
        print("Puntiació incorrecta")

except ValueError:
    print("Puntiació Incorrecta")

'''
Tasca 2:
Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.
'''


try:
    actual = int(input("Quin any es: "))
    any_qualsevol = int(input("Digues un any qualsevol: "))
    resta = actual - any_qualsevol
    if (resta>1):
        print("Han pasat", resta)
    elif (resta>=1):
        print("falta",resta,"any")
    elif (resta<1):
        print("Falten", abs(resta))
except ValueError:
    print("Error")


'''
Tasca 3:
Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
Podeu utilitzar la funció randint() de la llibreria random:
Exemple d'ús:
import random
numero = random.randint(1, 6)
'''
import random

try:
    dau1 = input("Jugador 1 tira el dau\n ")
    dau2 = input("Tugador 2 tira el dau\n ")

    if (dau1 == "tirar" or dau2 == "tirar"):
        dau1 = random.randint(1, 6)
        dau2 = random.randint(1, 6)
        print("El jugador 1 ha tet ",dau1)
        print("El jugador 2 ha tet ",dau2)
        if (dau1>dau2):
            print("Guanya el jugador 1")
        elif (dau1<dau2):
            print("Guanya el jugador 2")
        elif (dau1==dau2):
            print("Empat")      
    else:
        print("Un dels jugadors no sap tirar el dau")   

except ValueError:
    print("Error")