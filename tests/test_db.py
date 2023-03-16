from pytest import fixture, mark
from typing import Iterable
from main.infra.db.db_context import Connection, Cursor, execute_connect
from main.infra.db.query_tables import query_tables


@fixture(scope="function")
def setup() -> Iterable:

    # Arrange
    conn: Connection = execute_connect(":memory:")
    cursor: Cursor = conn.cursor()

    query = """SELECT NAME 
    FROM sqlite_master 
    WHERE type='table' 
    AND name='{TABLE}';"""

    yield conn, cursor, query

    # Cleanup
    conn.close()

@mark.parametrize("table", ["COSTUMERS", "PRODUCTS"])
def test_create_tables_costumers_and_products(setup: tuple[Connection, Cursor, str], table: str):

    _, cursor, query = setup

    # Act
    cursor.executescript(query_tables())

    table_name = cursor.execute(query.replace(
        "{TABLE}", table)).fetchone()

    # Assert
    assert (table,) == table_name

# @mark.skip(reason="")
