# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar,
# para cada palavra, quais são as suas vogais.

palavras = (input('Digite uma palavra: ').upper(), input('Digite uma palavra: ').upper(), input('Digite uma palavra: ').upper(),
            input('Digite uma palavra: ').upper(), input('Digite uma palavra: ').upper(), input('Digite uma palavra: ').upper())

vogais = ('A', 'E', 'I', 'O', 'U')

for palavra in palavras:
    print(f'\nA palavra {palavra} tem as vogais: ', end='')
    for vogal in vogais:
        if vogal in palavra:
            print(vogal, end=' ')

