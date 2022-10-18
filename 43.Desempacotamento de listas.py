
'''#podemos associar índices a itens da lista
lista = ['lu', 'elton', 'raye']

p1, p2, p3 = lista

print(p3)'''

#desempacotamento de listas

lista = ['lu', 'elton', 'raye','igo', 'thata']

p1, p2, *outra_lista,ultimo = lista

print(p1, p2)
print(p1, outra_lista)
print(p2, outra_lista,ultimo)
'''print(p3, outra_lista)
print(p4, outra_lista)
print(p5, outra_lista)'''