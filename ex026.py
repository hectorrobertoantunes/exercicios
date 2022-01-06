'''Criar um programa que conta a quantidade de letras A que existem em uma frase e a posição da primeira
 e última letras A'''

frase = input('Escreva a frase: ')
frase = frase.upper().strip()
print('O número de letra "A" que existem na frase é {}'.format(frase.count('A')))
print('A posição da primeira letra "A" é {}'.format(frase.find('A')+1))
print('A posição da última letra "A" é {}'.format(frase.rfind('A')+1))