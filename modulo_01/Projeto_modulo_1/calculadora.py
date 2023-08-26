"""
Descrição:

Crie um programa em Python que simule uma calculadora simples capaz de realizar operações de adição, subtração, multiplicação e divisão.
Funcionalidades:

Exibir um menu com as opções de operações disponíveis.
Permitir ao usuário escolher a operação desejada.
Solicitar ao usuário dois números para realizar a operação.
Exibir o resultado da operação na tela.
Requisitos:

O programa deve permitir ao usuário escolher a operação através de um menu com as seguintes opções:

Adição (+)
Subtração (-)
Multiplicação (*)
Divisão (/)
O programa deve receber dois números (operandos) digitados pelo usuário.

O programa deve realizar a operação escolhida pelo usuário e exibir o resultado na tela.

O programa deve repetir o processo até que o usuário decida sair da calculadora.

Caso o usuário escolha a operação de divisão (/), o programa deve verificar se o segundo número é zero e exibir uma mensagem de erro em caso afirmativo, informando que a divisão por zero não é permitida.

"""
def adicao(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        raise ValueError('Erro: divisão por zero não é permitida.')
    return numero1 / numero2

    

operacoes = {
    1: adicao,
    2: subtracao,
    3: multiplicacao,
    4: divisao,
}



while True:
    print('Digite o primeiro numero:')
    numero1 = int(input())
    print('Digite o segundo numero:')
    numero2 = int(input())

    print("----- MENU -------")
    print("Digite uma das opções")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    escolha = int(input())

    if escolha == 5:
        print("Saindo...")
        break

    if escolha not in operacoes:
        print("Opção inválida. Tente novamente.")
        continue

    try:
        resultado = operacoes[escolha](numero1, numero2)
        print(f'Resultado: {resultado}')
    except ValueError as error:
        print(error)