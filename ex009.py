# Fazer uma tabuada

num = int(input('Coloque aqui um número de 0 a 10: '))
print('------------')
for X in range(0,11):
    print('{} x {} = {}'.format(num, X, num*X ))
print('------------')