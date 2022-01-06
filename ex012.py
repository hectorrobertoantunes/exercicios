# Calculando Descontos
produto = float(input('Colque aqui o valor do produto: '))
desconto = produto * 0.05
Valor_Final = produto - desconto
print('O produto receberá um desconto de 5%, logo o seu preço inicial era {} e agora está à {}'.format(produto, Valor_Final))