'''Crie um programa que mostre o nome completo de uma pessoa e
forneça as seguinte informações:
          -  O nome com todas as letras maiúsculas e minúsculas
          -  Quantas letras existem ao todo sem considerar os espaços
          -  Quantas letras exister no primeiro nome da pessoa.'''


nome = input('Escreva aqui um nome Completo: ')
mai = nome.upper()
min = nome.lower()
spc_num = nome.count(" ")
letter_num = len(nome) - spc_num

print(mai)
print(min)
print('O numero de  espaços é de: {}'.format(spc_num))
print('O número de letras no nome é de: {}'.format(letter_num))

