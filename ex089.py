# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
# notas de cada aluno individualmente.

import math

alunos = []
while True:
    temporario_nome = []
    temporario_nota = []
    nome = input('Nome do aluno(a): ').capitalize()
    nota = float(input('Nota 1 do aluno(a): '))
    nota_2 = float(input('Nota 2 do aluno(a): '))
    media = (nota + nota_2) / 2
    temporario_nome.append(nome)
    temporario_nota.append(nota)
    temporario_nota.append(nota_2)
    temporario_nome.append(temporario_nota)
    temporario_nome.append(media)
    alunos.append(temporario_nome[:])
    ask = input('Quer continuar [N/S] ? ').upper()
    if ask == 'N':
        break
print('=+='*20)
print(f'{"     Notas     ":^11}')
print('=+='*20)
i = 0
print(f'{"No":<10}{"Nome":<10}{"Média":<10}')
while i < len(alunos):
    print(f'{i:<10}{alunos[i][0]:<10}{alunos[i][2]:<10}')
    i += 1

while True:
    ask_2 = int(input('\nDigite o index para saber as notas ou 999 para sair: '))
    if ask_2 == 999:
        break
    else:
        print(alunos[ask_2][1])




