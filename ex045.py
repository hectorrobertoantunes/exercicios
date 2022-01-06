#  Crie um programa que faça o computador jogar Jokenpô com você.

import random
import time
for x in range(1,4):

    jogador = input('Escolha entre pedra, papel ou tesoura: ')
    jogador = jogador.capitalize()
    lista = ['Pedra', 'Papel', 'Tesoura']
    print('\033[1:93m=+'*25)
    print('Computador está escolhendo...')
    print('=+'*25)
    print('\033[0:0m')
    time.sleep(3)
    print('O computador escolheu!')
    print('Jo...')
    time.sleep(2)
    print('Ken..')
    time.sleep(2)
    print('Pô!!!!!')
    time.sleep(2)
    computador = random.choice(lista)
    print('Computador escolheu {}'.format(computador))

    if jogador == 'Pedra' and computador == 'Papel':
        print('O computador ganhou')
    elif jogador == 'Papel' and computador == 'Pedra':
        print('O jogador ganhou')
    elif jogador == 'Tesoura' and computador == 'Pedra':
        print('O computador ganhou')
    elif jogador == 'Pedra' and computador == 'Tesoura':
        print('O jogador ganhou')
    elif jogador == 'Tesoura' and computador == 'Papel':
        print('O jogador ganhou')
    elif jogador == computador:
        print('Empate')
    else:
        print('O computador ganhou')
