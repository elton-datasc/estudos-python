'''
l = ['elton','guilherme','de','almeida', 10.5]

l[4] = 'silva'

print(l)
print(l[1:3])
print(l[::2])
print(l[::-1]) # inverte a lista'''

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

l1.insert(0, 'laranja') # acrescenta am dada posição
l1.append('b')
l1.extend(l3)
print(l1)

del(l1[3:5]) # excluindo nas posições indicadas
print(l1)

print(max(l3))

l2 = list(range(0, 10, 2))# tranformando um objeto range numa lista
print(l2)



