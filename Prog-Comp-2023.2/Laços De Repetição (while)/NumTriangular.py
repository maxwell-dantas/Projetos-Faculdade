#Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) triangular, de acordo com a definição.
num = int(input('Informe um número inteiro positivo: ')) 
t1 = 0 
x = 1

if num >=0:

    while num != t1:
        t1 = t1 + x
        x = x + 1

        if num < t1:
            print(f'O número {num} não é triangular')
            break

    if num == t1:
        print(f'O número {num} é triangular')

else:
    print('Desculpe, tente informar um número inteiro positivo!')