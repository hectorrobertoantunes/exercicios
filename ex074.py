# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
# mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(num)
maior = sorted(num)[-1]
menor = sorted(num)[0]

print(f'A tupla de números sorteados foi {num}')
print(f'O maior número dessa lista é o {maior}, enquanto que o menor foi {menor}')
