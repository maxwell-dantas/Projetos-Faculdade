#Faça um programa que determine um vencedor entre dois jogadores sobre pedra, papel e tesoura.

#Dados de entrada:
player_1 = str(input('Pedra, Papel ou Tesoura? ').lower())
player_2 = str(input('Pedra, Papel ou Tesoura? ').lower())

if player_1==player_2:      #Condição de Empate
    print('Empate')
else:
    if player_1=='pedra' and player_2=='tesoura':           #Condição de jogadas com Pedra
        print('Pedra quebra tesoura, o jogador 1 venceu!')
    elif player_1=='pedra' and player_2=='papel':
        print('Papel embrulha pedra, o jogador 2 venceu!')

    if player_1=='papel' and player_2=='pedra':             #Condição de jogadas com Papel
        print('Papel embrulha pedra, o jogador 1 venceu!')
    elif player_1=='papel' and player_2=='tesoura':
        print('Tesoura corta papel, o jogador 2 venceu!')
        
    if player_1=='tesoura' and player_2=='papel':           #Condição de jogadas com Tesoura
        print('Tesoura corta papel, o jogador 1 venceu!')
    elif player_1=='tesoura' and player_2=='pedra':
        print('Pedra quebra tesoura, o jogador 2 venceu!')

