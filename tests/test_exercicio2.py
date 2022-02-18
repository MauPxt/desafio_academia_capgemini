import unittest

from src.desafios.exercicio2 import validar_senha


class TestExercicio2(unittest.TestCase):
    def test_validar_senha(self):
        self.assertEqual(validar_senha('Ya3@ff'), 'Senha válida!')
        self.assertEqual(validar_senha('Ya3'), 'Senha inválida. '
                                                  'Tente novamente!')


if __name__ == '__name__':
    unittest.main()
