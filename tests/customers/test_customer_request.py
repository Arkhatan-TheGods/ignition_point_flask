from main.config import get_config
from sqlite3 import Connection, connect
from re import match
from pytest import mark, fixture
from requests import get, post, put
from main.infra.db.query_tables import drop_tables, create_tables
from main.infra.db.execute_query import execute_query
from json import dumps


@fixture
def setup() -> tuple:
    # TODO: implementar versionamento /api/v1/

    config = get_config()

    data_base = config.get('file_db')

    if data_base is None:
        raise Exception(
            "Data base não identificado, verificar arquivo settings.yaml")

    conn = connect(data_base)

    cursor = conn.cursor()

    execute_query(cursor, drop_tables())

    execute_query(cursor, create_tables())

    conn.close()

    return ('http://127.0.0.1:8080/customers',
            {"name": "Yago André Almada",
             "cpf": "942.554.492-10",
             "birth_date": "27/01/2002",
             "address": "Quadra 12 Conjunto F, 311"})


@fixture
def setup_customers():

    config = get_config()

    data_base = config.get('file_db')

    if data_base is None:
        raise Exception(
            "Data base não identificado, verificar arquivo settings.yaml")

    conn = connect(data_base)

    cursor = conn.cursor()

    execute_query(cursor, drop_tables())

    execute_query(cursor, create_tables())

    cursor.executemany("INSERT INTO CUSTOMERS(NAME, CPF, BIRTH_DATE, ADDRESS) \
            VALUES(:NAME, :CPF, :BIRTH_DATE, :ADDRESS);", [("Yago André Almada",
                                                            "942.554.492-10",
                                                            "27/01/2002",
                                                            "Quadra 12 Conjunto F, 311"),
                                                           ("Maitê Daiane da Mata",
                                                            "648.487.491-31",
                                                            "23/01/1969",
                                                            "Rua Manoel Severino da Silva, 303"),
                                                           ("Nicolas Danilo Leonardo da Rocha",
                                                            "219.581.745-30",
                                                            "04/01/1945",
                                                            "Conjunto Residencial 1 Condomínio 1 Bloco C, 568")])

    conn.commit()
    conn.close()

    return 'http://127.0.0.1:8080/customers/'

# @mark.skip(reason="")


def test_only_portuguese_words_with_space(setup: tuple) -> None:

    pattern_name = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\s]+$"

    assert match(pattern_name, setup[1]["name"])


# @mark.skip(reason="")
def test_post_customer_200(setup: tuple) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    response = post(f"{uri}/", input_data, headers=headers)

    assert 201 == response.status_code


# @mark.skip(reason="")
def test_get_all_customers(setup_customers) -> None:

    uri = setup_customers

    response = get(f"{uri}/")

    assert 200 == response.status_code and response.json().get("customers")

# @mark.skip(reason="")


def test_get_by_customer_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    response = get(f'{uri}/{1}')

    print(response.json())

    assert 200 == response.status_code and response.json().get("customer")


# @mark.skip(reason="")
def test_get_customer_by_cpf(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    response = get(f'{uri}/{customer.get("cpf")}')

    assert 200 == response.status_code and response.json().get("customer")


def test_get_customer_by_name(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    response = get(f'{uri}/{customer.get("name")}/name')

    print(response.json().get("customer"))

    assert 200 == response.status_code and response.json().get("customer")


def test_update_customer_name_by_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    customer['name'] = 'João Grilo'

    input_data = dumps(customer)

    response_put = put(f'{uri}/{1}', input_data, headers=headers)

    response = get(f'{uri}/{customer.get("name")}/name')

    assert 204 == response_put.status_code and customer['name'] == response.json().get('customer')[0][1]


def test_update_customer_cpf_by_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    customer['cpf'] = '123.456.789-00'

    input_data = dumps(customer)

    response_put = put(f'{uri}/{1}', input_data, headers=headers)

    response = get(f'{uri}/{customer.get("cpf")}')

    assert 204 == response_put.status_code and customer['cpf'] == response.json().get('customer')[2]


def test_update_customer_birth_by_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    customer['birth_date'] = '01/01/2000'

    input_data = dumps(customer)

    response_put = put(f'{uri}/{1}', input_data, headers=headers)

    response = get(f'{uri}/{1}')
    print('>>>>>>>>>>',response.json())

    assert 204 == response_put.status_code and customer['birth_date'] == response.json().get('customer')[3]

def test_update_customer_adress_by_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)

    customer['address'] = 'Av. Paulista, 3000, São Paulo/SP'

    input_data = dumps(customer)

    response_put = put(f'{uri}/{1}', input_data, headers=headers)

    response = get(f'{uri}/{1}')
    print('>>>>>>>>>>',response.json())

    assert 204 == response_put.status_code and customer['address'] == response.json().get('customer')[4]


def test_delete_customer_by_id(setup) -> None:

    uri, customer = setup

    input_data = dumps(customer)

    headers = {'Content-Type': 'application/json'}

    post(uri, input_data, headers=headers)
