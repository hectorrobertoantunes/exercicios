'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

# <= 200 km = 0.50, > 200km = 0.45

distancia = float(input('Escreva a distância da sua viagem: '))
if distancia <= 200:
    print('O valor da sua viagem será de R${:.2f} '.format(distancia*0.5))
else:
    print('O valor da sua viagem será de R${:.2f}'.format(distancia*0.45))

# Outra forma de escrever o if seria =

# distancia = 200*0.5 if distancia >= 200 else distancia = 200*0.45 (maneira simplificada)