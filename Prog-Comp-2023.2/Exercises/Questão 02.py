#Faça um programa que leia a coordenada cartesiana (coordenada X e Y) de dois pontos e calcule a distância entre eles.

#Entrada de dados:
ponto_Ax = float(input('Informe o valor de X na primeira coordenada: '))
ponto_Ay = float(input('Informe o valor de Y na primeira coordenada: '))
ponto_Bx = float(input('Informe o valor de X na segunda coordenada: '))
ponto_By = float(input('Informe o valor de Y na segunda coordenada: '))

#fórmulas:
delta_X = ponto_Ax - ponto_Bx
delta_Y = ponto_Ay - ponto_By
dist = (delta_X**2 + delta_Y**2)**(1/2)

print(f'A distância entre esses dois pontos é: {dist:.2f}')