from infra.db.db_context import Connection


def create_tables(conn: Connection, query: str) -> None:
    conn.cursor().executescript(query)
