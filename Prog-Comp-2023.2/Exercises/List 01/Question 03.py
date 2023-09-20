#Faça um programa que determine um vencedor entre dois jogadores sobre pedra, papel e tesoura.

#Dados de entrada:
player_1 = str(input('Pedra, Papel ou Tesoura? '))
player_2 = str(input('Pedra, Papel ou Tesoura? '))

#Condição:
if player_1==player_2:
    print('Empate')
else:
    if player_1=='Pedra' and player_2=='Tesoura':
        print('O jogador 1 venceu')
    elif player_1=='Pedra' and player_2=='Papel':
        print('O jogador 2 venceu')

    if player_1=='Papel' and player_2=='Pedra':
        print('O jogador 1 venceu')
    elif player_1=='Papel' and player_2=='Tesoura':
        print('O jogador 2 venceu')
        
    if player_1=='Tesoura' and player_2=='Papel':
        print('O jogador 1 venceu')
    elif player_1=='Tesoura' and player_2=='Pedra':
        print('O jogador 2 venceu')
