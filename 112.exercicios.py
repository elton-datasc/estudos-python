def mult(*args):
    n = 1
    for i in args:
        n *= i
    return n


multiplicar = mult(3,7)
print(multiplicar)