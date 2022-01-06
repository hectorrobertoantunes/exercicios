'''Crie um programa que leia o nome de uma cidade e diga se o nome começa com Santo'''

nome = input('Coloque aqui o nome da sua cidade: ')

nome = nome.lower().title().strip().split()
print(nome)
if nome[0] == 'Santo':
    print('True, pois o nome da sua cidade começa com Santo')
else:
    print('False, pois o nome da sua cidade com começa com Santo')