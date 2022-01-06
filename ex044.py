# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros
from time import sleep
preco = float(input('O valor do produto R$ '))
print('Carregando opções de pagamento...')
sleep(3)
print('Você pode pagar de quatro formas diferente A - à vista/cheque e você ganhará 10% de desconto')
print('Você pode pagar de quatro formas diferente B - à vista no cartão e você ganhará 5% de desconto')
print('Você pode pagar de quatro formas diferente C -  até 2x no cartão: preço formal')
print('Você pode pagar de quatro formas diferente D - 3x ou mais no cartão: 20% de juros')
pagamento = input('Qual seria a forma de pagamento? (A) (B) (C) (D) ')

if pagamento == 'A':
    print('O seu método de pagamento será à vista com cheque, o produto era R$ {:.2f} e agora será R$ {:.2f}'.format(preco, preco - (preco * 0.1)))
elif pagamento == 'B':
    print('O seu método de pagamento será à vista com cartão, o produto era R$ {:.2f} e agora será R$ {:.2f}'.format(preco, preco - (preco * 0.05)))
elif pagamento == 'C':
    print('O seu método de pagamento será 2x com cartão, o produto era R$ {:.2f} e agora será R$ {:.2f}'.format(preco, preco))
else:
    print('O seu método de pagamento será 3x  com cartão, o produto era R$ {:.2f} e agora será R$ {:.2f}'.format(preco, preco + (preco * 0.2)))






