#Dados dois números inteiros positivos, determinar o Máximo Divisor Comum (MDC) entre eles usando o Algoritmo de Euclides.

a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))

if a == 0:
    print(f'O valor do MDC é: {b}') #se o B for igual a 0, o maior valor que divide os dois é o próprio A

elif b == 0:
    print(f'O valor do MDC é: {a}') #se o A for igual a 0, o maior valor que divide os dois é o próprio B

elif a > b: #se o A for maior que B, o primeiro termo a ser considerado no RESTO é o A

    resto = a % b 

    while resto != 0: 
        a = b
        b = resto
        resto = a % b
    print(f'O valor do MDC é {b}')

elif b > a: #se o B for maior que A, o primeiro termo a ser considerado no RESTO é o B

    resto = b % a

    while resto != 0: 
        b = a
        a = resto
        resto = b % a
    print(f'O valor do MDC é {a}')