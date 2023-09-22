#Faça um programa que leia os 3 lados de um triângulo e informe o seu tipo:

#Dados de entrada:
a = float(input('Digite o primeiro lado do seu triângulo: '))
b = float(input('Digite o primeiro lado do seu triângulo: '))
c = float(input('Digite o primeiro lado do seu triângulo: '))

#Condição para a formação de um triângulo:
if a>0 and b>0 and c>0:
    if a > b - c and a < b + c:                     #Condição do tamanho do lado A
        if b > a - c and b < a + c:                 #Condição do tamanho do lado B
            if c > a - b and c < a + b:             #Condição do tamanho do lado C
                if a==b and b==c:                   #Condição do triângulo equilátero
                    print('Triângulo equilátero!')
                elif a!=b and a!=c and b!=c:        #Condição do triângulo escaleno
                    print('Triângulo escaleno!')
                else:                               #Se não for equilátero ou escaleno, é isósceles
                    print('Triângulo isósceles!')
            else:
                print('O valor da terciera medida deve ser maior que a diferença da primeira pela segunda e, também, deve ser menor que a soma desses dois lados!')
        else:
            print('O valor da segunda medida deve ser maior que a diferença da primeira pela terceira e, também, deve ser menor que a soma desses dois lados!')   
    else:
        print('O valor da primeira medida deve ser maior que a diferença da segunda pela terceira e, também, deve ser menor que a soma desses dois lados!')
else:
    print('O valor do primeiro, do segundo e do terceiro lado devem possuir valores maiores que 0!')    