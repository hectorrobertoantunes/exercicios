'''Faça um programa que leia o nome compelto de uma pessoa mostrando em seguida o primeiro e o último nome, separadamente.
'''

import names

while True:


    nome = names.get_full_name()
    print(nome)
    nome = nome.strip().split()
    print('O seu primeiro nome é {}'.format(nome[0]))
    print('O seu útimo nome é {}'.format(nome[-1]))

