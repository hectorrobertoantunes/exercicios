'''Faça um programa que diga se o número digitado é par ou ímpar'''

num = int(input('Escreva um número: '))
if (num % 2) == 0:
    print('o número {} é par'.format(num))
else:
    print('O número {} é ímpar'.format(num))
