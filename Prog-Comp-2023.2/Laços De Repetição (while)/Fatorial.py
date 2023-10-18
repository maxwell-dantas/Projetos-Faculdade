#Faça um programa que leia um número e imprima o seu fatorial.

import sys

num = int(input('Informe um número positivo: ')) #Dado de entrada
x = num - 1 #"x" será determinado pelo "num - 1"

if num < 0:
    print('Desculpe, tente informar um número positivo!')
    sys.exit
elif num == 0:
    print('O fatorial deste número é 1')
else:

    while x > 0: #Condição para poder exibir o valores do fatorial
        num = num * x
        x = x - 1
    print(f'O fatorial deste número é: {num}')