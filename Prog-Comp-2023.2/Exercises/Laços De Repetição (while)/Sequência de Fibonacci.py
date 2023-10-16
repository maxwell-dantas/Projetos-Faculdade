#Faça um programa que leia um valor N onde esse valor será os N primeiros números da sequência de Fibonacci

import sys

nt = int(input('Informe a quantidade de termos que você quer mostrar: ')) #Dado de entrada
t1 = 0 #Primeiro termo da sequência
t2 = 1 #Segundo termo da sequência
seq = 2 #A sequência irá começar a partir do segundo termo

if nt <= 0: #se o número for menor ou igual a zero não irá acontecer nada
    sys.exit()

print(f'{t2} ‣ ', end ='') #O end serve para dar continuadade na linha de exibição

while seq <= nt:
    t3 = t2 + t1
    t1 = t2 
    t2 = t3 
    seq = seq + 1
    print(f'{t3} ‣ ', end ='',)
print('Fim.')