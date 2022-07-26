# Import's
import sqlite3
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta


def ExecuteQueryOperator(query):
    con = sqlite3.connect("./data.db")
    cur = con.cursor()

    try:
        cur.execute(query)
    except Exception as e:
        raise e
    finally:
        con.commit()
        con.close()

    return None


# Classe
class Cliente:
    def __init__(self, nome, cpf, data_de_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento

        try:
            print("Instânciando tabelas no banco de dados...")
            ExecuteQueryOperator('''
                CREATE TABLE IF NOT EXISTS clients
                    (id INTEGER PRIMARY KEY, nome TEXT, cpf TEXT, data_de_nascimento TEXT)
            ''')
            print("Tabela instânciada com sucesso!")
        except:
            raise Exception("Ocorreu um erro ao instânciar a tabela no banco de dados.")
            

    def __main__():
        print("Olá mundo!")


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
        try:
            con = sqlite3.connect("./data.db")
            cur = con.cursor()

            dados = (self.nome, self.cpf, self.data_de_nascimento)

            try:
                cur.execute('''
                INSERT INTO clients (nome, cpf, data_de_nascimento) VALUES (?, ?, ?)
            ''', dados)
            except Exception as e:
                raise e
            finally:
                con.commit()
                con.close()
        except Exception as e:
            raise Exception("Ocorreu um erro no momento da criação do usuário..", e)
        
    
    def get_usuario(self):
        try:
            con = sqlite3.connect("./data.db")
            cur = con.cursor()

            try:
                result = cur.execute('''
                    SELECT * FROM clients WHERE cpf = %s
                ''' % self.cpf)

                for row in result:
                    return row
                return 0

            except Exception as e:
                raise e
            finally:
                con.commit()
                con.close()
        except Exception as e:
            raise Exception("Ocorreu um erro da seleção do usuário..", e)

    def delete_usuario(self):
        try:
            con = sqlite3.connect("./data.db")
            cur = con.cursor()

            try:
                cur.execute('''
                    DELETE FROM clients WHERE cpf = %s
                ''' % self.cpf)

                print("Usuário deletado com sucesso.")
                return 0
            except Exception as e:
                raise e
            finally:
                con.commit()
                con.close()
        except Exception as e:
            raise Exception("Ocorreu um erro ao deletar o usuário..", e)
