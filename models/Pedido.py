from models.Produtos import Produto
from prettytable import PrettyTable
from numpy.random import randint


class Pedido:
    def __init__(self):
        self.produtos = []
        self.total = 0

    def realizar_pedido(self):
        cardapio = Produto("null", 0)
        while True:
            cardapio.recuperar_produtos()
            i = 0
            for produto in cardapio.produtos:
                i = i + 1
                print(i, " ", produto.get_nome())
            opt = int(input("Digite um número para adicionar um produto ao carrinho, ou 0 para fechar"
                            " o pedido: "))
            if 1 <= opt <= i:
                produto_escolhido = cardapio.produtos.pop(opt - 1)
                self.produtos.append(produto_escolhido)
                print("Produto adicionado!")
            elif opt == 0:
                total = 0
                for produto in self.produtos:
                    total = total + int(produto.get_preco())
                self.total = total
                print("Pedido Fechado!")
                break
            else:
                print("Resposta Inválida.")

    def imprimenota(self):
        for produto in self.produtos:
            print(f"{produto.get_nome()}:  {produto.get_preco()} R$")
        print(f'\n\nTotal da Nota: {self.total} R$')

    def pagar(self):
        print("\n\nEscolha um método de pagamento:\n\n[ 1 ] Boleto Bancário\n[ 2 ] Cartão de Crédito ou Débito\n\n")
        pagamento = int(input("Digite o número desejado: "))
        if pagamento == 1:
            print(f"Total a pagar: {self.total}")
            self.gerar_boleto()
        elif pagamento == 2:
            parcelar = input("Deseja parcelar em até 3x sem juros? (S/N)")
            if parcelar == "N":
                print(f"Total a pagar: {self.total}")
                numero = input("Informe o número do seu cartão de crédito (apenas números, sem espaço): ")
                validade = input("Informe a data de expiração do cartão: (formato DD/MM/AA)")
                cvv = input("Informe o código de verificação de 3 dígitos: ")
                self.pagar_cartao(numero, validade, cvv)
            elif parcelar == "S":
                while True:
                    numero_parcelas = int(input("Digite o número de vezes que deseja parcelar:"))
                    if 1 <= numero_parcelas <= 3:
                        print(f"Total a pagar: {self.total}/{numero_parcelas} durante {numero_parcelas} meses.\n\n")
                        numero = input("Informe o número do seu cartão de crédito (apenas números, sem espaço): ")
                        validade = input("Informe a data de expiração do cartão (formato DD/MM/AA): ")
                        cvv = input("Informe o código de verificação de 3 dígitos: ")
                        self.pagar_cartao(numero, validade, cvv)
                        break
                    else:
                        print("Número inválido! Escolha um valor de 1 à 3.")

    def gerar_boleto(self):
        boleto = PrettyTable()
        boleto.field_names = ["Produto", "Preço"]
        for produto in self.produtos:
            print(produto.get_nome())
            print(produto.get_preco())
            boleto.add_row([produto.get_nome(), produto.get_preco()])
        boleto.add_row(["TOTAL:", f"{self.total} RS$"])
        boleto.add_row(["CÓDIGO DO BOLETO:", randint(100000000, 999999999, 1)])
        print(boleto)

    def pagar_cartao(self, numero, validade, cvv):
        print(f"{numero}, {validade}, {cvv}")
        print("funcao em desenvolvimento.")
