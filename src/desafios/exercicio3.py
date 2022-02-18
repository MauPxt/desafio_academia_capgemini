"""
Duas palavras podem ser consideradas anagramas de si mesmas se as letras de
uma palavra podem ser realocadas para formar a outra palavra. Dada uma string
qualquer, desenvolva um algoritmo que encontre o número de pares de substrings
que são anagramas.

"""
# GABARITO:
# resultado 'ovo' = 2 // [o, o], [ov, vo] == o:2,ov:2
# resultado2 'ifailuhkqq' = 3 // [i, i], [q, q] e [ifa, fai] == i:2,q:2,ifa:2

# Importando a função Counter da biblioteca collections que facilitará a
# resolução do problema proposto:
from collections import Counter


def pares_anagramas_parciais(palavra):
    '''
    Essa função verificará a quantidade de pares de anagramas parciais do
    parâmetro inserido.

    :param palavra: str: a palavra que deseja testar
    :return: retorna a quantidade de combinações possíveis com pares de
             anagramas
    '''

    # A variável 'contagem' foi estabelecida utilizando a função counter para
    # manipular as letras da palavra que foi inserida como parâmetro:
    contagem = Counter(
        ("".join(sorted(palavra[j:j + i])) for i in
         range(1, len(palavra)) for j in
         range(0, len(palavra) - i + 1)))

    # A variável 'valores_aceitaveis' elenca as letras que possuem repetições
    # válidas, por tanto acabam sendo elegíveis para a formação do anagrama:
    valores_aceitaveis = {chave: valor for chave, valor in
                          contagem.items() if valor >= 2}
    print(f'Valores que formam anagramas válidos para a palavra '
          f'"{palavra}": {valores_aceitaveis}')

    # Por fim, o retorno nada mais é do que uma simples manipulação
    # utilizando a interação da função sum com um looping nos
    # valores da variável 'contagem':
    return sum(sum(range(i)) for i in contagem.values())


if __name__ == '__main__':
    print('O número de pares de substrings que são anagramas é igual a: ',
          pares_anagramas_parciais('ovo'))
    print('O número de pares de substrings que são anagramas é igual a: ',
          pares_anagramas_parciais('ifailuhkqq'))
