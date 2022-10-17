'''str = 'O Brasil é o país do futuro. Eu quero ver o Brasil pra cima! Vai Brasil !'
str2 = 'Eu quero é ver o oco!'

lista = str.split(' ')
lista2 = str.split('.')

print(lista)
print(lista2)'''

'''palavra = ''
contagem = 0
for valor in lista:
    qtd_vezes = lista.count(valor)
    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor'''

#print(f'A palavra que mais aparece é {palavra}, ( {contagem}  x vezes ).')

cs = 'vamo simbora que o mundo arrodeou '
cs1 = 'e se eu ficar aqui parado eu não vou.'

f = cs + cs1
#f = f.split(" ")
#print(' '.join(f))
print(f)

for indice, valor in enumerate(f):
    print(indice, valor)

