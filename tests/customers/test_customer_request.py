from main.config import get_config
from sqlite3 import Connection, connect
from re import match
from pytest import mark, fixture
from requests import get, post
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

	return ('http://127.0.0.1:8080/customers/',
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

	pattner_name = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\s]+$"

	assert match(pattner_name, setup[1]["name"])


# @mark.skip(reason="")
def test_post_customer_200(setup: tuple) -> None:

	uri, customer = setup

	input_data = dumps(customer)

	headers = {'Content-Type': 'application/json'}

	response = post(uri, input_data, headers=headers)

	assert 200 == response.status_code


# @mark.skip(reason="")
def test_get_all_customers(setup_customers) -> None:

	response = get(setup_customers)

	assert 200 == response.status_code and response.json().get("customers")

# @mark.skip(reason="")
def test_get_by_customer_id(setup) -> None:

	uri, customer = setup

	input_data = dumps(customer)

	headers = {'Content-Type': 'application/json'}

	post(uri, input_data, headers=headers)

	response = get(f'{uri}{1}')

	assert 200 == response.status_code and response.json().get("customer")


# @mark.skip(reason="")
def test_get_customer_by_cpf(setup) -> None:

	uri, customer = setup
	
	input_data = dumps(customer)

	headers = {'Content-Type': 'application/json'}

	post(uri, input_data, headers=headers)

	response = get(f'{uri}{customer.get("cpf")}')

	assert 200 == response.status_code and response.json().get("customer")
