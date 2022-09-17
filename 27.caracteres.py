'''usuario = input('digite um usuário: ')
qtde = len(usuario)

print(usuario,qtde,type(qtde))

if qtde >= 6:
    print('usuário com mais de 6 caracteres')
else:
    print('usuário com menos de 6 caracteres')


st1 = input('digite um texto aqui: ')
st2 = input('digite outro texto aqui: ')

print(f'A qtde de caracteres foi {len(st1)+len(st2)}')'''


num1 = input('digite um número: ')
num2 = input('digite outro número: ')

if num1.isdecimal() and num2.isdecimal():
    num1 = float(num1)
    num2 = float(num2)
    s = num1 + num2
    print(s)
else:
    print('só é possível efetuar contas com números')
