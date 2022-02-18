"""
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando
o caractere * e espaços. A base e altura da escada devem ser iguais ao
valor de n. A última linha não deve conter nenhum espaço.
"""


def half_pyramid(tamanho):
    '''
    Essa função gera uma "figura" de meia pirâmide tendo como tamanho o
    parâmetro inserido.

    :param tamanho: int: o tamanho desejado da pirâmide
    '''
    for r in range(tamanho):
        for _ in range(tamanho - r - 1):
            print(' ', end='')  # looping para a criação dos espaços
        for _ in range(r + 1):
            print('*', end='')  # looping para a criação do corpo (*)
        print('')  # print para avançar uma linha da "figura"

if __name__ == '__main__':
    half_pyramid(6)
