# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
# Não é tão eficiente

numeros = []
for x in range(0, 5):
    num = int(input('Digite um número inteiro: '))
    numeros.append(num)
print(f'A lista de números digitados foi {numeros}')
print(f'O maior valor digitado foi {max(numeros)} e o menor {min(numeros)}. As respectivas posições'
      f'foram {numeros.index(max(numeros))} e {numeros.index(min(numeros))}')
