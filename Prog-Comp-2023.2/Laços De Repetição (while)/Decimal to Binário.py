#Faça um programa que solicite ao usuário um valor inteiro positivo e gere o seu valor em binário.

num = int(input('Informe um valor inteiro positivo: '))
bin = '' 
y = num 

if num == 0:
    print(f'O valor binário de 0 é 0')
else:
    while num >= 1:
        r = num % 2
        bin = str(r) + bin 
        num = num // 2
    print(f'O valor binário de {y} é {bin}')