# Importações
import os
import sys 
import time

# Modelos
from models.BaseFilmes import BaseFilmes
from models.Cliente import Cliente
from models.Filme import Filme
from models.Pedido import Pedido
from models.Produtos import Produto
from models.Sessao import Sessao
from models.Ingresso import Ingresso


# Lambda's
clear = lambda: os.system('clear')

# Opções do menu
menu_options = {
    0: "Ingresso.com",
    1: "BaseFilmes",
    2: "Clientes",
    3: "Pedidos",
    4: "Produtos",
    5: "Sair"
}


# Interfaces do terminal
def interface_client(client_option):
    if client_option == 0:
        clear()
        print("---------------------------------------------")
        print("    CineUFRJ - Administração de Clientes.    ")
        print("---------------------------------------------")
        print("            Consultar de usuário             ")
        print("---------------------------------------------")
        print("\n")

        get_cpf = input("CPF: ")

        try:
            cliente = Cliente(None, get_cpf, None)
            dados_cliente = cliente.get_usuario()
            clear()
            print("---------------------------------------------")
            print("    CineUFRJ - Administração de Clientes.    ")
            print("---------------------------------------------")
            print("             Consulta de usuário             ")
            print("---------------------------------------------")
            if dados_cliente == 0:
                print("Nenhum usuário encontrado com esse CPF.")
            else:
                print("Nome:", dados_cliente[1])
                print("CPF: ", dados_cliente[2])
                print("Data de nascimento: ", dados_cliente[3])
            print("---------------------------------------------")
            
            time.sleep(5)
            return 0
        except Exception as e:
            return 1
    elif client_option == 1:
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
    if option == 0:
        clear()
        print("---------------------------------------------")
        print("           CineUFRJ - Ingresso.com           ")
        print("---------------------------------------------")
        print(" Digite o número do CPF do cliente:          ")
        print("---------------------------------------------")
        compras_cpf = input("CPF: ")

        cliente = Cliente(None, compras_cpf, None)
        dados_cliente = cliente.get_usuario()
        if dados_cliente == 0:
            clear()
            print("---------------------------------------------")
            print("           CineUFRJ - Ingresso.com           ")
            print("---------------------------------------------")
            print(f" Cliente não localizado :(                  ")
            print("---------------------------------------------")
            time.sleep(4)
            clear()
            return 1

        cliente = Cliente(dados_cliente[1], dados_cliente[2], dados_cliente[3])

        lista_de_sessoes = [
            {
                "sessao_id": "27020404",
                "nome_do_filme": "007 - Sem tempo para morrer",
                "data_do_filme": "26/07/2022 - 15:10"
            }
        ]

        clear()
        print("------------------------------------------------------------------------")
        print("                       CineUFRJ - Ingresso.com                          ")
        print("------------------------------------------------------------------------")
        print(f" Cliente: {cliente.nome}                                               ")
        print("------------------------------------------------------------------------")
        for sessao in lista_de_sessoes:
            print(f"[{lista_de_sessoes.index(sessao)}] Filme: {sessao['nome_do_filme']}    -   {sessao['data_do_filme']} ")
        print("\n")

        sessao_id = int(input("Digite o número da sessão desejada: "))
        row = input("Digite a letra da fileira desejada: ")
        seat = input("Digite o número do assento desejado: ")
        dados_sessao = lista_de_sessoes[sessao_id]

        print(dados_sessao)

        ingresso = Ingresso(cliente.cpf, dados_sessao['sessao_id'], dados_sessao['nome_do_filme'], dados_sessao['data_do_filme'], row, seat)
        
        try:
            ingresso.buy_ticket()
            clear()
            print("------------------------------------------------------------------------")
            print("                       CineUFRJ - Ingresso.com                          ")
            print("------------------------------------------------------------------------")
            print("                   Compra realizada com sucesso! :)                     ")
            print("------------------------------------------------------------------------")
            print(f" Cliente: {cliente.nome}                                               ")
            print("------------------------------------------------------------------------")
            print(f" Filme: {dados_sessao['nome_do_filme']} - {dados_sessao['sessao_id']}  ")
            print(f" Data: {dados_sessao['data_do_filme']}                                 ")
            print(f" Assento: {seat} / {row}")
            time.sleep(7)
            clear()
            return 0
        except Exception as e:
            return 1

    elif option == 1:
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
        print("0 - Consultar")
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
