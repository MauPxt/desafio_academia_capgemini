import unittest  # importando a biblioteca para executar os testes unitários

from src.desafios.exercicio1 import escada

"""
O teste unitário será feito da seguinte maneira:
Primeiramente, a criação de uma classe que receberá o parametro de teste da biblioteca unittest. 
Logo após será definida uma função para testar a validade da função do exercício proposto.
"""


class TestEscada(unittest.TestCase):
    def test_escada(self):
        # Testando escada com tamanho 0
        self.assertEqual(escada(0), '')

        # Testando escada com tamanho 1
        self.assertEqual(escada(1), '*')

        # Testando escada com tamanho 2
        escada_2 = ' *\n**'
        self.assertEqual(escada(2), escada_2)

        # Testando escada com tamanho 6
        escada_6 = '     *\n    **\n   ***\n  ****\n *****\n******'
        self.assertEqual(escada(6), escada_6)

        # Testando escada com tamanho 10
        escada_10 = '         *\n        **\n       ***\n      ****\n     *****\n    ******\n   *******\n  ********\n *********\n**********'
        self.assertEqual(escada(10), escada_10)


if __name__ == '__name__':
    unittest.main()
