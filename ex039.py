#  Faça um programa que leia o ano de nascimento de um jovem e informe,
#  de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#  se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
data = int(input('Coloque o ano do seu nascimento: '))
idade = date.today().year - data

if idade == 18:
    print('Está na hora de virar militar e babar o ovo do bolsonaro!')
elif idade > 18:
    print('Já passou da hora de se alistar! ')
else:
    print('Você ainda não tem 18 anos para o alistamento, mas faltam {} anos.. Fique de olho'.format(18 - idade))