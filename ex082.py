# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas


lista_geral = []
lista_impares = []
lista_pares = []
while True:
    lista_geral.append(int(input('Digite um número: ')))
    ask = input('Quer continuar? [S/N]').upper()
    if ask == 'N':
        break

for x in lista_geral:
    if x % 2 == 0:
        lista_pares.append(x)
    else:
        lista_impares.append(x)

print(f'A lista geral é {lista_geral}')
print(f'A sua lista de números pares é {lista_pares}')
print(f'A sua lista de números ímpares é {lista_impares}')