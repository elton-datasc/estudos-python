'''while condição verdadeira:
    faça isso'''

'''x = 0
while x < 5:
    print(x)
    x += 1
print('acabou')'''

'''x = 0
while x < 10:
    if x == 3:
        x += 1
        continue
    print(x)
    x += 1
print('Acabou')'''

'''x = 0
while x < 10:
    if x == 3:
        x += 1
        break
    print(x)
    x += 1
print('Acabou')'''

contador = 1
acumulador = 1

'''while contador <= 5:
    print(contador, acumulador)
    acumulador = acumulador + contador
    contador += 1
else:
    print('cheguei no else')
print('continua...')'''

#aula 35 ELSE NO WHILE

while contador <= 10:
    print(contador)

    if contador > 5:
        break
    contador += 1
else:
    print('cheguei no else')
print('fora do while')



