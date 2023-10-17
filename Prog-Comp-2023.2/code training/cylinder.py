#Exercício para calcular a área do cilindro;
#Considere PI igual a 3.1416

#Dados de entrada:
raio = float(input('Informe o valor do raio da circuferência em cm: '))
altura = float(input('Informe o valor da altura do cilindro em cm: '))

if raio >0:

    #Fórmulas:
    aBase = 3.1416 * raio**2
    aLateral = 2 * 3.1416 * raio * altura
    aTotal = 2*aBase + aLateral

    print(f'Possuindo uma base de raio com {raio}cm² e altura de {altura}cm², você terá uma área de total de {aTotal:.2f}cm²')
else:
    print('Informe um raio maior que 0')