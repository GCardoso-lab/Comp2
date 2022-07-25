from models.BaseFilmes import BaseFilmes
class Sessao:
    def __init__(self, sala, horario, dublagem, tresd, cadeiras_disponiveis):
        self.Sala = sala
        self.Horario = horario
        self.Dublagem = dublagem
        self.Tresd = tresd
        self.cadeiras_disponiveis = [range(1,150,1)]
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

    def escolheAssento(self, assento):
        """Escolha assentos entre 1 e 150"""
        cadeiras_disponíveis = [range(1,150,1)]
        cadeiras_escolhidas = [assento]
        for x in self.cadeiras_disponiveis:
            if x in cadeiras_escolhidas:
                self.cadeiras_disponiveis.remove(x)
        return self.cadeiras_disponiveis

    def cancelaAssento(self, assento):
        self.cadeiras_disponiveis.add(x)
        cadeiras_escolhidas.remove(x)
        return self.cadeiras_disponiveis
        

    def Bilhete(self):
        bilhete = list(self.Nome, self.Ano, self.Duracao, self.Genero, self.FaixaEtaria,
                       self.Horario, self.Sala, self.Dubleg, self.Dimensao, self.Bilhete)
        return bilhete
