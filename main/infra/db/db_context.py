from sqlite3 import Connection, Cursor, connect

def execute_connect(db: str) -> Connection:
    return connect(db)
