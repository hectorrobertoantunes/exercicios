# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

def fatorial(num, show=False):
    """
    Esta função mostra o fatorial de um número inteiro
    :param num: O número que vc quer saber o fatorial
    :param show: Aqui mostra os calculos feito. Por padrão está false, mas se vc colocar True mostra o cálculo feito.
    :return: o returno é o resultado do calculo
    """
    f = 1
    for x in range(num, f, -1):
        f *= x
        if show == True:
            print(f'{x} x', end=' ')
        if x == 2:
            print(f'1 = {f}')

    return f


fatorial(5, True)
