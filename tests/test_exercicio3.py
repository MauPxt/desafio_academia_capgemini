import unittest

from src.desafios.exercicio3 import pares_anagramas_parciais


class TestExercicio3(unittest.TestCase):
    def test_validar_senha(self):
        self.assertEqual(pares_anagramas_parciais('ovo'), 2)
        self.assertEqual(pares_anagramas_parciais('ifailuhkqq'), 3)


if __name__ == '__name__':
    unittest.main()
