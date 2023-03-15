from pytest import fixture, mark
from typing import Iterable
import main.infra.db.tables as db

@fixture(scope="function")
def setup() -> Iterable:

    # Arrange
    conn: db.Connection = db.execute_connect(":memory:")
    cursor: db.Cursor = conn.cursor()

    yield conn, cursor

    # Cleanup
    conn.close()

# @mark.skip(reason="")

# @mark.skip(reason="")
def test_check_create_and_find_product_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

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


def test_check_edit_product_by_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

    # Act
    db.build_tables(cursor)

    costumer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "11/03/1952",
                "Quadra 12 Conjunto F, 311")

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

def test_check_remove_product_by_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

    # Act
    db.build_tables(cursor)

    costumer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "11/03/1952",
                "Quadra 12 Conjunto F, 311")

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