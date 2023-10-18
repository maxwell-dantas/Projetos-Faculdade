#Faça um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário.

num = int(input('Informe um número inteiro:'))

bin = 2 

resultado = 0

while bin <= num:

    if num // bin == 2:
        print('1')
    elif num // bin != 2:
        print('0')
print()