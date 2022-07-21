from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


class Cliente:
    def __init__(self, id, nome, cpf, data_de_nascimento, email, login, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.login = login
        self.senha = senha

    def permissao_filme(self, filme):
        data = dt.strptime(self.data_de_nascimento, "%d/%m/%Y")
        now = dt.now()
        c = relativedelta(now, data)
        idade = c.years
        if idade < filme.FaixaEtaria:
            return False
        else:
            return True

    def create_usuario(self):
        pass
    
    def get_usuario(self):
        pass

    def delete_usuario(self):
        pass
