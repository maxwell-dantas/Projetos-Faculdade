#Faça um programa que leia um número e imprima o seu fatorial.

#Dado de entrada
num = int(input('Informe um número: '))

fat = num
x = num - 1

'''
Exemplo: num = 4
x = 4 - 1 = 3
'''

while x > 0: #Condição para poder exibir o valores do fatorial
    num = num * x
    x = x - 1
print(f'O fatorial deste número é: {num}')