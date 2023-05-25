import unittest  # importando a biblioteca para executar os testes unitários

from src.desafios.exercicio2 import validar_senha

"""
O teste unitário será feito da seguinte maneira:
Primeiramente, a criação de uma classe que receberá o parametro de teste da biblioteca unittest. 
Logo após será definida uma função para testar a validade da função do exercício proposto.
"""


class TestExercicio2(unittest.TestCase):
    def test_validar_senha(self):
        self.assertEqual(validar_senha('Ya3@ff'), 'Senha válida!')
        self.assertEqual(
            validar_senha('Ya3'), 'Senha inválida. Tente novamente!'
        )
        self.assertEqual(validar_senha(''), 'Senha inválida. Tente novamente!')
        self.assertEqual(
            validar_senha('123456'), 'Senha inválida. Tente novamente!'
        )
        self.assertEqual(
            validar_senha('abc123'), 'Senha inválida. Tente novamente!'
        )
        self.assertEqual(
            validar_senha('ABCXYZ'), 'Senha inválida. Tente novamente!'
        )
        self.assertEqual(
            validar_senha('@#$%^&'), 'Senha inválida. Tente novamente!'
        )
        self.assertEqual(
            validar_senha('Ya3@'), 'Senha inválida. Tente novamente!'
        )


if __name__ == '__name__':
    unittest.main()
