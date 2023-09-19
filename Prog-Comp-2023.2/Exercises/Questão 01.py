#Faça um programa que leia um valor inteiro e informe se ele é um número par positivo, par negativo, ímpar positivo, ímpar negativo ou se é nulo.

#Entrada de Dados:
num = int(input('Informe um número inteiro: '))
resto = num%2

#Condição:
if num>=0:
     if num==0:
          print('Este é um valor NULO!')
     elif resto==0:
          print(f'Seu número de valor {num} é um PAR POSITIVO')
     elif resto!=0:
          print(f'Seu número de valor {num} é um ÍMPAR POSITIVO')
     
else:
     if num==0:
        print('Este é um valor NULO!')
     if resto==0:
          print(f'Seu número de valor {num} é um PAR NEGATIVO')
     else:
          print(f'Seu número de valor {num} é um ÍMPAR NEGATIVO')
    