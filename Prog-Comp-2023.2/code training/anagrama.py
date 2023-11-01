name = input('Informe a primeira palavra: ').lower()
name2 = input('Informe a segunda palavra: ').lower()

if len(name) == len(name2): #se a quantidade de caracteres forem iguais, pode prosseguir
    for i in name: #'i' está pegando todas as letras em comum da variável 'name' com a variavel 'name2'
        a = name2.count(i) #variável para armazenar o valor de 'i'
    for l in name2: #'l' está pegando todas as letras em comum da variável 'name' com a variavel 'name2'
        b = name.count(l) #variável para armazenar o valor de 'l'
        if name2.count(i) == name.count(l): #se a quant. de letras da var. 'a' for igual a quant. de letras da var. 'b', é um anagrama
            print('É um anagrama!')
else:
    print('Não é um anagrama!') 