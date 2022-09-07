a = int(2)
b = int(2)
c = int(3)

print(a == b and b < c)

a = int(2)
b = int(2)
c = int(3)

print(a == b or b < c)

a = int(2)
b = int(2)
c = int(3)

print(not a == b or not b < c)

"""
nome = input('Qual seu nome?')
idade = int(input('Qual sua idade?'))

idade_menor = 18
idade_maior = 30

if idade >= idade_menor and idade <= idade_maior:
  print(f'{nome} pode pegar o empréstimo.')
else:
  print(f'{nome} NÃO pode pegar o empréstimo.')
"""

a = 2
b = 3

if not b > a:
  print('b é maior do que a')
else:
  print('a é maior do que b')

a = ''
b = 0

if not a:
  print('Preencha o valor de a')

nome = 'elton'
if 'l' in nome:
  print(f'existe l em seu nome')