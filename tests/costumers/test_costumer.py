from pytest import fixture, mark
from typing import Iterable
from main.infra.db.db_context import Connection, Cursor, execute_connect
from main.infra.db.query_tables import query_tables


@fixture(scope="function")
def setup() -> Iterable:

    # Arrange
    conn: Connection = execute_connect(":memory:")
    cursor: Cursor = conn.cursor()

    costumer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "27/01/2002",
                "Quadra 12 Conjunto F, 311")

    yield conn, cursor, costumer

    # Cleanup
    conn.close()

# @mark.skip(reason="")


def test_check_create_and_find_costumer_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    cursor.executescript(query_tables())

    cursor.execute("""
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """, costumer)

    conn.commit()

    result = cursor.execute("SELECT ID FROM COSTUMERS WHERE ID=$ID",
                            (cursor.lastrowid,))

    # Assert
    assert (cursor.lastrowid,) == result.fetchone()


def test_check_edit_costumer_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    cursor.executescript(query_tables())

    cursor.execute("""
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """, costumer)

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


def test_check_remove_costumer_by_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, costumer = setup

    # Act
    cursor.executescript(query_tables())

    cursor.execute("""
    INSERT INTO COSTUMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS);
    """, costumer)

    cursor.execute("DELETE FROM COSTUMERS WHERE ID=$ID;",
                   (cursor.lastrowid,))

    conn.commit()

    result = cursor.execute("SELECT ID FROM COSTUMERS WHERE ID=$ID;",
                            (cursor.lastrowid,))

    # Assert
    assert result.fetchone() is None
