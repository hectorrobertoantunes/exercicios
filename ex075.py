# Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final,
# mostre:

# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o outro valor: '))
num3 = int(input('Digite o terceiro valor: '))
num4 = int(input('Digite o último valor: '))
tupla = (num, num2, num3, num4)
print(f'Você digitou os valores {tupla}')
if 9 in tupla:
    print(f'O número nove apareceu {tupla.count(9)} vezes')
else:
    print('O número nove não está na tupla')
if 3 in tupla:
    print(f'O valor três apareceu na {tupla.index(3) + 1} posição')
else:
    print('O valor três não existe na tupla!')

print('Os valores pares digitados foram:', end=' ')
for x in tupla:
    if x % 2 == 0:
        print(x, end=', ')

