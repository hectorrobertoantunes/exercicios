# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

exit = False
soma = 0
count_num = 0
while exit is not True:
    num = int(input('Digite qualquer número [Digite 999 para parar]: '))
    if num == 999:
        exit = True
        num = 0
    soma += num
    count_num += 1


print('\033[33mVocê digitou {} números e a soma dos valores digitados foi {}'.format(count_num - 1, soma))