# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(num):
    while True:
        if num.isnumeric() == True:
            return print(f'Você digitou o número {num}')
        else:
            print('Error, você não digitou um número')
            num = input('Digite um número: ')

num = input('Digite um número: ')
leiaInt(num)