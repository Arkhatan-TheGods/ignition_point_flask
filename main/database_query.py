def create_table_costumer() -> str:
    query = """
    CREATE TABLE IF NOT EXISTS CLIENTE(
    ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
    NOME TEXT NOT NULL, 
    CPF TEXT NOT NULL UNIQUE, 
    DATA_NASCIMENTO TEXT NOT NULL, 
    ENDERECO TEXT NOT NULL
    );"""
    return query


def new_costumer() -> str:
    query = """
    INSERT INTO CLIENTE(NOME,CPF,DATA_NASCIMENTO,ENDERECO)
    VALUES(:nome, :cpf, :dt_nasc, :endereco);"""
    return query


def find_costumer_by_id() -> str:
    query = "SELECT * FROM CLIENTE WHERE ID = :id ;"
    return query

def update_costumer() -> str:
    query = """UPDATE CLIENTE 
    SET NOME = :nome, 
    CPF = :cpf, 
    DATA_NASCIMENTO = :dt_nasc, 
    ENDERECO = :end 
    WHERE ID = :id ;"""
    return query

def delete_costumer() -> str:
    query = "DELETE CLIENTE WHERE ID = :id ;"
    return query

def all_costumer() -> str:
    return "SELECT * FROM CLIENTE;"