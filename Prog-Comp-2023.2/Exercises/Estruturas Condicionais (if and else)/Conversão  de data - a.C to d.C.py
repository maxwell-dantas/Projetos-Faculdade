'''Raul Seixas cantou que nasceu há 10 mil anos e não há nada neste mundo que ele não saiba demais.  
Faça um programa que, dado um inteiro de quantos anos se passaram, mostre em que ano ocorreu o evento. 
Lembre-se que você deve indicar se aconteceu AC (Antes de Cristo) ou DC (Depois de Cristo). 
Lembre-se que o primeiro ano da era cristã é 0 (zero).'''

ano_atual = int(input('Informe o ano atual: '))
anos_corridos_1 = ano_atual - 1976
nascimento = 1976 - 10000

evento_1 = ano_atual - nascimento


if evento_1>=0:
    print(f'Raul Seixas nasceu em {nascimento*-1} a.C e se passaram {evento_1} anos desde então.')
    print(f'Sendo {nascimento*-1} anos a.C e {ano_atual} anos d.C desde então.')
else:
    print(f'Raul Seixas nasceu em {nascimento*-1} a.C e se passaram {evento_1} d.C desde então')