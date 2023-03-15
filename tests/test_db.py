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


@mark.parametrize("table", ["COSTUMERS", "PRODUCTS"])
def test_create_tables_costumers_and_products(setup: tuple[db.Connection, db.Cursor, str], table: str):

    _, cursor, query = setup

    # Act
    db.build_tables(cursor)

    table_name = cursor.execute(query.replace(
        "{TABLE}", table)).fetchone()

    # Assert
    assert (table,) == table_name

def test_check_create_costumer(setup: tuple[db.Connection, db.Cursor, str]):

    conn, cursor, _ = setup

    # Act
    db.build_tables(cursor)
 
    costumer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "11/03/1952",
                "Quadra 12 Conjunto F, 311")

    # todo:SQL injection - addslashes()
    query = """
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """
    cursor.execute(query, costumer)
    
    conn.commit()

    print("lastrowid:", cursor.lastrowid)

    result = cursor.execute("SELECT ID FROM COSTUMERS")
    
    # Assert
    assert (cursor.lastrowid,) == result.fetchone()


# @mark.skip(reason="")
def test_check_create_products(setup: tuple[db.Connection, db.Cursor, str]):

    conn, cursor, _ = setup

    # Act
    db.build_tables(cursor)
 
    product = ("Black Coffe",)

    query = "INSERT INTO PRODUCTS(NAME) VALUES ($NAME)"
    
    cursor.execute(query, product)
    
    conn.commit()

    print("lastrowid:", cursor.lastrowid)

    result = cursor.execute("SELECT ID FROM PRODUCTS")
    
    # Assert
    assert (cursor.lastrowid,) == result.fetchone()