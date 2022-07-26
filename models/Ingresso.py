import sqlite3


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


class Ingresso:
    def __init__(self, user_cpf, sessao_id, nome_filme, data_filme, row, seat):
        self.user_cpf = user_cpf
        self.sessao_id = sessao_id
        self.nome_filme = nome_filme
        self.data_filme = data_filme
        self.row = row
        self.seat = seat

        try:
            print("Instânciando tabelas no banco de dados...")
            ExecuteQueryOperator('''
                CREATE TABLE IF NOT EXISTS tickets
                    (id INTEGER PRIMARY KEY, user_cpf TEXT, sessao_id TEXT, nome_filme TEXT, data_filme TEXT,
                     row TEXT, seat TEXT)
            ''')
            print("Tabela instânciada com sucesso!")
        except:
            raise Exception("Ocorreu um erro ao instânciar a tabela no banco de dados.")

    def buy_ticket(self):
        try:
            con = sqlite3.connect("./data.db")
            cur = con.cursor()

            dados = (self.user_cpf, self.sessao_id, self.nome_filme, self.data_filme, self.row, self.seat)

            try:
                cur.execute('''INSERT INTO tickets 
                    (user_cpf, sessao_id, nome_filme, data_filme, row, seat) VALUES (?,?,?,?,?,?)''', dados)
            except Exception as e:
                raise e
            finally:
                con.commit()
                con.close()
        except:
            raise Exception("Ocorreu um erro ao comprar o ticket..", e)

    def get_ticket(self):
        try:
            con = sqlite3.connect("./data.db")
            cur = con.cursor()

            try:
                result = cur.execute('''
                    SELECT * FROM tickets WHERE user_cpf = %s
                ''' % self.user_cpf)

                lista_de_ingressos = []

                for row in result:
                    lista_de_ingressos.append(row)
                return 0
            except Exception as e:
                raise e
            finally:
                con.commit()
                con.close()
        except Exception as e:
            raise Exception("Ocorreu um erro da seleção do ingresso..", e)


sessao = Ingresso("18188846740", "0001", "007 - Pronto para matar", "01/01/2022 19:30", "A", "15")
