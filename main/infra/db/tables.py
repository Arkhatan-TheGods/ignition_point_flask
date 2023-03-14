from sqlite3 import Connection, connect

def build_tables(data_base: str):

    conn: Connection | None = None

    try:
        conn = connect(data_base)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS CLIENTE(
            ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
            NOME TEXT NOT NULL, 
            CPF TEXT NOT NULL UNIQUE, 
            DATA_NASCIMENTO TEXT NOT NULL, 
            ENDERECO TEXT NOT NULL
            );""")

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()
