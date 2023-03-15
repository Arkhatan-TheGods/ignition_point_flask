from pytest import fixture, mark
from typing import Iterable
import main.infra.db.tables as db


@fixture(scope="function")
def setup() -> Iterable:

    # Arrange
    conn: db.Connection = db.execute_connect(":memory:")
    cursor: db.Cursor = conn.cursor()

    costumer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "27/01/2002",
                "Quadra 12 Conjunto F, 311")

    yield conn, cursor, costumer

    # Cleanup
    conn.close()

# @mark.skip(reason="")


def test_check_create_and_find_costumer_id(setup: tuple[db.Connection, db.Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    db.build_tables(cursor)

    query = """
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """
    cursor.execute(query, costumer)

    conn.commit()

    result = cursor.execute("SELECT ID FROM COSTUMERS WHERE ID = #ID", (cursor.lastrowid, ))

    # Assert
    assert (cursor.lastrowid,) == result.fetchone()


def test_check_edit_costumer_id(setup: tuple[db.Connection, db.Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    db.build_tables(cursor)

    query_create = """
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """
    cursor.execute(query_create, costumer)

    conn.commit()

    costumer_edit = ("Tomás Kaique",
                     "104.018.975-08",
                     "27/05/2002",
                     "Quadra QNL 4, 248",
                     cursor.lastrowid)

    query_edit = """
        UPDATE COSTUMERS 
        SET NAME = $NAME,
        CPF = $CPF,
        BIRTH_DATE = $BIRTH_DATE,
        ADDRESS = $ADDRESS
        WHERE ID = $ID;
    """
    cursor.execute(query_edit, costumer_edit)

    conn.commit()

    result = cursor.execute(
        """SELECT NAME, CPF, BIRTH_DATE, ADDRESS, ID 
        FROM COSTUMERS 
        WHERE ID = $ID;""", (cursor.lastrowid, ))

    # Assert
    assert costumer_edit == result.fetchone()


def test_check_remove_costumer_by_id(setup: tuple[db.Connection, db.Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    db.build_tables(cursor)

    query = """
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS);
    """
    cursor.execute(query, costumer)

    cursor.execute("DELETE FROM COSTUMERS WHERE ID = $ID;", (cursor.lastrowid,))

    conn.commit()

    result = cursor.execute("SELECT ID FROM COSTUMERS WHERE ID = $ID;",
                            (cursor.lastrowid,))

    # Assert
    assert result.fetchone() is None
