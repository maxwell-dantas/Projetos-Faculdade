#Faça um programa que leia os 3 ângulos de um triângulo e informe o seu tipo.

#Entrada de dados:
angle_1 = float(input('Informe o PRIMEIRO ângulo para o seu triângulo: '))
angle_2 = float(input('Informe o SEGUNDO ângulo para o seu triângulo: '))
angle_3 = float(input('Informe o TERCEIRO ângulo para o seu triângulo: '))
angle = angle_1 + angle_2 + angle_3

#Condição geral:
if angle_1 > 0 and angle_2 > 0 and angle_3 > 0 and angle == 180: 
    if angle_1 < 90 and angle_2 < 90 and angle_3 < 90:                  #Condição triângulo acutângulo
        print('O seu triângulo é o triângulo acutângulo')       
    elif angle_1 == 90 or angle_2 == 90 or angle_3 == 90:               #Condição triângulo retângulo
        print('O seu triângulo é o triângulo retângulo')    
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:                  #Condição triângulo obtusângulo
        print('O seu triângulo é o triângulo obtusângulo')
else:
   if angle_1 < 0 or angle_2 < 0 or angle_3 < 0:                        #Condição triângulo inválido
        print('Os ângulos devem ser positivos')
   else:
        print('A soma dos ângulos devem ser igual a 180°')