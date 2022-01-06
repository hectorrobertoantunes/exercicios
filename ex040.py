#Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota_1 = float(input('Coloque a nota da primeira prova: '))
nota_2 = float(input('Coloque a nota da segunda prova: '))

media = ((nota_2 + nota_1) / 2)
print(media)

if media == 7:
    print('Aprovado')
elif media > 5 and media <= 6.9:
    print('Reco Reco')
else:
    print('Reprovado')