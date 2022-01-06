# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

import random
import time

print('\033[33mO computador está escolhendo um número....\033[33m')
time.sleep(3)
num_pc = random.randint(0, 10)
print('\033[33mO computador terminou a escolha, agora...\033[33m')
time.sleep(1)
num_h = 'd'
cont = 0
while num_h != num_pc:
    num_h = int(input('Qual número o computador escolheu? '))
    if num_h < num_pc:
        print('Mais...')
    elif num_h > num_pc:
        print('Menos...')
    cont += 1
print('Parabens, você acerto, o número que o computador tinha escolhido era o {} !'.format(num_pc))
print('Você usou  x {} tentativas!'.format(cont))

