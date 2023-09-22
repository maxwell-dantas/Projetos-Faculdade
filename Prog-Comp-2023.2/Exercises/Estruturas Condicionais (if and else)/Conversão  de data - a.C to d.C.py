'''Raul Seixas cantou que nasceu há 10 mil anos e não há nada neste mundo que ele não saiba demais.  
Faça um programa que, dado um inteiro de quantos anos se passaram, mostre em que ano ocorreu o evento. 
Lembre-se que você deve indicar se aconteceu AC (Antes de Cristo) ou DC (Depois de Cristo). 
Lembre-se que o primeiro ano da era cristã é 0 (zero).'''

#Dados de entrada:
ano_atual = int(input('Informe o ano atual: '))
nascimento = int(input('Informe o ano de nascimento: '))
anos_corridos = ano_atual - nascimento
resultado = nascimento - 10000

evento = ano_atual - anos_corridos  #Evento de quantos anos se passarão depois de Cristo.

#Condição geral:
if ano_atual > nascimento:
    print(f'Nascendo em {nascimento} e tendo como ano atual {ano_atual}, caso você nascesse há 10000 anos atrás,' + 
        f' nasceria em {resultado*-1} a.C\ntendo como tempo percorrido: {resultado*-1} a.C e {evento} d.C')
else:
    print('O ano de nascimento não pode ser maior que o ano atual!')