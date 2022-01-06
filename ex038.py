# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num = int(input('Escreva um número: '))
num2 = int(input('Escreva outro número: '))
print('Agora o computador irá falar se são números iguais ou não. Caso a segunda, ele mostrará o maior e menor')

if num > num2:
    print('O primeiro número {} é maior que o segundo {}'.format(num, num2))
elif num < num2:
    print('O segundo número {} é maior que o primeiro {}'.format(num2, num))
else:
    print('Os número são iguais!')