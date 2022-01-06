'''Escreva um programa que leia a velocidade de um carro. Se ele ultrapassr 80km/h mostre uma
menssagem dizendo que ele foi multado. A multa é de R$ 7,00 para cada km acima do limite.'''
from time import sleep
velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80:
    print('Você está indo rápido demais! Foi multado pelo radar!!')
    print('Calculando a sua multa...')
    sleep(5)
    multa = (velocidade - 80) * 7

    print('O valor da sua multa foi de R$ {:.2f} reais'.format(multa))
else:
    print('A sua velocidade está igual ou abaixo de 80km/h, se beber não dirija!')