import datetime
info = {}

while True:
    info["Nome"] = input('Nome: ')
    info["ano_nascimento"] = int(input('Ano de nascimento: '))
    info["carteira"] = int(input('Número da carteira de trabalho [0 se não tem]: '))
    if info["carteira"] == 0:
        break
    info["ano_contratacao"] = int(input('Ano de contratação: '))
    info["Salário"] = float(input('Salário: '))
    break

print(f'O nome é: {info["Nome"]}')
print(f'A idade é: {datetime.date.today().year - info["ano_nascimento"]}')
if info["carteira"] != 0:
    print(f'A carteira de trabalho tem a numeração: {info["carteira"]}')
    print(f'Foi contratado(a) em: {info["ano_contratacao"]}')
    print(f'Salário: {info["Salário"]}')
    print(f'Aposentará com {(datetime.date.today().year - info["ano_nascimento"]) + 35}')
else:
    print('Não possui carteira assinada.')


