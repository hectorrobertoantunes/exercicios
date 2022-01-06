'''Jogo de advinhação -> Escreva um programa que faça o computador "Pensar" em um número
inteiro entre 0 - 5 e peça para o usuário tentar advinhar qual número foi escolhido pelo
computador. O programa deve escrever na tela se o jogador acertou ou errour.
'''

import random
from time import sleep


for i in range(0,5):
    print('Escolhendo um número...')
    sleep(5) # uma pausa de cinco segundos
    num_pc = random.randint(0,5)
    print('Pronto!')
    print(num_pc)
    num_play = int(input('Qual o número que o computador pensou? '))

    if num_play == num_pc:
        print('Parabéns, você acertou')
    else:
        print('Infelizmente, você errou!')
