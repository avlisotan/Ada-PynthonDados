import os, time

from Usuarios.Usuarios_Funcoes import *


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")
    pass


def menu_principal():
    return print(
        f""" 
    ---------------------------------------------------------------------------------------------------------
    |                     Boas vindo(a) ao nosso sistema de cadastro de usuário(a):                         |
    |                                                                                                       |
    |   1 - Inserir usuário                              |   2 - Excluir usuário                            |   
    |   3 - Atualizar usuário                            |   4 - Informações de um usuário                  |   
    |   5 - Informações de todos os usuários             |   6 - Informações de todos os usuários ativos    |   
    |   7 - Informações de todos os usuários excluídos   |   8 - Ativar/Desativar usuário                   |
    |   9 - Limpar Tela                                  |   0 - Sair                                       |
    ---------------------------------------------------------------------------------------------------------
    """
    )


def comecar():
    """Printa na tela o menu de opções"""

    menu_principal()

    opcao = escolher()

    menu_principal_escolher(opcao)

    return opcao


def menu_principal_escolher(opcao):
    """Match cases das opções disponíveis para o usuário"""
    match opcao:
        case 1:
            usuario_inserir()
            return comecar()
        case 2:
            usuario_excluir()
            return comecar()
        case 3:
            usuario = usuario_consultar()
            usuario_atualizar(usuario)
            return comecar()
        case 4:
            usuario_consultar()
            return comecar()
        case 5:
            tabela(usuarios_arquivo_ler())
            return comecar()
        case 6:
            tabela(usuarios_ativos())
            return comecar()
        case 7:
            tabela(usuarios_exclidos())
            return comecar()
        case 8:
            usuario = usuario_consultar()
            usuario_ativar_desativar(usuario)
            return comecar()
        case 9:
            limpar_tela()
            return comecar()
        case 0:
            return sistema_sair()
        case _:
            print("\n-------------------------------------------------")
            print("| Opção inválida, escolha uma das opções acima. |")
            print("-------------------------------------------------\n")
            time.sleep(3)
            return comecar()


def sistema_sair():
    print("\n------------------")
    print("| Até a próxima. |")
    print("------------------\n")
    pass
