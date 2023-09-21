#Faça um programa que leia dois valores inteiros (A e B) correspondentes aos catetos de um triângulo e calcule a hipotenusa.

#Dados de entrada:
a = float(input('Informe um número positivo para o cateto adjacente: '))
b = float(input('Informe um número positivo para o cateto oposto: '))

hip = (a**2 + b**2)**(1/2)

if a>=0 and b>=0:
    print(f'O valor da sua hipotenusa é {hip:.2f}')
else:
    print('Informe um número positivo para ambos os catetos!')