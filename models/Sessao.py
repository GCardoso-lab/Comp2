from models.BaseFilmes import BaseFilmes
class Sessao:
    def __init__(self, sala, horario, dublagem, tresd):
        self.Sala = sala
        self.Horario = horario
        self.Dublagem = dublagem
        self.Tresd = tresd
        self.sessoes = []
        self.arquivo = None
        self.nome_arquivo = 'sessoes.txt'

    def get_sala(self):
        return self.Sala

    def get_horario(self):
        return self.Horario

    def get_dublagem(self):
        return self.Dublagem

    def get_tresd(self):
        return self.Tresd

    def get_filme(self):
        return f"{self.Filme.get_nome()} | {self.Filme.get_ano()} | {self.Filme.get_duracao()}"

    def adicionar_filme(self):
        funcao = BaseFilmes()
        BaseFilmes.recuperar_filmes(funcao)
        print("\n\n === Criar sessão === \n\n")
        print("\n\nSelecione o filme para ser exibido na sessão: \n\n")
        i = 0
        for filme in funcao.filmes:
            i = i + 1
            print(i, " ", filme.get_nome())
        opt = int(input("Escolha a opç5ão desejada:"))
        filmeopt = funcao.filmes[opt-1]
        self.Filme = filmeopt
