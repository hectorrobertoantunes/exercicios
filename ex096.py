# Faça um programa que tenha uma função chamada área(),
# que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(a, b):
    result = a * b
    print(f'A área de um terreno {a} x {b} é de {result} metros quadrados')

print('  Controle de terreno')
print('--------------------')
w = float(input('Coloque aqui a largura do terreno: '))
l = float(input('Coloque aqui o comprimento do terreno: '))
area(w, l)