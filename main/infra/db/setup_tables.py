from db_context import Connection


def setup_tables(conn: Connection, query: str):

    status: bool = False

    try:
        conn.cursor().executescript(query)
    except Exception as ex:
        print(ex)
    finally:
        if conn:
            status = True
        return status
