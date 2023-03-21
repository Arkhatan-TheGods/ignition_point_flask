from pytest import fixture, mark
from typing import Iterable
from main.infra.db.db_context import Connection, Cursor, execute_connect
from main.infra.db.query_tables import create_tables,drop_tables

@fixture
def setup() -> Iterable:

    # Arrange
    conn: Connection = execute_connect(":memory:")
    cursor: Cursor = conn.cursor()

    customer = ("Tomás Kaique Assunção",
                "942.554.492-10",
                "27/01/2002",
                "Quadra 12 Conjunto F, 311")

    yield conn, cursor, customer

    # Cleanup
    conn.close()

# @mark.skip(reason="")


def test_check_create_and_find_customer_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, customer = setup

    # Act
    cursor.executescript(create_tables())

    cursor.execute("""
    INSERT INTO CUSTOMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """, customer)

    conn.commit()

    result = cursor.execute("SELECT ID FROM CUSTOMERS WHERE ID=$ID",
                            (cursor.lastrowid,))

    # Assert
    assert (cursor.lastrowid,) == result.fetchone()


def test_check_edit_customer_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, customer = setup

    # Act
    cursor.executescript(create_tables())

    cursor.execute("""
    INSERT INTO CUSTOMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS)
    """, customer)

    conn.commit()

    customer_edit = ("Tomás Kaique",
                     "104.018.975-08",
                     "27/05/2002",
                     "Quadra QNL 4, 248",
                     cursor.lastrowid)

    query_edit = """
        UPDATE CUSTOMERS 
        SET NAME = $NAME,
        CPF = $CPF,
        BIRTH_DATE = $BIRTH_DATE,
        ADDRESS = $ADDRESS
        WHERE ID = $ID;
    """
    cursor.execute(query_edit, customer_edit)

    conn.commit()

    result = cursor.execute(
        """SELECT NAME, CPF, BIRTH_DATE, ADDRESS, ID 
        FROM CUSTOMERS 
        WHERE ID = $ID;""", (cursor.lastrowid, ))

    # Assert
    assert customer_edit == result.fetchone()


def test_check_remove_customer_by_id(setup: tuple[Connection, Cursor, tuple]):

    conn, cursor, customer = setup

    # Act
    cursor.executescript(create_tables())

    cursor.execute("""
    INSERT INTO CUSTOMERS(NAME, CPF, BIRTH_DATE, ADDRESS) 
    VALUES ($NAME, $CPF, $BIRTH_DATE, $ADDRESS);
    """, customer)

    cursor.execute("DELETE FROM CUSTOMERS WHERE ID=$ID;",
                   (cursor.lastrowid,))

    conn.commit()

    result = cursor.execute("SELECT ID FROM CUSTOMERS WHERE ID=$ID;",
                            (cursor.lastrowid,))

    # Assert
    assert result.fetchone() is None