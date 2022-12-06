'''def mult(*args):
    n = 1
    for i in args:
        n *= i
    return n


multiplicar = mult(3,7)
print(multiplicar)'''

def par():
    num = int(input('digite um número: '))
    if num % 2 ==0:
        print(f'O número {num} é par')
    else:
        print(f'O número {num} é impar')


par()


