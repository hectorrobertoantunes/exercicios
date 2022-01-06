# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('Este programa fornece os 10 primeiros termos de uma P.A cujo o primeiro termo e a razão são fornecidos por você!')
num = int(input('Primeiro termo: '))
raz = int(input('Digite a razão: '))
exit = False
t = 10
num_t = 0
while exit is not True:
    for x in range(0, t):
        print('{}'.format(num), end=' -> ')
        num += raz
        num_t += 1
    print('PAUSA')
    t = int(input('Quantos termos vc quer a mais ?: '))
    if t == 0:
        exit = True
        print('O número de termos mostrados foi de {}'.format(num_t))

