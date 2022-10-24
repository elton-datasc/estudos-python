# gerar uma lista com 20 números aleatórios entre 1 e 10
import random
random.randint(1, 10)

'''numeros = []
for _ in range(20):
    numeros_aleatorios = random.randint(1, 10)
    numeros.append(numeros_aleatorios)
print(numeros)'''

#o mesmo que o código de cima, com compreensão de lista
n= ([random.randint(1, 10) for _ in range(20)])
print(n)

#trazendo só os pares
print([i for i in n if i % 2 == 0])

#exemplo 2
print([i for i in range(21) if i % 2 == 0])

for i in range(20):
    print(i)

v = [i for i in range(20) if i % 2 == 0]
print(v)

[print(i) for i in range(10)]