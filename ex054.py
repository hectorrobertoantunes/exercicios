# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime
maiores = 0
menores = 0
for x in range(0,7):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(x+1)))
    if datetime.date.today().year - ano <= 21:
        maiores += 1
    else:
        menores +=1

print('O número de pessoas maiores de idade são {}'.format(maiores))
print('O número de pessoas menores de idade são {}'.format(menores))