import unittest

from src.desafios.exercicio1 import half_pyramid


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