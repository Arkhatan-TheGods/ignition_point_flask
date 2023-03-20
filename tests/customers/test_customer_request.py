
from pytest import mark, fixture
from requests import get, post
import json


@fixture
def setup():
	# TODO: implementar versionamento /api/v1/
	# "name": "Tomás Kaique Assunção",
	return 'http://127.0.0.1:8080/customers/', {
		"name": "Kaique",
		"cpf": "942.554.492-10",
		"birth_date": "27/01/2002",
		"address": "Quadra 12 Conjunto F, 311"
	}


def test_post_customer_200(setup: tuple):

	uri, customer = setup

	input_data = json.dumps(customer)

	headers = {'Content-Type': 'application/json'}

	response = post(uri, input_data, headers=headers)

	assert 200 == response.status_code


@mark.skip(reason="reason for skipping the test case")
def test_get_all_customers(setup):

	uri, _ = setup

	response = get(uri)

	print("response:", response)

	# assert "942.554.492-10" == response.json()['cpf']
