# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

count_id = count_id_menor = count_h = count_m = 0
while True:
    nome = input('Escreva o nome: ').strip().capitalize()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo [M/F]: ').strip().upper()

    if idade > 18:
        count_id += 1
    else:
        count_id_menor += 1

    if sexo == 'M':
        count_h += 1

    if idade < 20 and sexo == 'F':
        count_m += 1

    ask = input('Deseja continuar o cadastro [S/N]? ')

    if ask in 'nN':
        break

print(f'{count_id} possuem mais de 18 anos. ')
print(f'{count_h} homens foram cadastrados.')
print(f'{count_m} mulheres com menos de 20 anos foram cadastradas')
print(f'{count_id_menor} são menores de 18 anos')






