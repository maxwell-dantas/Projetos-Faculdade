#Exercício para descobrir os valores das raízes de uma equação de segundo grau, quando houver

#Dados de entrada:
a = float(input('Insira o valor de A: '))
b = float(input('Insira o valor de B: '))
c = float(input('Insira o valor de C: '))

#Condição geral:
if a != 0:

    #Fórmulas:
    delta = b**2 - (4*a*c)
    x1 = (-b + ((delta**(1/2))))/2*a
    x2 = (-b - ((delta**(1/2))))/2*a

    #Condições:
    if delta <0:
        print('Como o delta foi menor que zero, a sua equação não possui raízes reais!')
    elif delta == 0: 
        print(f'Com delta sendo {delta}, o valor da sua raiz é: {x1==x2:.2f}!')
    else:   
        print(f'Com delta sendo {delta}, os valores das suas raízes são: {x1:.2f} e {x2:.2f}!\ne a sua forma fatorada será: (X - {x1:.0f}) * (X - {x2:.0f})')
else:
    print('O valor de A deve ser diferente de zero')

