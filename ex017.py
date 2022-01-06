'''Fazer um programa que calcula a hipotenusa'''
from math import hypot

c_a = float(input('Coloque aqui o valor do cateto adjascente: '))
c_o = float(input('Coloque aqui o valor do cateto oposto: '))
hipo = hypot(c_a, c_o)
print('O valor da hipotenusa é de {}'.format(hipo))
