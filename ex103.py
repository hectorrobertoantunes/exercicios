# Faça um programa que tenha uma função chamada ficha(),
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.

def ficha(jogador='<desconhecido>', gol=0):
    return print(f'O {jogador} fez um número de {gol} gol(s) na partida.')

# Main program

nome = input('Digite o nome do jogador: ')
gols = input('Digite o número de gols que o jogador fez: ')

if gols.isnumeric() == True:
    gols = int(gols)
else:
    gols = 0

if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
