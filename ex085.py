# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única
# que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

lista_geral = []
lista_par = []
lista_impar = []
for x in range(0, 7):
    num = int(input(f'Coloque o {x+1}o. número: '))
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)
lista_geral.append(lista_par)
lista_geral.append(lista_impar)
print(f'Os números pares foram {sorted(lista_geral[0])}')
print(f'Os números ímpares foram {sorted(lista_geral[1])}')