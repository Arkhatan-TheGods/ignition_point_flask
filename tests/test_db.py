from pytest import fixture, mark
from typing import Iterable
import main.infra.db.tables as db


@fixture(scope="function")
def setup() -> Iterable:

    # Arrange
    conn: db.Connection = db.execute_connect(":memory:")
    cursor: db.Cursor = conn.cursor()

    query = """SELECT NAME 
    FROM sqlite_master 
    WHERE type='table' 
    AND name='{TABLE}';"""

    yield conn, cursor, query

    # Cleanup
    conn.close()

# @mark.skip(reason="")


@mark.parametrize("table", ["COSTUMERS", "PRODUCTS"])
def test_create_tables_costumers_and_products(setup: tuple[db.Connection, db.Cursor, str], table: str):

    _, cursor, query = setup

    # Act
    db.build_tables(cursor)

    table_name = cursor.execute(query.replace(
        "{TABLE}", table)).fetchone()

    # Assert
    assert (table,) == table_name

# @mark.skip(reason="")
