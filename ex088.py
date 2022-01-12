# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep

print('-'*30)
print(f'{"MEGA SENA"}')
print('-'*30)
vetor = []
jogos = int(input('Quantos jogos você quer fazer: '))
for j in range(0, jogos):
    while len(vetor) < 6:
        sorteado = randint(1, 60)
        if sorteado not in vetor:
            vetor.append(sorteado)
    vetor.sort()
    sleep(1)
    print(f'Jogo {j+1}: {vetor}')
    vetor.clear()






