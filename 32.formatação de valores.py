#formatação de valores com modificadores (format e f-strings)
#:f para números de ponto flutuante (float)
'''n1 = 10
n2 = 3
d = n1 / n2
print(f'{d:.2f}')''' #formatação (.) para float (f)com duas casas decimais(2)

#para textos :s

'''nome = 'iron maiden'
print(f'{nome:s}')''' #indica que trata-se de uma string

# definindo uma quantidade de caracteres com preenchimentos de zeros

# > - esquerda
# < - direita
# ^ - centro
'''d = 1
print(f'{d:0>4}')''' # 4 casas á esquerda preenchendo com zeros

#combinando as formatações
'''n = 1150
print(f'{n:0>10.2f}')'''

#_____________________________________________________________________

#estudos
n2 = 7.90099222

print(f'{n2:.2f}')



