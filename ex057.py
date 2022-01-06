# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto

sexo = input('Coloque seu sexo [F/M]: ')
while sexo not in 'FMfm':
    sexo = input('Dados inválidos, informe novamente o seu sexo: ')
print('Tudo certo, obrigado!')