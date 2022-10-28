import os, json, time

from tabulate import tabulate

import Sistema.Sistema_Funcoes as ss

# caminho = "h:\\Meu Drive\\Estudos\\Programação\\Python\\Lets_Code\\Git\\Python\\Projetos\\Lets_Code_ADA\\DS_PY_002_Logica_de_Programacao_II_PY\\Dados\\Usuarios.json"

CAMINHO = "DS_PY_002_Logica_de_Programacao_II_PY\\Dados\\Usuarios.json"
caminho = os.path.join(os.getcwd(), CAMINHO)


def usuarios_arquivo_ler():
    """Faz a leitura dos dados do usuário e retorna em dicionário."""
    with open(caminho, "r", encoding="utf-8") as arquivo:
        usuarios_dicionario = json.load(arquivo)
    return usuarios_dicionario


def usuarios_gravar_arquivo(usuarios_dicionario):
    """Salva os dados do usuário em usuarios_dicionario."""
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(usuarios_dicionario, arquivo, indent=4, ensure_ascii=False)
    return usuarios_dicionario


def usuario_informacoes(nome: str):
    """Consulta usuário pelo nome e retorna o id + nome."""
    for id, usuario in usuarios_arquivo_ler().items():
        if usuario["Nome"] == nome:
            return id, usuario
    return None


def usuario_pedir_nome():
    nome = input("\nDigite o nome do usuario: ")
    if all(caracter.isalpha() or caracter.isspace() for caracter in nome):
        return nome.title()
    else:
        print("\nDigite apenas LETRAS no nome.\n")
        return usuario_pedir_nome()


def usuario_pedir_telefone():
    telefone = input("\nDigite o telefone do usuario: ")
    if telefone.isdigit() or telefone == "":
        return telefone
    else:
        print("\nDigite apenas NÚMEROS.\n")
        return usuario_pedir_telefone()


def usuario_pedir_endereco():
    endereco = input("\nDigite o endereço do usuario: ")
    return endereco


def usuario_consultar():
    """Para usuário não cadastrado, retorna mensagem."""
    nome = usuario_pedir_nome()
    usuario = usuario_informacoes(nome)
    print(usuario)
    if usuario != None:
        tabela(usuario)
        return usuario
    else:
        print(f"\nUsuário {nome} não encontrado!\n")
        return usuario_consultar()


def usuario_repetido(nome, telefone, endereco):
    """Para usuário com cadastro que já esteja cadastrado."""
    for id, usuario in usuarios_arquivo_ler().items():
        if (
            usuario["Status"] == True
            and usuario["Nome"] == nome
            and usuario["Telefone"] == telefone
            and usuario["Endereço"] == endereco
        ):
            print(f"\nUsuário -> {usuario['Nome']} já inserido e ativo\n")
            return menu_inserir_escolher()
        elif (
            usuario["Status"] == False
            and usuario["Nome"] == nome
            and usuario["Telefone"] == telefone
            and usuario["Endereço"] == endereco
        ):
            print(f"\nUsuário -> {usuario['Nome']} já inserido e agora reativado\n")
            usuario = id, usuario
            return usuario_ativar_desativar(usuario)


def usuario_inserir(
    telefone: str = "Nao Informado",
    endereco: str = "Nao Informado",
):
    """insere dados novo cadastro."""
    nome = usuario_pedir_nome()
    while not nome:
        nome = usuario_pedir_nome()
    telefone = usuario_pedir_telefone() or "Não informado"
    endereco = usuario_pedir_endereco() or "Não informado"
    usuario_repetido(nome, telefone, endereco)
    usuarios_dicionario = usuarios_arquivo_ler()
    usuarios_dicionario[str(len(usuarios_dicionario) + 1)] = {
        "Status": True,
        "Nome": nome,
        "Telefone": telefone,
        "Endereço": endereco,
    }
    usuarios_gravar_arquivo(usuarios_dicionario)
    # print("\nAdiconado com sucesso.")
    menu_inserir_escolher()
    return usuarios_arquivo_ler()


def menu_inserir_usuario():
    print(
        """
    -----------------------------------
    |        Funcionalidades:         |
    |                                 |
    | 1 - Inserir outro usuário       |
    | 2 - Votar ao Menu Pincipal      |
    ___________________________________
    """
    )


