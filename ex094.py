# Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

ficha = []
pessoa = {}
lista_mulheres = []
lista_idade_acima = []
while True:
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    pessoa['sexo'] = input('Sexo [M/F]: ').upper().strip()

    while pessoa['sexo'] != 'M' and pessoa['sexo'] != 'F':
        print('Tecla inválida. Por favor, escolha entre M ou F....')
        pessoa['sexo'] = input('Sexo [M/F]: ').upper().strip()

    pessoa['idade'] = int(input('Idade: '))
    ask = input('Deseja continuar [S/N] ? ').strip().upper()
    while ask != 'S' and ask != 'N':
        print('Tecla inválida. Digite S para sim e N para não...')
        ask = input('Deseja continuar [S/N] ? ').strip().upper()
    if pessoa['sexo'] == 'F':
        lista_mulheres.append(pessoa['nome'])

    ficha.append(pessoa.copy())
    if ask == 'N':
        break

num_pessoas = len(ficha)
media_idade = soma_idade = 0

for i in ficha:
    soma_idade += i['idade']
media_idade = soma_idade / num_pessoas
for i in ficha:
    if i['idade'] > media_idade:
        lista_idade_acima.append(i['nome'])
        print(lista_idade_acima)

print(f'O número de pessoas cadastradas foi de {num_pessoas}')
print(f'A média da idade das pessoas cadastradas foi de {media_idade}')

print(f'As mulheres que foram cadastradas foram: ', end=' ')
for m in lista_mulheres:
    print(f'{m}', end=' ')

print(f'\nAs pessoas que possuem a idade acima da média são: ', end=' ')
for idades in lista_idade_acima:
     print(f'{idades}', end=' ')





