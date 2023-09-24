#Calculadora de ano bissexto

ano = int(input('Informe o ano: '))

resto = ano%4

if ano>=0:
    if resto==0:
        print('É bissexto')
    else:
        print('Não é bissexto')