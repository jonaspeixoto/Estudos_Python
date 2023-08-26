"""
Desafio: Jogo da Forca

Neste desafio, você deve criar um jogo da forca simples em Python. O jogo deve seguir as seguintes regras:

O programa escolhe uma palavra aleatória de uma lista de palavras pré-definida.
O jogador tem um número limitado de tentativas (por exemplo, 6 tentativas) para adivinhar a palavra.
A cada tentativa, o programa mostra as letras adivinhadas corretamente e as letras que ainda não foram adivinhadas, representadas por "_".
O programa deve tratar exceções, como a entrada de caracteres inválidos (números, símbolos) e a entrada de mais de uma letra por tentativa.
Se o jogador adivinhar a palavra antes de acabarem as tentativas, ele vence o jogo. Caso contrário, ele perde.

"""

import random

def escolher_palavra(palavra):
    return random.choice(palavra)

def inicializar_esconder_palavra(palavra_adivinha):
    esconder_palavra = []
    for letra in palavra_adivinha:
        esconder_palavra.append('_')
    return esconder_palavra

def valida_entrada(entrada):
    entrada = entrada.lower()
    if len(entrada) == 1 and entrada.isalpha():
        return True
    return False

def verificar_tentativa(palavra_adivinha, esconder_palavra,tentativa, entrada):
    if entrada in palavra_adivinha:
        for indice, entrada_palavra in enumerate(palavra_adivinha):
            if entrada_palavra == entrada:
                esconder_palavra[indice] = entrada    

        print(palavra_adivinha)            
        print(esconder_palavra)            
        if palavra_adivinha == esconder_palavra:
            return True
        return False


def jogo_da_forca():

    palavras = ['banana', 'abacaxi', 'computador', 'elefante', 'girafa', 'alface', 'casa', 'carro', 'borboleta',
    'camiseta', 'escola', 'amarelo', 'janela', 'felicidade', 'telefone', 'violão', 'música', 'paralelepípedo', 'tigre',
    'abelha', 'cachorro', 'espelho', 'internet', 'chocolate', 'oceano', 'avião', 'inverno', 'primavera', 'outono', 'verão',
    'televisão', 'lua', 'estrela', 'floresta', 'arco-íris', 'piano']


    palavra_adivinha = escolher_palavra(palavras)
    print(palavra_adivinha)

    esconder_palavra = inicializar_esconder_palavra(palavra_adivinha)
    tentativa = 0
    max_tentativas  = 6

    while tentativa < max_tentativas:
        entrada = input('Digite uma entrada: ')
        if valida_entrada(entrada):
            tentativa += 1
            if verificar_tentativa(palavra_adivinha, esconder_palavra,tentativa, entrada ):
                print('Parabéns, você venceu!')
                break
        else: 
            print('Entrada invalida Por favor digite apenas uma letra de A a Z')

        print("".join(esconder_palavra))
        print(f'Você ainda tem {max_tentativas - tentativa} tentativas restantes.')

     
if __name__ == "__main__":
    jogo_da_forca()