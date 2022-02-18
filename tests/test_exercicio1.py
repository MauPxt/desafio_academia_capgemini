import unittest #importando a biblioteca para executar os testes unitários

from src.desafios.exercicio1 import escada

'''
O teste unitário será feito da seguinte maneira:
Primeiramente, a criação de uma classe que receberá o parametro de teste da biblioteca unittest. 
Logo após será definida uma função para testar a validade da função do exercício proposto.
'''
class TestExercicio1(unittest.TestCase):
    def test_escada(self):
        self.assertEqual(escada(1), '*')

        self.assertEqual(escada(2), ' *''\n'
                                    '**')

        self.assertEqual(escada(6),'     *''\n'
                                    '    **''\n'
                                    '   ***''\n'
                                    '  ****''\n'
                                    ' *****''\n'
                                    '******')


if __name__ == '__name__':
    unittest.main()