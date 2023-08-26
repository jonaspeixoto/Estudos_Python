
contatos = {'jonas': {'telefone': '848484', 'email': 'jonas@example.com'},
            'karol': {'telefone': '4541654165', 'email': 'karol@example.com'}}

def adicionar_contato(nome, telefone, email):
    contatos[nome] = {'telefone':telefone, 'email':email}
    print('Contato adicionado com sucesso!')

def visualizar_contatos():
    for contato, info in contatos.items():
        print(f'Nome: {contato}, Telefone: {info["telefone"]}, E-mail: {info["email"]}')
    print()

def buscar_contato(nome):
    return contatos.get(nome.lower(), 'Contato não existe')


print('Opções:')
print('1 - Adicionar contato:')
print('2 - Visualizar contatos:')
print('3 - Buscar contato:')
print('4 - Sair:')

print(contatos.items())
while(True):
    opcao = input('Escolha uma opção:')
    if opcao == '1':
        nome = input('Nome: ')
        telefone = input('telefone: ')
        email = input('email: ')

        adicionar_contato(nome, telefone, email)
    
    elif opcao == '2':
        visualizar_contatos()

    elif opcao == '3':
        nome = input('Digite o nome do contato dejesado: ')
        print(buscar_contato(nome))
    elif opcao == '4':
        print("Até logo!")
        break
    
