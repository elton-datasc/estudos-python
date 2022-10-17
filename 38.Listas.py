'''
l = ['elton','guilherme','de','almeida', 10.5]

l[4] = 'silva'

print(l)
print(l[1:3])
print(l[::2])
print(l[::-1])
#inverte a lista
'''

'''l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2

l1.insert(0, 'laranja')
#acrescenta am dada posição
l1.append('b')
l1.extend(l3)
print(l1)

del(l1[3:5])
#excluindo nas posições indicadas
print(l1)'''

#print(max(l3))

'_________________________________________________________________________'

'''l2 = list(range(0, 10, 2))
#tranformando um objeto range numa lista
print(l2)'''

segredo = 'panelinha'
acerto = []
chances = 3

while True:
    if chances <= 0:
        print('Já Elvis! Tente novamente!')
        break
    letra = input('Digite uma letra: ')
    if letra.isalpha():
        pass
    else:
        print('Só pode ser letra, abestado!')
        continue
    if len(letra) > 1:
        print('Não vale! Digite uma letra por vez!')
        continue
    if letra in segredo and len(letra) == 1:
        print('A palavra secreta tem esta letra!')
        acerto.append(letra)
        secreto_temp = ''
        for letra_secreta in segredo:
            if letra_secreta in acerto:
                secreto_temp += letra_secreta
            else:
                secreto_temp += '*'
        if secreto_temp == segredo:
            print(f'Acertô mizarávi! A palavra secreta é: {segredo} ! Parabéns !!')
            break
        else:
            print(f'A palavra secreta tá assim: {secreto_temp}')

    else:
        print('A palavra secreta não tem esta letra!')
        if letra not in segredo:
            chances -= 1
            print(f'Vc tem {chances} chance(s)')








