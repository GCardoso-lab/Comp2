from models.Filme import Filme
import requests
from bs4 import BeautifulSoup
from translate import Translator


class BaseFilmes:
    def __init__(self):
        self.filmes = []
        self.arquivo = None
        self.nome_arquivo = 'filmes.txt'

    def base_filmes(self):
        while True:
            try:
                print("\n\n === Base de Filmes === \n\n")
                print("1 - Incluir Filme Manualmente")
                print("2 - Incluir Filme com Link IMDB")
                print("3 - Consultar Filme")
                print("4 - Excluir Filme")
                print("5 - Sair")
                print("\n\n")

                opt = int(input("Escolha a opção desejada:"))

                if opt == 1:
                    self.incluir_filme()
                elif opt == 2:
                    self.incluir_imdb()
                elif opt == 3:
                    self.consultar_filme()
                elif opt == 4:
                    self.exclui_filme()
                elif opt == 5:
                    break
                else:
                    print("Opção inválida")
            except ValueError:
                print("Opção inválida")
        print("Você deixou a Base de Filmes.")

    def incluir_filme(self):
        self.filmes.clear()
        print("\n\n=== Inclusão de Filmes ===\n\n")
        nome = input("Nome: ")
        ano = input("Ano: ")
        duracao = input("Duração em Minutos: ")
        genero = input("Gênero: ")
        faixa_etaria = input("Faixa Etária: ")
        filme = Filme(nome, ano, duracao, genero, faixa_etaria)

        self.confirma_inclusao(filme)

    def incluir_imdb(self):
        self.filmes.clear()
        print("\n\n=== Inclusão de Filmes via IMDB ===\n\n")
        link = input("Cole aqui o link do filme no IMDB:")
        pagina = requests.get(link).text
        soup = BeautifulSoup(pagina, "lxml")
        nome = soup.find("h1", attrs={"data-testid": "hero-title-block__title"}).text
        anofaixa = soup.find_all("span", attrs={"class": "sc-8c396aa2-2 itZqyK"})
        ano = anofaixa[0].text
        faixa_etaria = anofaixa[1].text
        listaduracao = soup.findAll("li", attrs={"class": "ipc-inline-list__item"})
        duracao = listaduracao[5].text
        gender = listaduracao[6].text
        tradutor = Translator(to_lang="pt")
        genero = tradutor.translate(gender)
        filme = Filme(nome, ano, duracao, genero, faixa_etaria)

        self.confirma_inclusao(filme)

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

    def confirma_inclusao(self, filme):
        print(f"\n\n          Filme: {filme.get_nome()}, {filme.get_ano()}")
        while True:
            confirma = input("\n\nConfirma inclusão de Filme? (S/N)\n\n")
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

    def exclui_filme(self):
        print("\n\n==== Exclusão de Filmes ====\n\n")
        self.recuperar_filmes()
        i = 0
        for filme in self.filmes:
            i = i + 1
            print(i, " ", filme.get_nome())

        if i > 0:
            opt = int(input("\n\nInforme o numero do filme: "))
            if 1 <= opt <= i:
                filme = self.filmes.pop(opt - 1)
                if self.abre_arq_filmes('r'):
                    linhas = self.arquivo.readlines()
                    self.fecha_arq_filmes()
                    while True:
                        confirmacao = input(f"\n\nCerteza que deseja excluir o filme {filme.get_nome()} ? S/N\n")
                        if confirmacao == "S":
                            if self.abre_arq_filmes('w'):
                                for linha in linhas:
                                    if linha.strip("\n") != f"{filme.get_nome()};{filme.get_ano()};{filme.get_duracao()};" \
                                                            f"{filme.get_genero()};{filme.get_faixa_etaria()}; ":
                                        self.escreve_arq_filmes(linha)
                            self.fecha_arq_filmes()
                            print("\n\nFilme excluído.")
                            break
                        elif confirmacao == "N":
                            print("\n\nExclusão cancelada.")
                            break
                        else:
                            print("\n\nResposta inválida! Digite S ou N.")