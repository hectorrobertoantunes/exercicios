# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista
# e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint

def sorteia(a):
    for x in range(0, 5):
        numero = randint(0, 100)
        a.append(numero)

def somaPar(lista):
    soma = 0
    for x in lista:
        if x % 2 == 0:
            soma += x
    print(f'A soma dos pares da {lista} é {soma}')

numeros = []
sorteia(numeros)
somaPar(numeros)


