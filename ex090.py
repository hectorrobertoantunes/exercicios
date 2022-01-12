#  Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#  No final, mostre o conteúdo da estrutura na tela.

notas = dict()
notas['Nome'] = input('Nome: ').capitalize().strip()
notas['Média'] = float(input('Média: '))

if notas['Média'] >= 5:
    notas['Situação'] = 'Aprovado(a)'
else:
    notas['Situação'] = 'Reprovado(a)'

print(f'O nome é igual à: {notas["Nome"]}')
print(f'A sua média é igual à: {notas["Média"]}')
print(f'A sua situação é de {notas["Situação"]}')