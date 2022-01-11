# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

numeros = list()
while True:
    numeros.append(int(input('Digite um número: ')))
    ask = input('Quer continuar [N/S] ?: ').upper()
    if ask == 'N':
        break
numeros.sort(reverse=True)
print(f'A quantidades de números da sua lista é de {len(numeros)} e os números digitados foram {numeros}')

if 5 not in numeros:
    print('O número 5 não existe na sua lista!')
else:
    print('O número 5 existe na sua lista!')

