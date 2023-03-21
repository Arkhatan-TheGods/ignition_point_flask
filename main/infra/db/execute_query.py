from sqlite3 import Cursor

def execute_query(cursor: Cursor, query: str) -> None:
    cursor.executescript(query)
