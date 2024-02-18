import os

restaurantes = [{'nome': 'Praça', 'categoria': 'Japonesa', 'ativo':False}, 
                {'nome': 'Fritz', 'categoria': 'Fastfood', 'ativo':True}, 
                {'nome': 'CAKES', 'categoria': 'bolo', 'ativo':True}]

def exibir_nome_do_programa():

    '''Esssa função exibi o nome do programa. '''

    print(""" 
███████╗░█████╗░███╗░░░███╗███████╗  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗████╗░████║██╔════╝  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░██║░░██║██╔████╔██║█████╗░░  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
██╔══╝░░██║░░██║██║╚██╔╝██║██╔══╝░░  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██║░░░░░╚█████╔╝██║░╚═╝░██║███████╗  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═╝░░░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():

    '''Esssa função exibi as opções disponíveis. '''

    print("1. Cadastrar Restaurant")
    print("2. Listar Restaurante ")
    print("3. Alterar estado do  Restaurante ")
    print("4. Sair ")

def finalizar_app():

    '''Esssa função executa o encerramento do APP. '''

    exibir_subtitulo('Finalizando o app')
    
def voltar_menu_principal():

    '''Esssa função executa o retorno ao menu principal. '''

    input('\nDigite uma tecla para voltar ao menu princiapl !')
    main()

def opcao_invalida():

    '''Esssa função retorna a mensagem de opçao invalida quando o usuario escolhe uma opção inexistente. '''

    print('Opção inválida!\n')
    voltar_menu_principal()
    
def exibir_subtitulo(texto):

    '''Esssa função exibi o subtitulo. '''

    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():

    '''Esssa função executa o cadastro de novos restaurantes. '''

    exibir_subtitulo('Cadastro de novos restaurantes.')
    nome_do_restaurante = input('Digite o nome do restaunte que  gostaria cadastrar:')

    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}:')

    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    
    restaurantes.append(dados_do_restaurante)

    exibir_subtitulo(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_menu_principal()

def listar_restaurantes():
    '''Esssa função executa a listagem de restaurantes. '''
    exibir_subtitulo('Listando os restaurantes:')
    
    print(f'{'Nome do restaurante:'.ljust(22)} | {'Categoria:'.ljust(20)} | {'Status:'}  ')

    for restaunte in restaurantes:
        nome_restaurante = restaunte['nome']
        categoria = restaunte['categoria']
        ativo = 'ativado' if restaunte['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    voltar_menu_principal()

def alterar_estado_restaurante():
    '''Esssa função executa a alteração de estado do restaurante. '''
    

    exibir_subtitulo('Alterar estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurantes_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurantes_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restauten {nome_restaurante} foi desativado com sucesso.'
            print(mensagem)
            
    if not restaurantes_encontrado:
        print('O restaurante não foi encontrado')
    voltar_menu_principal()

def escolher_opcao():
    '''Esssa função executa a função escolhida. '''

    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
                
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alterar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()
            
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
    