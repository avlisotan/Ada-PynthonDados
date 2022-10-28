def sortear_palavra():
    import random
    lista_palavras = ['arvore', 'banana', 'gato', 'bola', 'escova']
    palavra_sorteada = random.choice(lista_palavras)
    chances = (len(palavra_sorteada)//2)
    return palavra_sorteada, chances


def comecar(palavra_sorteada: str, chances: int) -> str:
    print(f'''
    ------- BEM VINDO(A) -------
    ESTE É O JOGO DA FORCA!!!


    ------- Regras -------
    Só será aceito uma
    letra por vez.


    A palavra que você deverá descobrir
    tem {len(palavra_sorteada)} letras.


    Você poderá errar até {chances} vezes.

    ''')


def solicitar_letra():
    letra = input('Digite uma letra: ')
    while not letra.isalpha():
        print('Cactere digitado não é uma letra.')
        letra = input('Por favor, digite uma LETRA: ')
    return letra


def lista_underline(palavra_sorteada: str) -> list:
    letras_descobertas = (len(palavra_sorteada)*"_ ").split(" ")[:-1]
    return letras_descobertas


def verificar_letra(palavra_sorteada: str, letra: str, letras_descobertas: list):
    for index, elemento in enumerate(palavra_sorteada):
        if (letra == elemento):
            letras_descobertas[index] = elemento
    pass


def limpar_tela():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    pass


def jogar():

    palavra_sorteada, chances = sortear_palavra()
    comecar(palavra_sorteada, chances)
    letras_descobertas = lista_underline(palavra_sorteada)

    # ganhou = False
    max_tentativas = len(palavra_sorteada) + chances

    for i in range(max_tentativas):
        # while (not ganhou):
        letra = solicitar_letra()
        if (letra in palavra_sorteada):
            limpar_tela()
            verificar_letra(palavra_sorteada, letra, letras_descobertas)
            print(f'{"".join(letras_descobertas)}\n')
            if ("".join(letras_descobertas) == palavra_sorteada):
                print(f'VOCÊ GANHOU!!!\n')
                # ganhou = True
        else:
            chances -= 1
            if (chances == 0):
                limpar_tela()
                print(f'\nVocê PERDEU!!!')
                print(f'\nPalavra era: {palavra_sorteada}\n')
                break
            else:
                limpar_tela()
                print(f'\n{"".join(letras_descobertas)}')
                print(f'\nVocê ainda tem {chances} tentativas.\n')

 # %%
jogar()
