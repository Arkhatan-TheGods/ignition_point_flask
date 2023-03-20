from sqlite3 import Connection, Cursor, connect

def execute_connect(database: str) -> Connection:
    return connect(database)
