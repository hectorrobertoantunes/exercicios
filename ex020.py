'''Criar uma ordem aleatória de apresentação de um trabalho'''

import random
import names

lista = []
for x in range(1, 11):
    nome = names.get_full_name()
    lista.append(nome)


random.shuffle(lista)
print('A ordem da apresentação será: ',lista)
