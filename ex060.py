# Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Coloque o número: '))

i = 1
result = num
while i != num:
    result = result * i
    i += 1
print(result)


