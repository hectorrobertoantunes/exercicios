'''Faça um programa que leia um número  de 0 a 9999  e mostre na tela cada um dos dígitos separados'''

num = int(input('Digite um número de até quatro algarismos: '))
uni = print('Unidade: {} '.format((num//1)%10))
dez = print('Dezena: {} '.format((num//10)%10))
cen = print('Centeza: {} '.format((num//100)%10))
mil = print('Milhar: {} '.format((num//1000)%10))

