'''
x=int(input("Escriu un numero:"))

if (x>0):
    print(x,"Es positiu")
elif (x<0):
    print(x,"Es negatiu")
else:
    print(x,"Es igual")
'''
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
