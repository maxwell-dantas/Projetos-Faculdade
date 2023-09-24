#Faça um programa que, dado um inteiro de quantos anos se passaram, mostre em que ano ocorreu o evento.

#Dados de entrada:
nascimento = int(input('Informe o ano de nascimento: '))
resultado = nascimento - 10000
tempo_percorrido = 10000 + nascimento

if nascimento < 10000:  #Condição para existir um ano a.C
     if nascimento <0:  #Condição de quem nasceu a.C*
        print(f'Nascendo no ano {nascimento*-1} a.C, caso você nascesse há 10000 anos atrás,' + 
        f' nasceria no ano {resultado*-1} a.C\ntendo como tempo percorrido: {tempo_percorrido} anos a.C')
     else:  #Condição de quem nasceu d.C
         if nascimento == 1:    #Condição para o print mostrar que passou 1 ano ao invés de 1 anos d.C
            print(f'Nascendo no ano {nascimento} d.C, caso você nascesse há 10000 anos atrás,' + 
             f' nasceria em {resultado*-1} a.C\ntendo como tempo percorrido: {resultado*-1} anos a.C e {nascimento} ano d.C')
         else: 
             print(f'Nascendo no ano {nascimento} d.C, caso você nascesse há 10000 anos atrás,' + 
             f' nasceria em {resultado*-1} a.C\ntendo como tempo percorrido: {resultado*-1} anos a.C e {nascimento} anos d.C')
else:
     print(f'Nascendo no ano {nascimento} d.C, caso você nascesse há 10000 anos atrás,' + 
     f' nasceria no ano {resultado} d.C\ntendo como tempo percorrido: {nascimento} anos d.C')
