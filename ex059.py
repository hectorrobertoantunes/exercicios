# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa


num_1 = float(input('Escreva o primeiro valor: '))
num_2 = float(input('Escreva o segundo valor: '))
exit = False

while exit is not True:
    print('[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos Números')
    print('[ 5 ] Sair')
    resp = int(input('Digite o valor da opção'))
    if resp == 1:
        print('O resultado da soma entre o {} + {} = {}'.format(num_1, num_2, num_1 + num_2))
    elif resp == 2:
        print('O resultado da multiplicação entre o {} x {} = {}'.format(num_1, num_2, num_1 * num_2))
    elif resp == 3:
        if num_1 > num_2:
            print('O primeiro número {} é maior que o segundo {}.'.format(num_1, num_2))
        elif num_1 < num_2:
            print('O primeiro número {} é ´menor que o segundo {}.'.format(num_1, num_2))
        else:
            print('O primeiro número {} é ´igual ao segundo {}.'.format(num_1, num_2))

    elif resp == 4:
        num_1 = float(input('Escreva o primeiro valor: '))
        num_2 = float(input('Escreva o segundo valor: '))

    elif resp == 5:
        exit = True


