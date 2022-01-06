# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('Este programa fornece os 10 primeiros termos de uma P.A cujo o primeiro termo e a razão são fornecidos por você!')
num = int(input('Primeiro termo: '))
raz = int(input('Digite a razão: '))

for x in range(0,10):
    print('{}'.format(num), end = ' -> ')
    num += raz
print('FIM')
