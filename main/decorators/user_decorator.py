from typing import Callable, Any
from sqlite3 import Connection, connect

def unit_of_work(data_base: str, enviroment:str) -> Callable:

    def decorator(func: Callable) -> Callable:

        def close_connection(conn: Connection | None):
            if conn:
                conn.rollback()

        def wrapper(*args: tuple, **kwargs: dict) -> Any:

            conn: Connection | None = None
            response: dict = {}

            try:
                conn = connect(data_base)

            except Exception as ex:
                print("Erro:", ex)
                response.update({"code": 500})
                close_connection(conn)
            else:
                try:
                    cursor = conn.cursor()
                    
                    if "TEST" == enviroment.upper():
                        cursor.executescript("""
                        BEGIN;
                        CREATE TABLE IF NOT EXISTS USERS (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        NAME TEXT NOT NULL,
                        BIRTH_DATE TEXT NOT NULL,
                        EMAIL TEXT NOT NULL,
                        ADDRESS TEXT NOT NULL,
                        CREATED_ON DATETIME DEFAULT CURRENT_TIMESTAMP);
                        COMMIT;
                        """)
                    
                    cursor.close()

                    response: dict = func(*args, conn=conn, **kwargs)

                except Exception as ex:
                    print("Erro:", ex)
                    response.update({"code": 500})
                    close_connection(conn)
            finally:
                if conn:
                    conn.close()
                return response

        return wrapper

    return decorator

