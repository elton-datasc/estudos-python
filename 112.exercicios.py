'''def mult(*args):
    n = 1
    for i in args:
        n *= i
    return n


multiplicar = mult(3,7)
print(multiplicar)'''

# retornando par ou impar
def par():
    num = int(input('digite um número: '))
    print(f'O número {num} é par') if num % 2 ==0 else print(f'O número {num} é impar')


par()

#outra forma de retornar par ou impar
def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é impar'

print(par_impar(45))
print(par_impar(56))
print(par_impar(12))
print(par_impar(11))


