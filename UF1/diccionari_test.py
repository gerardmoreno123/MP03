'''
diccionari = {}
print("type",type(diccionari))
diccionari['one'] ='un'
diccionari['two'] = 'dos'
diccionari['three'] = 'tres'
print(diccionari)
print(diccionari['one'])
print(diccionari['two'])
print(diccionari['three'])
eng2cat={'one': 'un', 'two': 'dos', 'three': 'tres'}
print(eng2cat)
'''

diccionari = {'pepe':[45,75,15],'maria':[78,45,89],'juan':[45,89,35]}
diccionari = {'pepe':[45,75,15],'maria':[78,45,89],'juan':[45,89,35]}
print(diccionari['pepe'][1:],diccionari['maria'],diccionari['juan'])
print('pepe' in diccionari)
print(75 in diccionari['pepe'])
print(list(diccionari.values()))

diccionari['pepe'].append(87)
print('valor final',diccionari['pepe'])
