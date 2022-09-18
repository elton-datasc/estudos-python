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

#formatação de texto

'''nome = 'renato russo'

print(f'{nome:#^20}')'''

nome = 'renato russo'

print(f'{nome:@>13}')


#_____________________________________________________________________

#estudos
n = 400
print(f'{n:0>5}')

n1 = 3.58958959958959
print(f'{n1:.2f}')



