# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições

def voto(ano):
    import datetime
    idade = datetime.date.today().year - ano
    if idade < 16:
        return print(f'Você tem {idade}: Não pode votar ainda')
    elif idade >=18 and idade <= 65:
        return print(f'Você tem {idade}: Voto é obrigatório')
    else:
        return print(f'Voctê tem {idade}: Voto não é obrigatório')


nascimento = int(input('Coloque o seu ano de nascimento: '))
voto(nascimento)
