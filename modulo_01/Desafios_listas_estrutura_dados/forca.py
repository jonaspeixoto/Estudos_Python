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

def valida_entrada(entrada):
    entrada = entrada.lower()
    if len(entrada) == 1 and entrada.isalpha():
        return True
    return False




palavras = ['banana', 'abacaxi', 'computador', 'elefante', 'girafa', 'alface', 'casa', 'carro', 'borboleta',
'camiseta', 'escola', 'amarelo', 'janela', 'felicidade', 'telefone', 'violão', 'música', 'paralelepípedo', 'tigre',
'abelha', 'cachorro', 'espelho', 'internet', 'chocolate', 'oceano', 'avião', 'inverno', 'primavera', 'outono', 'verão',
'televisão', 'lua', 'estrela', 'floresta', 'arco-íris', 'piano']


palavra_adivinha = list(random.choice(palavras))
print(palavra_adivinha)
guarda_palavras = []
tentativa = 0
tentativas_restantes = 6

for letra in palavra_adivinha:
    guarda_palavras.append('_')


while tentativa < 6:
    entrada = input('Digite uma entrada: ')
    if valida_entrada(entrada):
        tentativa += 1
        tentativas_restantes -=1
        if entrada in palavra_adivinha:
            for indice, entrada_palavra in enumerate(palavra_adivinha):
                if entrada_palavra == entrada:
                    guarda_palavras[indice] = entrada                
        if palavra_adivinha == guarda_palavras:
            print('Ganhou')
            break
    else: 
        print('Entrada invalida Por favor digite apenas uma letra de A a Z')
    print(guarda_palavras)
    print(f'voce ainda tem {tentativas_restantes} tentativas')



    