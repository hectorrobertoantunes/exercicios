# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = []

while True:
    num = int(input('Digite um número: '))
    if num in numeros:
        ask = input('Você quer continuar [N/S]? ').upper()
        if ask == 'N':
            break
        num = int(input('Digite um número: '))

    else:
        numeros.append(num)
    ask = input('Você quer continuar [N/S]? ').upper()
    if ask == 'N':
        break
print(f'Os números digitados foram: {sorted(numeros)}')