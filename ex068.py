# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.

while True:
    print('-'*30)
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for x in range(0, 11):
        print(f'{num} x {x} = {num * x}')
    print('-' * 30)

