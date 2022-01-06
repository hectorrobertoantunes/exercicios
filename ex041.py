# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

import datetime


ano = int(input('Coloque o ano do seu nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano

if idade <= 9:
    print('Categoria: Mirim')
elif idade <=14:
    print('Categoria: Infantil')
elif idade <= 19:
    print('Categoria: Júnior')
elif idade <= 25:
    print('Categoria: Sênior')
else:
    print('Categoria: Master')