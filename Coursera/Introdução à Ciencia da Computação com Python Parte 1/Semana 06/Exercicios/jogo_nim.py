
def computador_escolhe_jogada(n, m):
    cont = m - 1
    while cont >= 1:
        if (n - cont) % (m + 1) == 0:
            jogada = cont
            break
        cont -= 1
    else:
        jogada = m
    return jogada


def usuario_escolhe_jogada(n, m):
    valida = False
    while not valida:
        jogada = int(input('Quantas peças você vai tirar? '))
        if jogada > m or jogada > n or jogada <= 0:
            print('\033[31mJogada inválida!\033[m')
        else:
            valida = True
    return jogada


def partida():
   
    numero_peças = int(input('Quantas peças? '))
    limite_peças = int(input('Limite de peças por jogada? '))
    
    computador_joga = False
    msg_singular = ['resta', 'apenas', 'uma', 'peça']
    msg_plural = ['restam', 'peças']


    if numero_peças % (limite_peças + 1) == 0:
        print('Você começa!')
    else:
        print('Computador começa!')
        computador_joga = True

    while numero_peças > 0:
        if computador_joga:
            jogada = computador_escolhe_jogada(numero_peças, limite_peças)
            computador_joga = False
            if jogada > 1:
                print('Computador retirou {} {}.'.format(jogada, msg_plural[-1]))
            else:
                print('Computador retirou {} {}.'.format(jogada, msg_singular[-1]))
        else:
            jogada = usuario_escolhe_jogada(numero_peças, limite_peças)
            computador_joga = True
            if jogada > 1:
                print('Você retirou {} {}.'.format(jogada, msg_plural[-1]))
            else:
                print('Você retirou {} {}.'.format(msg_singular[-2], msg_singular[-1]))


        numero_peças -= jogada
        if numero_peças > 0:
            if numero_peças > 1:
                print('Agora {} {} {} no tabuleiro.\n'.format(msg_plural[0], numero_peças, msg_plural[1]))
            else:
                print('Agora {} {} {} {} no tabuleiro.\n'.format(msg_singular[0], msg_singular[1], msg_singular[2], msg_singular[3]))


    if computador_joga:
        print('\nFim do jogo! Você ganhou!\n')
        return True
    else:
        print('\nFim do jogo! O computador ganhou!\n')
        return False

 
def campeonato():
    partidas = 3
    rodada = 0
    jogador = 0
    computador = 0

    while rodada < partidas:
        rodada += 1
        print('\n**** Rodada {} ****\n'.format(rodada))
        vencedor = partida()
        if vencedor:
            jogador += 1
        else:
            computador += 1

    print('**** Final do campeonato! ****\n')
    print('Placar: Você  {} x {}  Computador\n'.format(jogador, computador))


def main():    
    menu = "JOGO DO NIM:\n\
1 - Partida Isolada\n\
2 - Campeonato\n\
3 - Sair\n\
#>_\b"
    play = True
    while play:
        escolha = input(menu)
        if escolha == '1':
            print('Partida Isolada!\n')
            partida()
        elif escolha == '2':
            print('Campeonato!\n')
            campeonato()
        elif escolha == '3':
            play = False
        else:
            print("Opção inválida...\n")
#end main

main()