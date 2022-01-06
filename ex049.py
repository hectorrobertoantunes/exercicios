#Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite o número que você quer saber a tabuada: '))

for x in range(0,11):
    print("{} x {} = {}".format(num, x, num * x))

