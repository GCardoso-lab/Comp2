from models.Filme import Filme


class BaseFilmes:
    def __init__(self):
        self.filmes = []
        self.arquivo = None
        self.nome_arquivo = 'filmes.txt'

    def base_filmes(self):

        while True:
            try:
                print("\n\n === Base de Filmes === \n\n")
                print("1 - Incluir Filme")
                print("2 - Consultar Filme")
                print("3 - Sair")
                print("\n\n")

                opt = int(input("Escolha a opção desejada:"))

                if opt == 1:
                    self.incluir_filme()
                elif opt == 2:
                    self.consultar_filme()
                elif opt == 3:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Opção inválida")
        print("Você deixou a Base de Filmes.")

    def incluir_filme(self):
        self.filmes.clear()
        print(print("\n\n=== Inclusão de Filmes ===\n\n"))
        nome = input("Nome: ")
        ano = input("Ano: ")
        duracao = input("Duração em Minutos: ")
        genero = input("Gênero: ")
        faixa_etaria = input("Faixa Etária: ")
        filme = Filme(nome, ano, duracao, genero, faixa_etaria)

        while True:
            confirma = input("\n\n Confirma inclusão de Filme? (S/N)\n\n")
            if confirma == "S":
                if self.abre_arq_filmes('a'):
                    linha = f"{filme.get_nome()};{filme.get_ano()};{filme.get_duracao()};" \
                            f"{filme.get_genero()};{filme.get_faixa_etaria()}; \n"
                    self.escreve_arq_filmes(linha)
                    self.fecha_arq_filmes()
                    print("\nFilme incluído com sucesso.")
                    break
            elif confirma == "N":
                print("Inclusão Cancelada.")
                break
            else:
                print("Opção Inválida! Digite S ou N.")

    def consultar_filme(self):
        print("\n\n==== Consulta de Filmes ====\n\n")
        self.recuperar_filmes()
        i = 0
        for filme in self.filmes:
            i = i + 1
            print(i, " ", filme.get_nome())

        if i > 0:
            opt = int(input("\n\nInforme o numero do filme: "))
            if 1 <= opt <= i:
                filme = self.filmes.pop(opt - 1)
                print(filme)
            else:
                print("Numero inválido")

    def recuperar_filmes(self):
        self.filmes.clear()
        if self.abre_arq_filmes('r'):
            for line in self.arquivo:
                pos = pos_old = 0
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
                    ano = funci.pop(0)
                    duracao = funci.pop(0)
                    genero = funci.pop(0)
                    faixa_etaria = funci.pop(0)
                    filme = Filme(nome, ano, duracao, genero, faixa_etaria)
                    self.filmes.append(filme)
                except IndexError:
                    self.fecha_arq_filmes()
                    break
            self.fecha_arq_filmes()

    def update_filmes(self):
        if self.abre_arq_filmes('w'):
            for filme in self.filmes:
                linha = f"{filme.get_nome()};{filme.get_ano()};{filme.get_duracao()};" \
                        f"{filme.get_genero()};{filme.get_faixa_etaria()}; \n"
                self.escreve_arq_filmes(linha)
            self.fecha_arq_filmes()

    def abre_arq_filmes(self, tipo):
        try:
            self.arquivo = open(self.nome_arquivo, tipo)
            return True
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False

    def fecha_arq_filmes(self):
        try:
            self.arquivo.close()
            return True
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False

    def le_arq_filmes(self, linha):
        try:
            self.arquivo.read()
            return linha
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False

    def escreve_arq_filmes(self, linha):
        try:
            self.arquivo.write(linha)
            return True
        except IOError:
            print("Problemas para acessar a base de filmes!")
            return False