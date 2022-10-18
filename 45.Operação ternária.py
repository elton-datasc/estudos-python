# Operador Ternário

#idade = 15
msg = 'acesso liberado'
msgn = 'acesso não liberado'

'''if idade >= 18:
    print('Acesso liberado')
else:
    print('Pode não.')

print(msg) if idade >= 18 else print(msgn)'''

#exemplo de uso

idade = input('Digite sua idade: ')

if not idade.isnumeric():
    print('Idade não pode ser texto.Digite novamente')
else:
    idade = int(idade)
    print(msg) if idade >= 18 else print(msgn)



#faça if condição else faça
