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

def test_check_create_and_find_product_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

    # Act
    db.build_tables(cursor)

    cursor.execute("INSERT INTO PRODUCTS(NAME) VALUES ($NAME)",
                   ("Black Coffe",))

    conn.commit()

    result = cursor.execute("SELECT ID FROM PRODUCTS WHERE ID=$ID",
                            (cursor.lastrowid, ))

    # Assert
    assert (cursor.lastrowid,) == result.fetchone()


def test_check_edit_product_by_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

    # Act
    db.build_tables(cursor)
    
    cursor.execute("INSERT INTO PRODUCTS(NAME) VALUES ($NAME);", 
                   ("Black Coffe",))

    product_edit = ("Real Black Coffee", cursor.lastrowid)

    cursor.execute("UPDATE PRODUCTS SET NAME = $NAME WHERE ID = $ID;", 
                   product_edit)

    conn.commit()

    result = cursor.execute("SELECT NAME, ID FROM PRODUCTS WHERE ID=$ID;",
                            (cursor.lastrowid,))

    # Assert
    assert product_edit == result.fetchone()

def test_check_remove_product_by_id(setup: tuple[db.Connection, db.Cursor]):

    conn, cursor = setup

    # Act
    db.build_tables(cursor)

    cursor.execute("INSERT INTO PRODUCTS(NAME) VALUES ($NAME);",
                   ("Black Coffe",))

    cursor.execute("DELETE FROM PRODUCTS WHERE ID = $ID;",
                   (cursor.lastrowid, ))

    conn.commit()

    result = cursor.execute("SELECT ID FROM PRODUCTS WHERE ID=$ID;",
                            (cursor.lastrowid, ))

    # Assert
    assert result.fetchone() is None