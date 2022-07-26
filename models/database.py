import sqlite3

def ExecuteQueryOperator(query):
    con = sqlite3.connect("./data.db")
    cur = con.cursor()

    try:
        cur.execute(query)
    except:
        print("Ocorreu um erro ao executar a query enviada.")
    finally:
        con.commit()
        con.close()

    return None
