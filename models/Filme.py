class Filme:
    def __init__(self, nome, ano, duracao, genero, faixa_etaria):
        self.Nome = nome
        self.Ano = ano
        self.Duracao = duracao
        self.Genero = genero
        self.FaixaEtaria = faixa_etaria

    def __str__(self):
        return f" Nome: {self.Nome} \n Ano: {self.Ano} \n Duração: " \
               f"{self.Duracao} \n Gênero: {self.Genero} \n Faixa etária: {self.FaixaEtaria}"

    def get_nome(self):
        return self.Nome

    def get_ano(self):
        return self.Ano

    def get_duracao(self):
        return self.Duracao

    def get_genero(self):
        return self.Genero

    def get_faixa_etaria(self):
        return self.FaixaEtaria
