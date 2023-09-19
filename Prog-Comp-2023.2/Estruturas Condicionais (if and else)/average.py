'''Calcule a média semestral do IFRN
1. Se a média for menor que 20, o aluno estará REPROVADO;
2. Se a média for maior que 20 e menor que 60, o aluno estará de RECUPERAÇÃO;
3. Se a média for maior ou igual a 60, o aluno estará APROVADO'''

#Dados de entrada:
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
peso1 = int(input('Digite o peso da sua nota 1:')) 
peso2 = int(input('Digite o peso da sua nota 2: ')) 

#Condição geral:
if n1>=0 and n1<=100 and n2>=0 and n2<=100 and peso1 >0 and peso2>0:

    #Fórmula:
    media = (n1*peso1 + n2*peso2)/(peso1 + peso2)

    print(f'A sua média neste semestre é {media:.2f}')

    #Condições:
    if media <20:
        print('Você está REPROVADO!')
    elif media >=20 and media <60:
        print('Você está em PROVA FINAL!')
    elif media >=60:
        print('Parabéns, você está APROVADO!')
else:
    print('Os pesos devem ser maiores que 0 e as notas devem estar entre 0 e 100')
