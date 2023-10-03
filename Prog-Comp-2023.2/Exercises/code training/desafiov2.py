x1 = int(input('Informe o valor de X1: '))
x2 = int(input('Informe o valor de X2: '))

if x1<=x2:
    while x1<=x2:
        y = 0.2*x1 - 0.4
        print(f'({x1},{y})')
        x1 += 1