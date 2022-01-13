# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partidas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
jogador["Nome"] = input('Qual o nome do jogador(a): ')
num_partidas = int(input('Quantas partidas o(a) jogador(a) participou?  '))
gols = []
total = 0
for i in range(0, num_partidas):
    num_gols = int(input(f'Números de gols na {i+1}º partida? '))
    gols.append(num_gols)
jogador['Gols'] = gols[:]
jogador['Total'] = sum(gols)
print('=+'*20)
print(jogador)
print('=+'*20)
for k, v in jogador.items():
    print(f'O campo {k} valor {v}')
print('=+' * 20)
print(f'O jogador ou jogadora {jogador["Nome"]} jogou {num_partidas} partidas:')
p = 1
for i in jogador["Gols"]:
    print(f'Na {p}º Partida o jogador(a) {jogador["Nome"]} marcou {i} Gols')
    p += 1


