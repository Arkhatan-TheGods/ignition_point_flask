from main.config import get_config
from sqlite3 import Connection, Cursor, connect
from re import match
from pytest import mark, fixture
from requests import get, post
import json


@fixture
def setup() -> tuple:
	# TODO: implementar versionamento /api/v1/

	config = get_config()
	
	data_base = config.get('file_db')
	
	if data_base is None:
		raise Exception(
			"Data base não identificado, verificar arquivo settings.yaml")

	conn: Connection = connect(data_base)

	cursor: Cursor = conn.cursor()

	cursor.executescript("""
	BEGIN;
		
		DROP TABLE IF EXISTS CUSTOMERS;
		DROP TABLE IF EXISTS PRODUCTS;
		
		CREATE TABLE IF NOT EXISTS CUSTOMERS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CPF TEXT NOT NULL UNIQUE,
                BIRTH_DATE TEXT NOT NULL,
                ADDRESS TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

            CREATE TABLE IF NOT EXISTS PRODUCTS(
                ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                NAME TEXT NOT NULL,
                CREATED_AT TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            COMMIT;""")

	cursor.close()

	conn.close()

	return ('http://127.0.0.1:8080/customers/',
         [{"name": "Yago André Almada",
           "cpf": "942.554.492-10",
           "birth_date": "27/01/2002",
           "address": "Quadra 12 Conjunto F, 311"},
          {"name": "Maitê Daiane da Mata",
           "cpf": "648.487.491-31",
           "birth_date": "23/01/1969",
           "address": "Rua Manoel Severino da Silva, 303"},
          {"name": "Nicolas Danilo Leonardo da Rocha",
           "cpf": "219.581.745-30",
           "birth_date": "04/01/1945",
           "address": "Conjunto Residencial 1 Condomínio 1 Bloco C, 568"}])

@mark.skip(reason="")
def test_only_portuguese_words_with_space(setup: tuple) -> None:

	pattner_name = "^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ\\s]+$"

	assert match(pattner_name, setup[1][0]["name"])

@mark.skip(reason="")
def test_post_customer_200(setup: tuple) -> None:

	uri, customer = setup
	
	input_data = json.dumps(customer[1])

	headers = {'Content-Type': 'application/json'}

	response = post(uri, input_data, headers=headers)

	assert 200 == response.status_code


@mark.skip(reason="")
def test_get_all_customers(setup) -> None:

	uri, customers = setup

	for customer in customers:

		input_data = json.dumps(customer)

		headers = {'Content-Type': 'application/json'}

		post(uri, input_data, headers=headers)

	response = get(uri)

	print(response.json())

	assert 200 == response.status_code and [] != response

# @mark.skip(reason="")
def test_get_by_customer_id(setup) -> None:

	uri, customers = setup
	
	input_data = json.dumps(customers[1])

	headers = {'Content-Type': 'application/json'}

	post(uri, input_data, headers=headers)

	response = get(f'{uri}{1}')

	print("response:>>>>>>>>>>", json.loads(response.content))

	assert 200 == response.status_code and () != response

@mark.skip(reason="")
def test_get_customer_by_cpf(setup) -> None:

	uri, customers = setup
	
	input_data = json.dumps(customers[1])

	headers = {'Content-Type': 'application/json'}

	post(uri, input_data, headers=headers)

	response = get(f'{uri}{customers[1][1]}')

	print("response:>>>>>>>>>>", response)

	# assert 200 == response.status_code and () != response