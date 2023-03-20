from sqlite3 import Connection, connect
import database_query
def build_tables(data_base: str):

    conn: Connection | None = None

    try:
        conn = connect(data_base)
        cursor = conn.cursor()
        cursor.execute(database_query.create_table_customer())

    except Exception as e:
        print(e)

    finally:
        if conn:
            conn.close()
