'''Faça um programa que dê somente a parte inteira de um número float'''
import math

num = float(input('Escreva aqui um número decimal: '))
inteiro = math.trunc(num)
print('O número que você escolheu foi o {} e a sua parte inteira é {}'.format(num, inteiro))