# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos

frase = input('Digite uma frase: ')
frase = frase.lower().replace(' ','')
in_frase = frase[::-1]
if frase == in_frase:
    print('Esta frase é um palíndromo')