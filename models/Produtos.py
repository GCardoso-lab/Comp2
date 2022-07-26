class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco
        self.arquivo = None
        self.nome_arquivo = 'produtos.txt'
        self.produtos=[]
        
    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco

    def abre_arq_produtos(self, tipo):
        try:
            self.arquivo = open(self.nome_arquivo, tipo)
            return True
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False

    def fecha_arq_produtos(self):
        try:
            self.arquivo.close()
            return True
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False

    def le_arq_produtos(self, linha):
        try:
            self.arquivo.read()
            return linha
        except IOError:
            print("Problemas para acessar a base de produtos!")
            return False

    def escreve_arq_produtos(self, linha):
        try:
            self.arquivo.write(linha)
            return True
        except IOError:
            print("Problemas para acessar a base de produtos!")
            return False

    def recuperar_produtos(self):
        self.produtos.clear()
        if self.abre_arq_produtos('r'):
            for line in self.arquivo:
                pos_old = 0
                funci = []
                while True:
                    try:
                        pos = line.index(";", pos_old)
                        funci.append(line[pos_old:pos])
                        pos_old = pos + 1
                    except ValueError:
                        break

                try:
                    nome = funci.pop(0)
                    preco = funci.pop(0)
                    produto = Produto(nome, preco)
                    self.produtos.append(produto)
                except IndexError:
                    self.fecha_arq_produtos()
                    break
            self.fecha_arq_produtos()

    def registrar_produto(self):
        print(f"\n\n          Produto: {self.nome}, {self.preco} R$")
        while True:
            confirma = input("\n\nConfirma inclusão de Produto? (S/N)\n\n")
            if confirma == "S":
                if self.abre_arq_produtos('a'):
                    linha = f"{self.nome};{self.preco}; \n"
                    self.escreve_arq_produtos(linha)
                    self.fecha_arq_produtos()
                    print("\nProduto incluído com sucesso.")
                    break
            elif confirma == "N":
                print("Inclusão Cancelada.")
                break
            else:
                print("Opção Inválida! Digite S ou N.")