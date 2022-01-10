# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não.
# No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

p_mil = p_barato = total = np_barato = 0
while True:
    produto = input('Nome do produto: ')
    valor_p = float(input('Valor do produto R$: '))
    total += valor_p
    if valor_p == total:
        p_barato = valor_p
    if valor_p < p_barato:
        np_barato = produto
        p_barato = valor_p
    if valor_p > 1000:
        p_mil += 1
    ask = input('Quer continuar comprando [N/S]? ').upper().strip()
    if ask == 'N':
        break
print(f'O total gasto em compras foi de {total:.2f}.')
print(f'O produto mais barato foi {np_barato}, cujo o preço é R${p_barato:.2f} reais.')
print(f'{p_mil} Custaram mais de R$ 1000,00 reais!')
