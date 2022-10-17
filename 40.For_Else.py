panelinha = ['elton', 'luciana', 'rayane']

'''for nome in panelinha:
    if nome.lower().startswith('l'):
        print('é luuuuuuu')
    elif nome.lower().startswith('r'):
        print('é rayeeeee')'''

for nome in panelinha:
    if nome.lower().startswith('r'):
        break
    print(nome)
else:
    print('não existe uma palavra que comece com a letra j')

