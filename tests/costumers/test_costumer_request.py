
from pytest import mark, fixture
from requests import get, post
import json


@fixture
def setup():
	# TODO: implementar versionamento /api/v1/
	return 'http://127.0.0.1:8080/costumers/', {
		"name": "Tomás Kaique Assunção",
		"cpf": "942.554.492-10",
		"birth_date": "27/01/2002",
		"address": "Quadra 12 Conjunto F, 311"
	}


def test_post_costumer_200(setup: tuple):

	uri_consumer, consumer = setup

	input_data = json.dumps(consumer)

	headers = {'Content-Type': 'application/json'}

	response = post(uri_consumer, input_data, headers=headers)

	assert 200 == response.status_code


# @mark.skip(reason="reason for skipping the test case")
def test_get_all_costumers(setup):

	uri_consumer, _ = setup

	response = get(uri_consumer)

	print("response:", response)

	# assert "942.554.492-10" == response.json()['cpf']
