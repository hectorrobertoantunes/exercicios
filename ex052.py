# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.



p = 0

num = int(input('Digite um número: '))

for x in range(1, num+1):
    if num % x == 0:
        p += 1

if p == 2:
    print('Este número é primo!')
else:
    print('Este número não é primo!')