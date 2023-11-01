#Find the largest palindrome made from the product of two -digit numbers.

max = 0 #valor do maior número até o momento

for a in range(100,1000): #'a' pertence a um conjunto de 100 a 999
    for b in range(100,1000): #'b' pertecente a um conjunto de 100 a 999
        resultado = a * b #a variável 'resultado' será executada até o conjunto se multiplicar por completo (999 * 999)
        constante = resultado #a variável 'constante' serve para armazenar os valores do resultado

        x = 0 #'x' será responsável por transformar o número em seu inverso. Ex.: 105 = 501

        while resultado > 0:
            resto = resultado % 10 #o 'resto' pegará o resto da divisão
            x = x * 10 + resto #o valor de 'x' é multiplicado por 10 para avançar uma casa decimal e, por fim, adicionado a variavel 'resto'
            resultado = resultado // 10 #o valor do 'resultado' sofrerá uma divisão inteira por 10 para variar o seu número

        if x == constante: #se o valor de 'x' for igual ao da 'constante', teremos um palíndromo
            if x > max:
                max = x #se x for maior que o valor max, o max será o x
                amax = a #se a for maior que amax, o amax será o a
                bmax = b #se a for ma ior que amax, o amax será o b

print(f'O maior palíndromo do produto de dois termos com três algarismos é: {amax} * {bmax} = {max}')