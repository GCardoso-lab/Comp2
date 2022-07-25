from models.BaseFilmes import BaseFilmes


class Sessao:
    def __init__(self, sala, horario, dublagem, tresd,):
        self.Sala = sala
        self.Horario = horario
        self.Dublagem = dublagem
        self.Tresd = tresd
        self.cadeiras_disponiveis = [range(1, 150, 1)]
        self.Filme = ''

    def get_sala(self):
        return self.Sala

    def get_horario(self):
        return self.Horario

    def get_dublagem(self):
        return self.Dublagem

    def get_tresd(self):
        return self.Tresd

    def get_filme(self):
        if self.Filme == '':
            print("Filme ainda não definido para esta sessão!")
        else:
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

    def escolhe_assento(self):
        """Escolha assentos entre 1 e 150"""
        print(f"Cadeiras disponíveis: {self.cadeiras_disponiveis}")
        opt = input("Digite aqui os assentos desejados, separados por vírgula: ")
        cadeiras_escolhidas = opt.split(",")
        for x in self.cadeiras_disponiveis:
            if x in cadeiras_escolhidas:
                self.cadeiras_disponiveis.remove(x)
        print("Cadeiras escolhidas!")

    def libera_assento(self, assento):
        self.cadeiras_disponiveis.insert(assento, assento-1)
        print("Assento liberado!")

    def bilhete(self):
        bilhete = [self.Filme.get_nome(), self.Filme.get_ano(), self.Sala, self.Horario, self.Dublagem,
                   self.Tresd]
        return bilhete
