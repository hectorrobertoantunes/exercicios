#  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#  Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep

valor_casa = float(input('Escreva o valor da casa: '))
salario = float(input('Escreva o valor do seu salário: '))
anos = int(input('Em quantos anos você pagará a casa? '))

porcen_sal = salario * 0.3
meses = anos * 12
mensalidade = valor_casa / meses

print('Calculando..')
sleep(3)

print('Você pagará a casa em {} meses com mensalidades no valor de R$ {:.2f}'.format(meses, mensalidade))

if mensalidade > porcen_sal:
    print('Desculpe, mas a mensalidade ultrapassou os 30% do seu salário, portanto, empréstimo negado.')
else:
    print('A mensalidade da casa cabe no seu bolso, portanto, empréstimo aceito!')


