"""
Escreva um algoritmo que mostre na tela uma escada de tamanho n utilizando
o caractere * e espaços. A base e altura da escada devem ser iguais ao
valor de n. A última linha não deve conter nenhum espaço.
"""


def escada(tamanho):
    '''
    Essa função gera uma "figura" de escada tendo como tamanho o
    parâmetro inserido.

    :param tamanho: int: o tamanho desejado da pirâmide
    :return: retorna a "figura" da escada de acordo com o tamanho desejado
    '''

    for r in range(tamanho):
        return "\n".join((" " * (tamanho - r - 1)) + ('*' * (r + 1)) for r in
                         range(tamanho))


if __name__ == '__main__':
    print(escada(6))