#Faça um programa que solicite ao usuário um valor inteiro positivo e informe a quantidade de dígitos.

num = int(input('Informe um valor inteiro positivo: '))

dig = 0 #Contador de dígitos

if num < 0:
    print('Digite um número inteiro positivo!')

elif num == 0:
    print('O número de dígitos é: 1')

else:
    while num > 0: #Condição para o programa continuar executando o laço
        resto = num % 10 #Irá pegar o resto da divisão
        num = num // 10 #Irá dividir o número por 10, variando, assim, o número
        dig = dig + 1
    print(f'O número de dígitos é: {dig}')