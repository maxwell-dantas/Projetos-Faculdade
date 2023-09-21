#Faça um programa que leia os 3 lados de um triângulo e informe o seu tipo:

#Dados de entrada:
a = float(input('Digite o primeiro lado do seu triângulo: '))
b = float(input('Digite o primeiro lado do seu triângulo: '))
c = float(input('Digite o primeiro lado do seu triângulo: '))




if a>=0 and b>=0 and c>=0:
    if a > b - c and a < b + c:

        if b > a - c and b < a + c:
    
            if c > a - b and c < a + b:
                if a==b and b==c:
                    print('Triângulo equilátero!')
                elif a!=b and a!=c and b!=c:
                    print('Triângulo escaleno!')
                else:
                    print('Triângulo isósceles!')
            else:
                print('O valor da terciera medida deve ser maior que a diferença da primeira pela segunda e, também, deve ser menor que a soma desses dois lados!')
        else:
            print('O valor da segunda medida deve ser maior que a diferença da primeira pela terceira e, também, deve ser menor que a soma desses dois lados!')   
    else:
        print('O valor da primeira medida deve ser maior que a diferença da segunda pela terceira e, também, deve ser menor que a soma desses dois lados!')       