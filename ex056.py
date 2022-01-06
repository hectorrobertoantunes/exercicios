# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.


idades_somadas = 0
idade = 0
homem_velho = 0
mulheres_menos_vinte = 0
maior_idade = 0

for p in range(1, 5):
    print('----Pessoa {}º----'.format(p))
    nome = input('Nome: ').strip()
    idade = int(input('Idade: ').strip())
    sexo = input('Sexo: [F/M] ').strip().upper()
    idades_somadas += idade


    if sexo == 'M' and idade > maior_idade:
        homem_velho = nome
        maior_idade = idade
    if sexo == 'F' and idade < 20:
        mulheres_menos_vinte += 1

media_idade = idades_somadas / 4
print('A média de idades é {}'.format(media_idade))
print('O homem mais velho se chama {} e tem {} de idade'.format(maior_idade, homem_velho))
print('O número de mulheres que possuem menos de 20 anos é {}'.format(mulheres_menos_vinte))



