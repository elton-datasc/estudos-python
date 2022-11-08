# soma = lambda x, x2: x + x2
#
# print(soma(3, 9))
#
# #exemplo de uso prático
# precos = [100, 50, 70, 30]
#
# impostos = list(map(lambda x: x * 0.3, precos))
#
# print(impostos)

m = lambda n1, n2: n1 * n2


def n(n1, n2):
    return n1 * n2


def o(n1, n2):
    mult = n1 * n2
    return mult


print(m(9, 3))
print(n(9, 3))
print(o(9, 3))