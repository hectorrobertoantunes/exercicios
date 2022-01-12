# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior_valor = soma = soma_tc = soma_pares = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = int(input(f'Coloque aqui o número da posição {[ l+1 ]}{ [c+1] }: '))
        matrix[l][c] = num
        soma += num
        if num % 2 == 0:
            soma_pares += num
        if c == 2:
            soma_tc += num
        if l == 1 and c == 0:
            maior_valor = num
        elif l == 1 and num > maior_valor:
            maior_valor = num
print(matrix)
for l in range(0, 3):
    print()
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^7}]', end='')
print(f'\nA soma dos valores pares digitados é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_tc}')
print(f'A soma de todos os valores da matrix é {soma}')
print(f'O maior valor da segunda linha é {maior_valor}')



