# funções lambda: funções anônimas
def soma(n1, n2):
    return n1 + n2

print(soma(4, 5))

#o mesmo efeito da função de cima
soma_lambda = lambda num1, num2: num1 + num2
print(soma_lambda(5, 4))

lista = [10, 20, 30, 40, 50]
filter()