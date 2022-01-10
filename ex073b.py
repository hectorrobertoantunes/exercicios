#  Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
#  na ordem de colocação.
#  Depois mostre:

# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.

times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense',
         'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR',
         'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')

print(f'Os cinco primeiros times do Brasileirão são: {times[:5]}')
print(f'Os últimos quatro colocados do Brasileirão são: {times[-4:]}')
print(f'Os times em ordem alfabética {sorted(times)}')
print(f'O time da Chapecoense se encontra na posição {times.index("Chapecoense") + 1}')
