# Faça um programa que tenha uma função chamada contador(),
# que receba três parâmetros:
# início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2
# c) uma contagem personalizada
from time import sleep
def  contador(a, b, c):

    if b <= 0:
        constante = -1
    else:
        constante = 1

    for x in range(a, b + constante, c):
        print(x, end=' ')
        sleep(0.5)


contador(10, 0, -2)
print('\n Agora é a sua vez, crie uma contagem personalizada')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

if b <= 0:
    constante = -1
else:
    constante = 1

for x in range(a, b + constante, c):
    print(x, end=' ')
    sleep(0.5)