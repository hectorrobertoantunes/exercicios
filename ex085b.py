# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
for x in range(0, 7):
    numero = int(input(f'Digite o {x+1}o. número: '))
    if numero % 2 == 0:
        num[0].append(numero)
    else:
        num[1].append(numero)
print(f'Os números pares foram {sorted(num[0])}, e os ímpares {sorted(num[1])}')