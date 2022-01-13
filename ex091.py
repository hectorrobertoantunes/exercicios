from random import randint
from operator import itemgetter
from time import sleep
jogadores = {}
ranking = {}
for x in range(0, 4):
    jogadores[f'Jogador {x+1}'] = randint(1, 6)
for j, v in jogadores.items():
    print(f'O jogador {j} tirou o valor {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('== RANKING ==')
for i in range(0, 4):
    print(f'Em {i+1}º Lugar {ranking[i][0]}, tirou {ranking[i][1]}')
