nome = input('Digite um nome: ')
a = len(nome) - 1 #valor da enésima posição da variável nome
b = len(nome) #valor da posição final da variável nome

def inverter(nome): #função para inverter a variável 'nome'
    return nome[::-1]

while a >= 0: 
    if a <= len(nome):
        print(' ' * a, end='') #caso o valor de 'a' for menor ou igual ao número de caracteres do nome, será preenchido por espaços
        print(nome[a:b] + inverter(nome[a:b])) #irá imprimir a variável 'nome' e a sua 'inversa'
        a -= 1

c = 0
d = 0 #contador de letras apagadas


while c <= len(nome):
    if c <= len(nome):
        print(' ' * d, end='') #a cada letra apagada se contará um espaço a partir do contador 'd'
        print(nome[c:b] + inverter(nome[c:b])) #irá imprimir a variável 'nome' e a sua 'inversa'
        c += 1
        d += 1