 # Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 # Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
        'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')

while True:
    num = int(input('Coloque aqui um número de zero até vinte: '))
    if 20 >= num >= 0:
        break
    print('Tente novamente', end=' ')

print(f'O número {num} escrito por extenso é {cont[num]}')
