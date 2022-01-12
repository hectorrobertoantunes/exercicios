ficha = list()

while True:
    nome = input('Nome: ').capitalize().strip()
    nota_1 = float(input('Nota 1: '))
    nota_2 = float(input('Nota 2: '))
    media = (nota_1 + nota_2) / 2
    ficha.append([nome, [nota_1, nota_2], media])
    ask = input('Quer continuar [S/N]? ').upper()
    if ask == 'N':
        break
print('=+='*20)
print(f'{"     Notas     ":^11}')
print('=+='*20)
i = 0
print(f'{"No":<10}{"Nome":<10}{"Média":<10}')
while i < len(ficha):
    print(f'{i:<10}{ficha[i][0]:<10}{ficha[i][2]:<10}')
    i += 1
while True:
    ask_2 = int(input('\nDigite o index para saber as notas ou 999 para sair: '))
    if ask_2 == 999:
        break
    else:
        print(ficha[ask_2][1])
