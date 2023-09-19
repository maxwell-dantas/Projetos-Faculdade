#Exercício para calcular a área do cone;
#Considere PI igual a 3.1416

#Dados de entrada:
raio = float(input('Informe o raio do seu cone em cm: '))
altura = float(input('Informe a altura do seu cone em cm: '))

if raio >0:

    #Fórmulas:
    geratriz = (raio**2 + altura**2)**(1/2)
    aBase = 3.1416 * raio**2
    aLateral = 3.1416 * raio * geratriz
    aTotal = aLateral + aBase

    print(f'A área do seu cone é {aTotal:.2f}cm²')
else:
    print('Informe um raio maior que 0')