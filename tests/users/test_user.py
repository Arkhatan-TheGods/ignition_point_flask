from pytest import fixture
from main.decorators.user_decorator import unit_of_work
from main.wire import users_controller
from sqlite3 import Connection, connect

def create_tables(data_base: str):

    conn: Connection | None = None
    response: dict = {}

    try:
        conn = connect(data_base)

        conn.cursor().executescript("""CREATE TABLE IF NOT EXISTS USERS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        NAME TEXT NOT NULL,
        BIRTH_DATE TEXT NOT NULL,
        EMAIL TEXT NOT NULL,
        ADDRESS TEXT NOT NULL,
        CREATED_ON DATETIME DEFAULT CURRENT_TIMESTAMP);""")

    except Exception as ex:
        print("Erro:", ex)

    finally:
        if conn:
            conn.close()
        return response



@fixture
def setup() -> tuple:

    return "Pietro Daniel Cardoso", \
        "06/03/1991", \
        "pietro-cardoso94@lins.net.br", \
        "Rua Ivan Marrocos, 818"

def test_create_user(setup) -> None:

    fn_controller = users_controller(unit_of_work(":memory",
                                                  enviroment="test"))
    
    response: dict = fn_controller["create"](setup)

    assert {'message': 'Usuário cadastrado com sucesso'} == response
