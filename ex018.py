'''Criar um programa que nos informe qual é o valor do seno, cosseno e tangente de um angulo.'''
from math import sin, tan, radians, degrees, cos

angulo = float(input('Escreve aqui o angulo: '))
radianos = radians(angulo)
seno = sin(radianos)
cosseno = cos(radianos)
tangente = tan(radianos)
print('O valos do seno é {} e do cosseno é {}, por fim a tangente é {}'.format(seno, cosseno, tangente))
