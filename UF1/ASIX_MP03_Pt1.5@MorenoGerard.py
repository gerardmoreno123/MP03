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

nota = input("Digues una puntuació entre 0 i 10: ")

if (float(nota) >10 or float(nota) < 0):
    print("Fora del rang")
elif (float(nota) >= 9):
    print("Exel·lent")
elif (float(nota) >= 8):
    print("Notable")
elif (float(nota) >= 7):
    print("Bé")
elif (float(nota) >= 5):
    print("Suficient")
elif (float(nota) < 5):
    print("Insuficient")
else:
    ("Puntiació incorrecta")

'''
Tasca 2:
Escriu un programa que demani l'any actual i un altre any qualsevol. El resultat ha de mostrar quants anys han passat des de l'any introduït o quants anys falten.
Ara milloreu el programa per a fer que quan la diferència sigui només d'un any, ens digui que només falta un any.
'''

'''
Tasca 3:
Creeu un joc de daus on es generi una tirada per a cadascun dels jugadors, quan escriguin la paraula "tirar" en un input i posteriorment es mostri el resultat de la partida.
Podeu utilitzar la funció randint() de la llibreria random:
Exemple d'ús:
import random
numero = random.randint(1, 6)
'''
