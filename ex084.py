# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

pessoas = []
dados = []
peso_maior = peso_menor = 0
while True:
    dados.append(input('Nome: ').strip())
    dados.append(float(input('Peso(kg): ').strip()))
    if len(pessoas) == 0:
        peso_maior = peso_menor = dados[1]
    else:
        if dados[1] > peso_maior:
            peso_maior = dados[1]
        if dados[1] < peso_menor:
            peso_menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    print(peso_maior)
    ask = input('Desenha continuar? [S/N]: ').upper().strip()
    if ask == 'N':
        break
print(f'O número de pessoas cadastradas foram {len(pessoas)}')
print(f'As pessoas mais pesadas foram: ', end='')
for p in pessoas:
    if p[1] == peso_maior:
        print(f'{p[0]}', end=', ')
print(f'\nAs pessoas mais leves fora: ', end='')
for p in pessoas:
    if p[1] == peso_menor:
        print(f'{p[0]}', end=', ')


