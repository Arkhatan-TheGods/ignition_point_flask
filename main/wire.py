from typing import Callable, Any
from sqlite3 import Connection

# IoC - Inversion of Control

def users_controller(unit_of_work:Callable) -> dict:

    @unit_of_work
    def create_user(*args: tuple, **kwargs: Any) -> dict:

        notifier: dict = {}
        conn: Connection = kwargs.get("conn", None)

        cursor = conn.cursor()
        try:
            cursor.execute("""INSERT INTO USERS(NAME, BIRTH_DATE, EMAIL, ADDRESS) 
            VALUES($NAME, $BIRTH_DATE, $EMAIL, $ADDRESS)""", args[0])

        except Exception as ex:
            notifier = {"erro": ex}
        else:
            conn.commit()

        finally:
            cursor.close()

            if {} != notifier:
                raise Exception(notifier)

        return {"message": f"Usuário cadastrado com sucesso"}

    return {"create":create_user}