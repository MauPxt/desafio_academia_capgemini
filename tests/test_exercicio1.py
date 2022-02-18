import unittest #importando a biblioteca para executar os testes unitários

from src.desafios.exercicio1 import half_pyramid

'''
O teste unitário será feito da seguinte maneira:
Primeiramente, a criação de uma classe que receberá o parametro de teste da biblioteca unittest. 
Logo após será definida uma função para testar a validade da função do exercício proposto.
'''
class TestExercicio1(unittest.TestCase):
    def test_half_pyramid(self):
        self.assertEqual(half_pyramid(1), '*')

        self.assertEqual(half_pyramid(2), ' *''\n'
                                        '**')

        self.assertEqual(half_pyramid(6),'     *''\n'
                                        '    **''\n'
                                        '   ***''\n'
                                        '  ****''\n'
                                        ' *****''\n'
                                        '******')


if __name__ == '__name__':
    unittest.main()