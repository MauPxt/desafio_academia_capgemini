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
    :return: retorna a "figura" da meia piramide de acordo com o tamanho desejado
    '''

    for r in range(tamanho):
        return "\n".join((" " * (tamanho - r - 1)) + ('*' * (r + 1)) for r in
                         range(tamanho))


if __name__ == '__main__':
    print(half_pyramid(6))