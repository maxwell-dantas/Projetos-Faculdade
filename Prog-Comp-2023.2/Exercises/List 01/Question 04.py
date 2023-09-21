'''Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este numero.
 Isto é, se for informado 1 exibir Domingo, se for informado 2, exibir Segunda-Feira e assim por diante.'''

#Dados de entrada:
x = int(input('Informe um número inteiro entre 1 e 7: '))

#Condição geral:
if x>=1 and x<=7:
    #Condição dos dias da semana:
    if x==1:
        print('Domingo')
    elif x==2:
        print('Segunda-Feira')
    elif x==3:
        print('Terça-Feira')
    elif x==4:
        print('Quarta-Feira')
    elif x==5:
        print('Quinta-Feita')
    elif x==6:
        print('Sexta-Feira')
    elif x==7:
        print('Sábado')
else:
    print('Valor inválido.')
