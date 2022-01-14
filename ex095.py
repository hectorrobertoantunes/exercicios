jogador = {}
gols = []
jogadores = []
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Coloque o nome do jogador(a): ').capitalize().strip()
    jogador['número-de-partidas'] = int(input('Coloque o número de partidas: ').strip())
    for j in range(0, jogador['número-de-partidas']):
        gol = int(input(f'Coloque o número de gols da {j+1}º Partida: '))
        gols.append(gol)
        jogador['Gols'] = gols[:]
        jogador['Total'] = sum(gols)
    jogadores.append(jogador.copy())
    ask =  input('Continuar ? (S/N) ').upper().strip()[0]
    if ask == 'N':
        break
print('=-'*30)
print('               TABELA')
print('=-'*30)

print(f'{"Código":<20}{"Nome":<20}{"Gols":<20}{"Total":>20}')
print('--'*30)
for c in range(0, len(jogadores)):
    print(f'{c:<20}{jogadores[c]["nome"]:<20}{jogadores[c]["Gols"]}{jogadores[c]["Total"]:>20}')

while True:
    cod = int(input('Digite o código do jogador (999 para sair) : '))
    if cod == 999:
        break
    else:
        print(f'--Levantamento do jogador {jogadores[cod]["nome"]} ')
        for i, g in enumerate(jogadores[cod]["Gols"]):
            print(f'Na {i+1}º Partida, {jogadores[cod]["nome"]} fez {g} Gols!')
