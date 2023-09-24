#Faça um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este numero.

#Dados de entrada:
x = int(input('Informe um número inteiro entre 1 e 12: '))

#Condição geral:
if x>=1 and x<=12:
    #Condição dos dias da semana:
    if x==1:
        print('Janeiro')
    elif x==2:
        print('Fevereiro')
    elif x==3:
        print('Março')
    elif x==4:
        print('Abril')
    elif x==5:
        print('Maio')
    elif x==6:
        print('Junho')
    elif x==7:
        print('Julho')
    elif x==8:
        print('Agosto')
    elif x==9:
        print('Setembro')
    elif x==10:
        print('Outubro')
    elif x==11:
        print('Novembro')
    elif x==12:
        print('Dezembro')
else:
    print('Digite um valor válido.')