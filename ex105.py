# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:

# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def nota(* n, sit=False):
    """
    Função que coloca as notas de uma turma em um dicionário e no final revela qual a maior, menor, média e a situação da turma

    :param n: Aqui você pode colocar quantas notas precisar, pois o asterisco cria uma tupla com os valores dentro de N
    :param sit: Se true mostra a situação dos alunos (Boa ou ruim). Se false não mostra a situação, somente os valores
    :return: Retorna um print de acordo com a situação.
    """

    soma = 0
    aluno = {}
    aluno['Total'] = len(n)
    aluno['Maior Nota'] = max(n)
    aluno['Menor Nota'] = min(n)
    for x in n:
        soma += x
    aluno['Média da turma'] = soma/len(n)
    if sit == True:
        if aluno['Média da turma'] >= 7:
            aluno['Situação'] = 'Boa'
            return print(aluno)
        else:
            aluno['Situação'] = 'Ruim'
            return print(aluno)
    else:
        return print(aluno)



nota(3, 5, 1.6, 1.7, 5, 7.4, 9.5, 6.4, 9, sit=True)

