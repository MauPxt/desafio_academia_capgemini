import unittest #importando a biblioteca para executar os testes unitários

from src.desafios.exercicio3 import pares_anagramas_parciais

'''
O teste unitário será feito da seguinte maneira:
Primeiramente, a criação de uma classe que receberá o parametro de teste da biblioteca unittest. 
Logo após será definida uma função para testar a validade da função do exercício proposto.
'''

class TestExercicio3(unittest.TestCase):
    def test_validar_senha(self):
        self.assertEqual(pares_anagramas_parciais('ovo'), 2)
        self.assertEqual(pares_anagramas_parciais('ifailuhkqq'), 3)


if __name__ == '__name__':
    unittest.main()
