#elementos iteráveis
#indices
# num de 0 a 9

frase = "uma coisa é uma coisa e um negoço é um negoço"
tamanho_frase = len(frase)

contador = 0

nova_string = ''

'''while contador < tamanho_frase:
    nova_string += frase[contador]
    contador += 1
print(nova_string)'''

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == 'o':
        nova_string += 'O'
    else:
        nova_string += letra
    contador += 1

print(nova_string)

