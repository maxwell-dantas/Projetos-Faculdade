#Faça um programa que leia um par de coordenadas e mostre os valores de Y para cada valor de X.

import sys #Importanto biblioteca SYS 

x1 = int(input('Informe o valor de X1: '))
x2 = int(input('Informe o valor de X2: '))


if x1>x2:
    print('Informe X1<=X2')
    sys.exit()

while x1<=x2:
    y = 0.2*x1 - 0.4
    print(f'({x1},{y:.2f})')
    x1 += 1
