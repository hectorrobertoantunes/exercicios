# Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.

i = 0
s = 0
for x in range(1,501,2):
    if x % 3 == 0:
        i += 1
        s += x
print('Entre 1 e 500 temos {} número, e a soma desses números é {} '.format(i, s))