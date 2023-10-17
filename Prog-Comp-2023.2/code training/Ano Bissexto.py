#Calculadora de ano bissexto

ano = int(input('Informe o ano: '))

if ano>=0 and ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
    print('É bissexto')
else:
    print('Não é bissexto')