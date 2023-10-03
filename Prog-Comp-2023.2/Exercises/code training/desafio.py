#Faça um programa que leia um par de coordenadas e mostre os valores de Y para cada valor de X.

x1 = int(input('Informe o valor de X1: '))
x2 = int(input('Informe o valor de X2: '))

y1 = 0.2 * x1 - 0.4 #Função
y2 = 0.2 * x2 - 0.4 #Função

if x1 <= x2:
    while y1 <= y2:
        print(f'X1 sendo {x1:.2f} e se deslocando até X2 (tendo como valor {x2:.2f}), o Y será {y1:.2f}')
        y1 += 0.2
        x1 += 1
