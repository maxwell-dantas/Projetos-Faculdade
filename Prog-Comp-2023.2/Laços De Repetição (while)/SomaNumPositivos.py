'''Faça um programa que solicite valores inteiros ao usuário e à medida que o usuário o informe o valor o programa deverá somar apenas os números positivos digitados pelo usuário. 
O programa deve permitir que o usuário digite uma quantidade não determinada de números. O programa encerra e imprime o valor da soma quando o usuário digitar o valor 0 (ZERO).'''

ordinal = 1 #Ínicio da minha enumeração de números digitados
resultado = 0 

while True:

    num = int(input(f'Informe o {ordinal}° número ou digite 0 para sair: '))
    ordinal = ordinal + 1

    if num > 0: 
        resultado = resultado + num #O valor da variável resultado irá se alterar de acordo com os números positivos somados
        
    elif num == 0:
        break

print(f'A soma dos números positivos digitados são: {resultado}')