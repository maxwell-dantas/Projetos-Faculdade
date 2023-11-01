while True:
    name = str(input('Digite um nome ou um número: ').lower())
    nameinv = name[::-1]
    
    if name == nameinv:
        print('É palíndromo')
    else:
        print('Não é palíndromo')
        break