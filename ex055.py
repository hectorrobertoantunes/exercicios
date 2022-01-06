# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos

pesos = []
for x in range(0,6):
    peso = float(input('qual o peso da {}º pessoa ? '.format(x+1)))
    pesos.append(peso)

print('A pessoa mais pesada tinha o peso de {} kg, enquanto a mais leve tinha {} kg'.format(max(pesos), min(pesos)))
