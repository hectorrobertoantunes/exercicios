# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

ask =  0
num_list = []
while ask != 'S':
    num = int(input('Digite um número: '))
    num_list.append(num)
    ask = input('Deseja continuar a digitar valores? [S/N]').upper()

print('O Maior número foi {}, o menor foi {} e a média foi de {}'.format(max(num_list), min(num_list), sum(num_list)/len(num_list)))
