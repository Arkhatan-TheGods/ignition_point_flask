from pytest import fixture
from main.services.validators.customer_validator import customer_validator

@fixture
def setup() -> tuple:

    return ("Tomas Kaique Assun",
            "942.554.492-10",
            "28/02/2002",
            "Quadra 12 Conjunto F, 311")


def test_name_is_alpha(setup: tuple) -> None:
    print(setup)
    input_data_validation, validation_by_id, validation_by_CPF, validation_by_name = customer_validator()

    notifications = input_data_validation(setup)

    assert [] == notifications
