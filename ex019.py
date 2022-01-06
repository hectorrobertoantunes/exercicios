'''Sorteando um item da lista'''
import random
import names

lista = []
for x in range(1, 11):
    nome = names.get_full_name()
    lista.append(nome)

escolhido = random.choice(lista)
print('O nome escolhido da lista foi {}'.format(escolhido))
