'''Crie um programa que leia o nome de uma pessoa  e diga se ela  tem SILVA no nome'''

nome = input('Escreva o seu nome: ')
nome =  nome.lower().title()
print('Silva' in nome)