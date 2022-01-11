maior = 0
menor = 0
numeros = []
for x in range(0, 5):
    numeros.append(int(input('Digite um número inteiro: ')))
    if x == 0:
        maior = menor = numeros[x]
    elif numeros[x] > maior:
        maior = numeros[x]
    elif numeros[x] < maior:
        menor = numeros[x]
print(f'A lista de números digitadas foi {numeros}')
print(f'O maior número foi {maior} e está na posição: ', end='')
for p, n in enumerate(numeros):
    if n == maior:
        print(f'{p}...', end='')
print(f'\nO menor número foi {menor} e está na posição: ', end='')
for p, n in enumerate(numeros):
    if n == menor:
        print(f'{p}...', end='')