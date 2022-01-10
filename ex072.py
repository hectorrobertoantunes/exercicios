# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

num = int(input('Digite o valor R$: '))
uni = ((num // 1)% 10 * 1)
dez = ((num // 10)% 10 * 10)
cen = ((num // 100)% 10 * 100)
mil = ((num // 1000)% 10 * 1000)

print(f'O número de notas de R$50,00 reais será {mil/50}')
print(f'O número de notas de R$20,00 reais será {cen/20}')
print(f'O número de notas de R$10,00 reais será {dez/10}')
print(f'O número de notas de R$1,00 reais será {uni/1}')
