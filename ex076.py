# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

itens = ('Lápis', 1.70,
         'Borracha', 2,
         'Caneta', 2.50,
         'Lapiseira', 7.50,
         'Mochila', 200,
         'Merendeira', 50,
         'Cadernos', 5.50,
         'Estojo', 7.90,
         'Livros', 100.90,
         'Folhas', 39.40)
print('='*40)
print(f'{"PAPELARIA":^40}')
print('='*40)

for pos in range(0, len(itens)):
    if pos % 2 == 0:
        print(f'{itens[pos]:.<30}', end='')
    else:
        print(f' R$ {itens[pos]:>.2f}')