'''n = input('digite um número: ')
try:
    if n.isdigit():
        n = int(n)
        if n % 2 == 0:
            print(f'{n} é um número par.')
        else:
            print(f'{n} é um número ímpar.')
    else:
        print(f'{n} não é número inteiro.')
except:
    print('erro.favor reiniciar o programa.')'''

nome = input('digite seu nome: ')

if len(nome) <= 4:
    print('seu nome é curto')
elif len(nome) <=6:
    print('seu nome é normal')
else:
    print('seu nome é muito grande')
