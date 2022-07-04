from datetime import datetime as dt

class Cliente():
    def __init__(self, id, nome, cpf, data_de_nascimento, email, login, senha):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento
        self.email = email
        self.login = login
        self.senha = senha

    def permissaoFilme(data_de_nascimento, classificacao_do_filme):
        data = dt.strptime(data_de_nascimento, "%d/%m/%Y")
        now = datetime.now()

        c = now - data

        if c < classificacao_do_filme:
            return False
        else:
            return True

    def createUsuario(nome, cpf, data_de_nascimento, email, login, senha):
        pass
    
    def getUsuario(login, senha):
        pass

    def deleteUsuario(login, senha):
        pass