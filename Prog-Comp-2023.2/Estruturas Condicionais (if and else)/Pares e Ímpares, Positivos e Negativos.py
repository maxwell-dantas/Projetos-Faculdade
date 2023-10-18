#Faça um programa que leia um valor inteiro e informe se ele é um número par positivo, par negativo, ímpar positivo, ímpar negativo ou se é nulo.

#Entrada de Dados:
num = int(input('Informe um número inteiro: '))
resto = num%2

#Condição do número NULO:
if num == 0:
     print('Este número é um valor NULO!')
else:
#Condição de números ímpares e pares positivos e negativos:
     if num > 0:                                                            #Números positivos
          if resto == 0:
               print(f'Seu número de valor {num} é um PAR POSITIVO')
          else:
               print(f'Seu número de valor {num} é um ÍMPAR POSITIVO')         
     else:                                                                 #Números negativos
          if resto == 0:
               print(f'Seu número de valor {num} é um PAR NEGATIVO')
          else:
               print(f'Seu número de valor {num} é um ÍMPAR NEGATIVO')