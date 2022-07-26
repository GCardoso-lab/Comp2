# Importações
import os
import sys 

# Modelos
from models.BaseFilmes import BaseFilmes
from models.Cliente import Cliente
from models.Filme import Filme
from models.Pedido import Pedido
from models.Produtos import Produto
from models.Sessao import Sessao


# Lambda's
clear = lambda: os.system('clear')

# Opções do menu
menu_options = {
    1: "BaseFilmes",
    2: "Clientes",
    3: "Filmes",
    4: "Pedidos",
    5: "Produtos",
    6: "Sessão",
    7: "Sair"
}


# Interfaces do terminal
def interface_client(client_option):
    if client_option == 1:
        clear()
        print("---------------------------------------------")
        print("    CineUFRJ - Administração de Clientes.    ")
        print("---------------------------------------------")
        print("             Cadastro de usuário             ")
        print("---------------------------------------------")
        print("\n")

        nome = input("Nome completo: ")
        cpf = input("CPF: ")
        data_de_nascimento = input("Data de nascimento: ")

        try:
            cliente = Cliente(nome, cpf, data_de_nascimento)
            cliente.create_usuario()
            return 0
        except:
            return 1
    elif client_option == 2:
        clear()
        print("---------------------------------------------")
        print("    CineUFRJ - Administração de Clientes.    ")
        print("---------------------------------------------")
        print("               Deletar cliente               ")
        print("---------------------------------------------")
        print("\n")
        deletar_cpf = input("Insira o CPF do cliente: ")

        try:
            cliente = Cliente(None, deletar_cpf, None)
            cliente.delete_usuario()
            return 0
        except:
            return 1
    elif client_option == 3:
        return 3

def interface_main():
    if option == 1:
        clear()
        _bfilmes = BaseFilmes()
        _bfilmes.base_filmes()
        clear()
    elif option == 2:
        clear()
        print("---------------------------------------------")
        print("    CineUFRJ - Administração de Clientes.    ")
        print("---------------------------------------------")
        print(" Selecione a opção que deseja seguir no menu ")
        print("---------------------------------------------")
        print("1 - Registrar")
        print("2 - Deletar")
        print("3 - Retornar")
        print("\n")

        while (True):
            try:
                client_option = int(input("Opção selecionada: "))
            except:
                print("Não foi possível identificar a opção desejada, tente novamente...")
                continue;

            response = interface_client(client_option)
            if response == 0:
                clear()
                print("[SUCESSO] Operação ocorreu com sucesso.")
                break
            elif response == 1:
                clear()
                print("[ERRO] Ocorreu algum problema durante a operação.")
                break
            elif response == 3:
                clear()
                print("[AVISO] Retornando ao menu principal.")
                break
    elif option == 3:
        pass
    elif option == 4:
        pass
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:
        print("[CineUFRJ] Saindo do programa...")
        sys.exit()


# Mainframe da aplicação
while (True):
    print("---------------------------------------------")
    print("            Bem vind@ ao CineUFRJ.           ")
    print("---------------------------------------------")
    print("Selecione a opção que deseja seguir no menu: ")

    for key in menu_options.keys():
        print(key, "--", menu_options[key])

    try:
        option = int(input("Insira o número da opção: "))
    except:
        clear()
        print("\n")
        print("[AVISO] Ocorreu um erro no momento de verificar sua escolha anterior, tente novamente..")
        continue;

    interface_main()
