'''Dado um número natural na base binária, transformá-lo para a base decimal. Usar OBRIGATORIAMENTElaço de repetição. 
Exemplo: Dado 10010 a saída será 18, pois 1.24 + 0.23 + 0.22 + 1.21 + 0.20 = 18.'''

bin = int(input('Informe um valor binário: '))
num = 0 #número decimal
pot = 0 #a potência começa em 0
rd = bin #resultado decimal

while bin > 0:
    resto = bin % 10
    num = num + resto * (2 ** pot)
    bin = bin // 10
    pot = pot + 1

print(f'O valor do número binário: {rd}, em decimal é: {num}')
