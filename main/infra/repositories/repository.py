from sqlite3 import Cursor

def repository(cursor: Cursor) -> dict:
    def execute(query: str, parameters: tuple):
        cursor.execute(query, parameters)
        return cursor.fetchone()
    
    def fetchone(query: str, parameters: tuple) -> tuple:
        return cursor.execute(query, parameters).fetchone()

    def fetchall(query: str, parameters: tuple) -> list[tuple]:
        return cursor.execute(query, parameters).fetchall()
    
    def all_results(query: str) -> list[tuple]:
        return cursor.execute(query).fetchall()

    return {"execute": execute, "fetchone": fetchone, "fetchall": fetchall, "all": all_results}
