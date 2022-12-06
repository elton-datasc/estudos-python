'''def mult(*args):
    n = 1
    for i in args:
        n *= i
    return n


multiplicar = mult(3,7)
print(multiplicar)'''

def par():
    num = int(input('digite um número: '))
    print(f'O número {num} é par') if num % 2 ==0 else print(f'O número {num} é impar')

    
par()


