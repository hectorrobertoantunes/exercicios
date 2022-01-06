# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep
win = 0
while True:
    dedos = int(input('Digite o número de dedos: '))
    choice = input('Par ou Ímpar? ').capitalize().strip()
    print('O computador está escolhendo...')
    sleep(2)
    dedos_pc = randint(0, 10)
    choice_pc = 0
    if choice == 'Par':
        choice_pc = 'Ímpar'
    else:
        choice_pc = 'Par'
    print(f'O computador escolheu {choice_pc} e colocou {dedos_pc}')
    sleep(2)
    soma = dedos + dedos_pc
    if soma % 2 == 0 and choice_pc == 'Par':
        print('O computador ganhou!')
        break
    elif soma % 2 == 0 and choice == 'Par':
        print('Você ganhou')
        win += 1
    elif soma % 2 != 0 and choice_pc == 'Ímpar':
        print('O computador ganhou!!')
        break
    else:
        print('Você ganhou!')
        win += 1

print(f'Você ganhou {win} vezes do computado!')



