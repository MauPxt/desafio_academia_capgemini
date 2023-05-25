"""
Débora se inscreveu em uma rede social para se manter em contato com seus
amigos. A página de cadastro exigia o preenchimento dos campos de nome e
senha, porém a senha precisa ser forte. O site considera uma senha forte
quando ela satisfaz os seguintes critérios:

Possui no mínimo 6 caracteres.
Contém no mínimo 1 digito.
Contém no mínimo 1 letra em minúsculo.
Contém no mínimo 1 letra em maiúsculo.
Contém no mínimo 1 caractere especial. Os caracteres especiais são:!@#$%^&*()-+

Débora digitou uma string aleatória no campo de senha, porém ela não tem
certeza se é uma senha forte. Para ajudar Débora, construa um algoritmo que
informe qual é o número mínimo de caracteres que devem ser adicionados para
uma string qualquer ser considerada segura.
"""

# importando a biblioteca re, pois nela contém expressões interessantes para
# a resolução do problema atual:
import re


def validar_senha(senha):
    """
    Essa função testa a validade de uma senha sob os seguintes critérios:
        Possui no mínimo 6 caracteres.
        Contém no mínimo 1 digito numérico.
        Contém no mínimo 1 letra em minúsculo.
        Contém no mínimo 1 letra em maiúsculo.
        Contém no mínimo 1 caractere especial.

    :param senha: str: senha a ser testada
    :return: retorna se a senha é válida ou inválida
    """
    if not (
        len(senha) >= 6
        and re.search(r'\d', senha)
        and re.search(r'[a-z]', senha)
        and re.search(r'[A-Z]', senha)
        and re.search(r'[_@$]', senha)
    ):
        return 'Senha inválida. Tente novamente!'

    return 'Senha válida!'


if __name__ == '__main__':
    validar_senha('Ya3')
