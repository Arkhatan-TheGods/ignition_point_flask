from sqlite3 import Cursor, Connection, connect
from typing import TypedDict, Callable, Any
import database_query

Operation = TypedDict('Operation', {'execute': Callable[[str, tuple], Any], 
                                    'fetchone': Callable[[str, tuple], Any], 
                                    'fetchall': Callable[[str, tuple], Any]})

def operator(cursor: Cursor) -> Operation:
    def execute(query: str, parameters: tuple):
        return cursor.execute(query, parameters)

    def fetchone(query: str, parameters: tuple) -> tuple:
        return cursor.execute(query, parameters).fetchone()

    def fetchall(query: str, parameters: tuple) -> list[tuple]:
        return cursor.execute(query, parameters).fetchall()
    
    def all(query: str) -> list[tuple]:
        return cursor.execute(query).fetchall()

    return {"execute": execute, "fetchone": fetchone, "fetchall": fetchall, "all": all}


def connect_to_db() -> Connection:
    try:
        conn = connect('store.db')
        return conn
    except Exception as e:
        print(e)


def create_table_costumer() -> None:
    try:
        conn = connect_to_db()
        cursor = conn.cursor()
        cursor.execute(database_query.create_table_costumer())
        conn.close()
    except Exception as e:
        print(e)