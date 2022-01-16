#  Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#  Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

def maior(* num):
    from time import sleep
    print('Analisando os valores passados...')
    sleep(1)
    print(f'{num} são os valores que foram passados. Portanto existem {len(num)} elementos.')

    maior = 0
    for x in num:
        if x >= maior:
            maior = x

    print(f'Dentre esses, o maior elemento é o {maior}')

maior()