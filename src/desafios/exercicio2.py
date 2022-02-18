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
    '''
    Essa função testa a validade de uma senha sob os seguintes critérios:
        Possui no mínimo 6 caracteres.
        Contém no mínimo 1 digito numérico.
        Contém no mínimo 1 letra em minúsculo.
        Contém no mínimo 1 letra em maiúsculo.
        Contém no mínimo 1 caractere especial.

    :param senha: str: senha a ser testada
    :return: retorna se a senha é válida ou inválida
    '''
    password = senha
    controle = 0  # variável para controle

    while True:  # looping para validação dos testes
        if len(password) < 6:  # testando o tamanho da senha
            controle = -1
            print(
                f'A senha deve possuir no mínimo 6 caracteres! '
                f'Restam: {6 - len(senha)} caracteres')
            break

        elif not re.search("[0-9]", password):  # testando os dígitos numéricos
            print('A senha precisa conter no mínimo 1 dígito!')
            controle = -1
            break

        elif not re.search("[a-z]", password):  # testando as letras minúsculas
            print('A senha precisa conter no mínimo 1 letra em minúsculo!')
            controle = -1
            break

        elif not re.search("[A-Z]", password):  # testando as letras maiúsculas
            print('A senha precisa conter no mínimo 1 letra em maiúsculo!')
            controle = -1
            break

        elif not re.search("[_@$]", password):  # testando caracteres especiais
            print('A senha precisa conter no mínimo 1 caractere especial! '
                  'Ex: !@#$%^&*()-+')
            controle = -1
            break

        else:
            controle = 0
            resultado = "Senha válida!"
            break

    if controle == -1:  # verificando valor da variável controle
        resultado = "Senha inválida. Tente novamente!"

    return resultado


if __name__ == '__main__':
    validar_senha('Ya3@ff')
