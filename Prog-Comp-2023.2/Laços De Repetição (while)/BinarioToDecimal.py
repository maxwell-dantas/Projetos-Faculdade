'''Dado um número natural na base binária, transformá-lo para a base decimal. Usar OBRIGATORIAMENTElaço de repetição. 
Exemplo: Dado 10010 a saída será 18, pois 1.24 + 0.23 + 0.22 + 1.21 + 0.20 = 18.'''

bin = str(input('Informe um número binário: '))
validação = True
num = 0 #número decimal
pot = 0 #a potência começa em 0
rb = bin #resultado bin

for digitos in bin:

    if digitos != '0' and digitos != '1':

        validação = False
        break

if validação:

    bin = int(bin)
    while bin > 0:

        resto = bin % 10
        num = num + resto * (2 ** pot)
        bin = bin // 10
        pot = pot + 1

    print(f'O valor do número binário: {rb}, em decimal é: {num}')

else:
    print('Este valor não corresponde a um número binário!')
