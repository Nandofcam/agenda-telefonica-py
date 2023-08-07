agenda = {}

def adicionarContato(nome: str, telefone: str) -> None:
    agenda[nome] = telefone
    print('Contato adicionado com sucesso!')

def editarContato(nome: str, telefone: str) -> None:
    if nome in agenda.keys():
        agenda[nome] = telefone
        print('Dados alterados com sucesso!')
    else:
        print('O contato não está cadastrado!')

def pesquisarContato(nome: str) -> None:
    if nome in agenda.keys():
        print('------------------')
        print(f'\nContato: {nome}')
        print(f'Telefone: {agenda[nome]}')
        print('\n ------------------')
    else:
        print('Contato não encontrado!')

def deletarContato(nome: str) -> None:
    if nome in agenda.keys():
        del agenda[nome]
        print('Contato removido com sucesso!')
    else:
        print('Contato não encontrado!')

def listarTodos():
    for nome in agenda:
        print('--------------')
        print(f'\nContato: {nome}')
        print(f'Telefone: {agenda[nome]}')
        print('\n--------------')

while True:
    print("------ Bem vindo ao Menu ------")
    opcao = int(input('1 - Adicionar contato \n'
                      '2 - Editar contato \n'
                      '3 - Pesquisar contato \n'
                      '4 - Deletar contato \n'
                      '5 - Listar todos \n'
                      '6 - Sair \n'
                      'Selecione uma opção: '))
    if opcao == 1:
        nome = input('Insira o nome do contato que deseja adicionar: ')
        tel = input('Insira o número do contato, com DDD: ')
        adicionarContato(nome, tel)
    elif opcao == 2:
        nome = input('Digite o nome do contato que você deseja alterar: ')
        tel = input('Digite o novo telefone: ')
        editarContato(nome, tel)
    elif opcao == 3:
        nome = input('Insira o nome de contato que deseja pesquisar: ')
        pesquisarContato(nome)
    elif opcao == 4:
        nome = input('Digite o nome do contato: ')
        deletarContato(nome)
    elif opcao == 5:
        listarTodos()
    elif opcao == 6:
        break
    else:
        print('Opção inválida!')