def menu_inserir_escolher():
    menu_inserir_usuario()
    opcao = escolher()
    match opcao:
        case 1:
            return usuario_inserir()
        case 2:
            return ss.comecar()


def escolher():
    opcao = input("Escolha uma, entre as opções acima: ")
    if opcao.isdigit():
        return int(opcao)
    else:
        print("Digite apenas o NÚMERO da opção escolhida.")
        return escolher()


def menu_atualizar():
    print(
        """
    -----------------------------------
    |        Funcionalidades:         |
    |                                 |
    | 1 - Ativar/Desativar usuário    |
    | 2 - Atualizar nome              |
    | 3 - Atualizar telefone          |
    | 4 - Atualizar endereço          |
    | 5 - Atualizar cadastro completo |
    ___________________________________
    """
    )


def menu_atualizar_ecolher(opcao, usuario):
    id, _ = usuario
    usuarios = usuarios_arquivo_ler()
    match opcao:
        case 1:
            usuario_ativar_desativar(usuario)
        case 2:
            nome = usuario_pedir_nome()
            usuarios[id]["Nome"] = nome
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 3:
            telefone = usuario_pedir_telefone()
            usuarios[id]["Telefone"] = telefone
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 4:
            endereco = usuario_pedir_endereco()
            usuarios[id]["Endereço"] = endereco
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case 5:
            nome = usuario_pedir_nome()
            endereco = usuario_pedir_endereco()
            telefone = usuario_pedir_telefone()
            usuarios[id] = {
                "Status": True,
                "Nome": nome,
                "Telefone": telefone,
                "Endereço": endereco,
            }
            usuarios_gravar_arquivo(usuarios)
            return "\nAlterado com sucesso."
        case _:
            print("\n-------------------------------------------------")
            print("| Opção inválida, escolha uma das opções acima. |")
            print("-------------------------------------------------\n")
            time.sleep(3)
            return escolher()


def usuario_atualizar(usuario):
    menu_atualizar()
    opcao = escolher()
    menu_atualizar_ecolher(opcao, usuario)


def usuario_excluir():
    usuarios = usuarios_arquivo_ler()
    id, usuario = usuario_consultar()
    usuarios[id]["Status"] = False
    usuarios_gravar_arquivo(usuarios)
    dicionario = id, usuario
    tabela(dicionario)
    return print(f"\nStatus do usuário modificado com sucesso")


def usuarios_ativos():
    """retorna todos os usuários ativos no cadastro."""
    ativos = {}
    for id, usuario in usuarios_arquivo_ler().items():
        if usuario["Status"] == True:
            ativos[id] = usuario
    return ativos


def usuarios_exclidos():
    """retorna todos os cadastros inativos."""
    inativos = {}
    for id, usuario in usuarios_arquivo_ler().items():
        if usuario["Status"] == False:
            inativos[id] = usuario
    return inativos


def usuario_ativar_desativar(usuario):
    id, _ = usuario
    usuarios = usuarios_arquivo_ler()
    if usuarios[id]["Status"] == True:
        usuarios[id]["Status"] = False
        usuarios_gravar_arquivo(usuarios)
    else:
        usuarios[id]["Status"] = True
        usuarios_gravar_arquivo(usuarios)
    tabela(usuario_informacoes(usuario[1]["Nome"]))
    return print("Status do usuario alterado com sucesso.")


def tabela(dicionario):
    tabela = []
    headers = ["ID", "STATUS", "NOME", "TELEFONE", "ENDEREÇO"]
    if type(dicionario) == dict:
        for id, usuario in dicionario.items():
            tabela.append(
                [
                    id,
                    usuario["Status"],
                    usuario["Nome"],
                    usuario["Telefone"],
                    usuario["Endereço"],
                ]
            )
    else:
        id, usuario = dicionario
        tabela.append(
            [
                id,
                usuario["Status"],
                usuario["Nome"],
                usuario["Telefone"],
                usuario["Endereço"],
            ]
        )
    print(tabulate(tabela, headers, tablefmt="simple_grid"))
