from sqlite3 import Connection, Cursor, connect

conn: Connection | None = None


def execute_connect(db: str):
    return connect(db)


def build_tables(cursor: Cursor):

    query = """
            BEGIN;
            CREATE TABLE IF NOT EXISTS COSTUMERS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CPF TEXT NOT NULL UNIQUE,
                BIRTH_DATE TEXT NOT NULL,
                ADDRESS TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );

            CREATE TABLE IF NOT EXISTS PRODUCTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            COMMIT;
            """
    cursor.executescript(query)
